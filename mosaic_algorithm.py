import os
import numpy as np
from osgeo import gdal
from qgis.core import QgsProcessingAlgorithm, QgsProcessingParameterMultipleLayers, QgsProcessingParameterEnum, QgsProcessingParameterRasterDestination

class MosaicAlgorithm(QgsProcessingAlgorithm):
    INPUTS = 'INPUTS'
    MODE = 'MODE'
    STAT = 'STAT'
    OUTPUT = 'OUTPUT'
    DATA_TYPE = 'DATA_TYPE'

    STAT_KEYS = ['median', 'mean', 'gmean', 'max', 'min', 'std', 'valid_pixels', 'last_pixel', 'jday_last_pixel', 'jday_median', 'linear_trend']
    DATA_TYPES = ['Default', 'Byte', 'UInt16', 'Int16', 'UInt32', 'Int32', 'Float32', 'Float64']

    def __init__(self):
        super().__init__()

    def name(self):
        return 'mosaic'

    def displayName(self):
        return self.tr('Mosaic')

    def group(self):
        return self.tr('Raster')

    def groupId(self):
        return 'raster'

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterMultipleLayers(
                self.INPUTS,
                self.tr('Input layers'),
                QgsProcessing.TypeRaster
            )
        )

        self.addParameter(
            QgsProcessingParameterEnum(
                self.MODE,
                self.tr('Mode'),
                ['Single Band', 'Multiple Bands'],
                defaultValue=0
            )
        )

        self.addParameter(
            QgsProcessingParameterEnum(
                self.STAT,
                self.tr('Computation Algorithm for Overlap Area'),
                self.STAT_KEYS,
                defaultValue=0
            )
        )

        self.addParameter(
            QgsProcessingParameterEnum(
                self.DATA_TYPE,
                self.tr('Output Data Type'),
                self.DATA_TYPES,
                defaultValue=0
            )
        )

        self.addParameter(
            QgsProcessingParameterRasterDestination(
                self.OUTPUT,
                self.tr('Output file')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        layers = self.parameterAsLayerList(parameters, self.INPUTS, context)
        mode = self.parameterAsEnum(parameters, self.MODE, context)
        stat = self.parameterAsEnum(parameters, self.STAT, context)
        data_type = self.parameterAsEnum(parameters, self.DATA_TYPE, context)
        output = self.parameterAsOutputLayer(parameters, self.OUTPUT, context)

        input_files = [layer.source() for layer in layers]
        self.create_mosaic(input_files, output, self.STAT_KEYS[stat], self.DATA_TYPES[data_type], mode)

        return {self.OUTPUT: output}

    def create_mosaic(self, input_files, output_file, stat, data_type, mode):
        # Read input files
        datasets = [gdal.Open(file) for file in input_files]
        bands = [ds.GetRasterBand(1).ReadAsArray() for ds in datasets]

        # Determine the data type of the input files if Default is selected
        if data_type == 'Default':
            gdal_data_type = datasets[0].GetRasterBand(1).DataType
        else:
            gdal_data_type = {
                'Default': gdal.GDT_Unknown,
                'Byte': gdal.GDT_Byte,
                'UInt16': gdal.GDT_UInt16,
                'Int16': gdal.GDT_Int16,
                'UInt32': gdal.GDT_UInt32,
                'Int32': gdal.GDT_Int32,
                'Float32': gdal.GDT_Float32,
                'Float64': gdal.GDT_Float64
            }[data_type]

        # Stack the bands along the third axis
        stack = np.dstack(bands)

        # Apply the chosen statistic
        if stat == 'median':
            result = np.median(stack, axis=2)
        elif stat == 'mean':
            result = np.mean(stack, axis=2)
        elif stat == 'gmean':
            result = np.exp(np.mean(np.log(stack + 1e-10), axis=2))  # Add small value to avoid log(0)
        elif stat == 'max':
            result = np.max(stack, axis=2)
        elif stat == 'min':
            result = np.min(stack, axis=2)
        elif stat == 'std':
            result = np.std(stack, axis=2)
        elif stat == 'valid_pixels':
            result = np.sum(stack != 0, axis=2)
        elif stat == 'last_pixel':
            result = stack[:, :, -1]
        elif stat == 'jday_last_pixel':
            result = stack[:, :, -1]  # This needs actual Julian day values
        elif stat == 'jday_median':
            result = np.median(stack, axis=2)  # This needs actual Julian day values
        elif stat == 'linear_trend':
            result = self.linear_trend(stack)

        # Write output file
        self.write_output(output_file, result, datasets[0], gdal_data_type)

    def linear_trend(self, stack):
        x = np.arange(stack.shape[2])
        y = stack.reshape(-1, stack.shape[2])
        A = np.vstack([x, np.ones(len(x))]).T
        slope = np.linalg.lstsq(A, y.T, rcond=None)[0][0]
        return slope.reshape(stack.shape[:2])

    def write_output(self, output_file, result, ref_dataset, gdal_data_type):
        driver = gdal.GetDriverByName('GTiff')
        out_ds = driver.Create(output_file, ref_dataset.RasterXSize, ref_dataset.RasterYSize, 1, gdal_data_type)
        out_ds.SetGeoTransform(ref_dataset.GetGeoTransform())
        out_ds.SetProjection(ref_dataset.GetProjection())
        out_band = out_ds.GetRasterBand(1)
        out_band.WriteArray(result)
        out_band.FlushCache()
        out_ds = None
