from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QListWidgetItem
from qgis.core import QgsProject
import os

from .mosaic_dialog_base import Ui_MosaicDialog
from .mosaic_algorithm import MosaicAlgorithm

class MosaicDialog(QtWidgets.QDialog, Ui_MosaicDialog):
    def __init__(self, iface, parent=None):
        super(MosaicDialog, self).__init__(parent)
        self.iface = iface  # Store the iface parameter
        self.setupUi(self)
        self.setFixedWidth(600)  # Make the plugin window wider
        self.run_button.clicked.connect(self.run_mosaic)
        self.cancel_button.clicked.connect(self.close)
        self.open_raster_button.clicked.connect(self.open_raster)
        self.select_all_button.clicked.connect(self.select_unselect_all)
        self.remove_button.clicked.connect(self.remove_selected)
        self.browse_button.clicked.connect(self.browse_output_file)
        self.show_advanced_options_checkbox.stateChanged.connect(self.toggle_advanced_options)
        self.input_mode.currentIndexChanged.connect(self.update_input_mode)
        self.load_opened_rasters()
        self.toggle_advanced_options()

    def load_opened_rasters(self):
        self.raster_list.clear()
        layers = [layer for layer in QgsProject.instance().mapLayers().values() if layer.type() == layer.RasterLayer]
        for layer in layers:
            item = QListWidgetItem(layer.name())
            item.setCheckState(QtCore.Qt.Checked)
            self.raster_list.addItem(item)

    def open_raster(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Open Raster Files", "", "Raster Files (*.tif *.img *.hdr)")
        for file in files:
            item = QListWidgetItem(os.path.basename(file))
            item.setCheckState(QtCore.Qt.Checked)
            item.setData(QtCore.Qt.UserRole, file)
            self.raster_list.addItem(item)

    def select_unselect_all(self):
        for index in range(self.raster_list.count()):
            item = self.raster_list.item(index)
            item.setCheckState(QtCore.Qt.Unchecked if item.checkState() == QtCore.Qt.Checked else QtCore.Qt.Checked)

    def remove_selected(self):
        for item in self.raster_list.selectedItems():
            self.raster_list.takeItem(self.raster_list.row(item))

    def browse_output_file(self):
        file, _ = QFileDialog.getSaveFileName(self, "Save Output File", "", "TIF Files (*.tif);;All Files (*)")
        if file:
            self.output_file.setText(file)

    def toggle_advanced_options(self):
        visible = self.show_advanced_options_checkbox.isChecked()
        self.advanced_options.setVisible(visible)
        self.adjustSize()

    def update_input_mode(self):
        if self.input_mode.currentText() == "Single Band":
            self.band.setValue(1)
            self.band.setEnabled(False)
        else:
            self.band.setEnabled(True)

    def run_mosaic(self):
        input_layers = []
        for index in range(self.raster_list.count()):
            item = self.raster_list.item(index)
            if item.checkState() == QtCore.Qt.Checked:
                layer = QgsProject.instance().mapLayersByName(item.text())
                if not layer:
                    input_layers.append(item.data(QtCore.Qt.UserRole))
                else:
                    input_layers.append(layer[0].source())

        output_file = self.output_file.text()
        mode = self.input_mode.currentIndex()
        stat = self.algorithm.currentIndex()
        data_type = self.data_type.currentText()

        mosaic_algorithm = MosaicAlgorithm()
        mosaic_algorithm.create_mosaic(input_layers, output_file, mosaic_algorithm.STAT_KEYS[stat], data_type, mode)

        if self.open_output_checkbox.isChecked():
            self.iface.addRasterLayer(output_file, "Mosaic Output")

        QMessageBox.information(self, "Mosaic Plugin", "Mosaic created successfully!")
