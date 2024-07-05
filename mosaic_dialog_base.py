# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mosaic_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MosaicDialog(object):
    def setupUi(self, MosaicDialog):
        MosaicDialog.setObjectName("MosaicDialog")
        MosaicDialog.resize(400, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(MosaicDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.raster_list = QtWidgets.QListWidget(MosaicDialog)
        self.raster_list.setObjectName("raster_list")
        self.raster_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.verticalLayout.addWidget(self.raster_list)
        
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setObjectName("buttons_layout")
        
        self.open_raster_button = QtWidgets.QPushButton(MosaicDialog)
        self.open_raster_button.setObjectName("open_raster_button")
        self.buttons_layout.addWidget(self.open_raster_button)
        
        self.select_all_button = QtWidgets.QPushButton(MosaicDialog)
        self.select_all_button.setObjectName("select_all_button")
        self.buttons_layout.addWidget(self.select_all_button)
        
        self.remove_button = QtWidgets.QPushButton(MosaicDialog)
        self.remove_button.setObjectName("remove_button")
        self.buttons_layout.addWidget(self.remove_button)
        
        self.verticalLayout.addLayout(self.buttons_layout)
        
        self.open_output_checkbox = QtWidgets.QCheckBox(MosaicDialog)
        self.open_output_checkbox.setObjectName("open_output_checkbox")
        self.verticalLayout.addWidget(self.open_output_checkbox)
        
        self.output_path_layout = QtWidgets.QHBoxLayout()
        self.output_path_layout.setObjectName("output_path_layout")
        
        self.output_label = QtWidgets.QLabel(MosaicDialog)
        self.output_label.setObjectName("output_label")
        self.output_path_layout.addWidget(self.output_label)
        
        self.output_file = QtWidgets.QLineEdit(MosaicDialog)
        self.output_file.setObjectName("output_file")
        self.output_path_layout.addWidget(self.output_file)
        
        self.browse_button = QtWidgets.QPushButton(MosaicDialog)
        self.browse_button.setObjectName("browse_button")
        self.output_path_layout.addWidget(self.browse_button)
        
        self.verticalLayout.addLayout(self.output_path_layout)
        
        self.input_mode_layout = QtWidgets.QHBoxLayout()
        self.input_mode_layout.setObjectName("input_mode_layout")
        
        self.input_mode_label = QtWidgets.QLabel(MosaicDialog)
        self.input_mode_label.setObjectName("input_mode_label")
        self.input_mode_layout.addWidget(self.input_mode_label)
        
        self.input_mode = QtWidgets.QComboBox(MosaicDialog)
        self.input_mode.setObjectName("input_mode")
        self.input_mode.addItem("")
        self.input_mode.addItem("")
        self.input_mode_layout.addWidget(self.input_mode)
        
        self.verticalLayout.addLayout(self.input_mode_layout)
        
        self.algorithm_layout = QtWidgets.QHBoxLayout()
        self.algorithm_layout.setObjectName("algorithm_layout")
        
        self.algorithm_label = QtWidgets.QLabel(MosaicDialog)
        self.algorithm_label.setObjectName("algorithm_label")
        self.algorithm_layout.addWidget(self.algorithm_label)
        
        self.algorithm = QtWidgets.QComboBox(MosaicDialog)
        self.algorithm.setObjectName("algorithm")
        for alg in ['median', 'mean', 'gmean', 'max', 'min', 'std', 'valid_pixels', 'last_pixel', 'jday_last_pixel', 'jday_median', 'linear_trend']:
            self.algorithm.addItem(alg)
        self.algorithm_layout.addWidget(self.algorithm)
        
        self.verticalLayout.addLayout(self.algorithm_layout)
        
        self.show_advanced_options_checkbox = QtWidgets.QCheckBox(MosaicDialog)
        self.show_advanced_options_checkbox.setObjectName("show_advanced_options_checkbox")
        self.verticalLayout.addWidget(self.show_advanced_options_checkbox)
        
        self.advanced_options = QtWidgets.QWidget(MosaicDialog)
        self.advanced_options.setObjectName("advanced_options")
        self.advanced_options_layout = QtWidgets.QVBoxLayout(self.advanced_options)
        self.advanced_options_layout.setObjectName("advanced_options_layout")
        
        self.data_type_layout = QtWidgets.QHBoxLayout()
        self.data_type_layout.setObjectName("data_type_layout")
        
        self.data_type_label = QtWidgets.QLabel(self.advanced_options)
        self.data_type_label.setObjectName("data_type_label")
        self.data_type_layout.addWidget(self.data_type_label)
        
        self.data_type = QtWidgets.QComboBox(self.advanced_options)
        self.data_type.setObjectName("data_type")
        for dt in ['Default', 'Byte', 'UInt16', 'Int16', 'UInt32', 'Int32', 'Float32', 'Float64']:
            self.data_type.addItem(dt)
        self.data_type_layout.addWidget(self.data_type)
        
        self.advanced_options_layout.addLayout(self.data_type_layout)
        
        self.band_layout = QtWidgets.QHBoxLayout()
        self.band_layout.setObjectName("band_layout")
        
        self.band_label = QtWidgets.QLabel(self.advanced_options)
        self.band_label.setObjectName("band_label")
        self.band_layout.addWidget(self.band_label)
        
        self.band = QtWidgets.QSpinBox(self.advanced_options)
        self.band.setObjectName("band")
        self.band.setMinimum(1)
        self.band_layout.addWidget(self.band)
        
        self.advanced_options_layout.addLayout(self.band_layout)
        
        self.verticalLayout.addWidget(self.advanced_options)
        
        self.run_button = QtWidgets.QPushButton(MosaicDialog)
        self.run_button.setObjectName("run_button")
        self.verticalLayout.addWidget(self.run_button)
        
        self.cancel_button = QtWidgets.QPushButton(MosaicDialog)
        self.cancel_button.setObjectName("cancel_button")
        self.verticalLayout.addWidget(self.cancel_button)

        self.retranslateUi(MosaicDialog)
        QtCore.QMetaObject.connectSlotsByName(MosaicDialog)

    def retranslateUi(self, MosaicDialog):
        _translate = QtCore.QCoreApplication.translate
        MosaicDialog.setWindowTitle(_translate("MosaicDialog", "Mosaic Tool"))
        self.open_raster_button.setText(_translate("MosaicDialog", "Open Bands"))
        self.select_all_button.setText(_translate("MosaicDialog", "Select/Unselect All"))
        self.remove_button.setText(_translate("MosaicDialog", "Remove"))
        self.open_output_checkbox.setText(_translate("MosaicDialog", "Do you want to open the output in QGIS Interface?"))
        self.output_label.setText(_translate("MosaicDialog", "Output File:"))
        self.browse_button.setText(_translate("MosaicDialog", "Browse"))
        self.input_mode_label.setText(_translate("MosaicDialog", "Input Mode:"))
        self.input_mode.setItemText(0, _translate("MosaicDialog", "Single Band"))
        self.input_mode.setItemText(1, _translate("MosaicDialog", "Multiple Bands"))
        self.algorithm_label.setText(_translate("MosaicDialog", "Computation Algorithm:"))
        self.show_advanced_options_checkbox.setText(_translate("MosaicDialog", "Show Advanced Options"))
        self.data_type_label.setText(_translate("MosaicDialog", "Output Data Type:"))
        self.band_label.setText(_translate("MosaicDialog", "No of Output Band/s:"))
        self.run_button.setText(_translate("MosaicDialog", "Mosaic"))
        self.cancel_button.setText(_translate("MosaicDialog", "Cancel"))
 