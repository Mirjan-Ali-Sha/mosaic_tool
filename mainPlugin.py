from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from qgis.core import QgsApplication
import os
from .resources_rc import *
from qgis.core import QgsProject
from qgis.utils import iface
from PyQt5.QtWidgets import QAction, QFileDialog, QTableWidgetItem, QToolBar

from .mosaic_dialog import MosaicDialog

class MosaicPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.actions = []
        self.menu = self.tr(u"&MAS Raster Processing")
        self.toolbar = None
        self.first_start = None
        # self.select_all_state = True  # Added to keep track of the select all/unselect all state

    def tr(self, message):
        return QCoreApplication.translate('MosaicPlugin', message)


    def initGui(self):
        icon_path = ':/mosaic.png'
        # Check if the toolbar already exists, if not create it
        self.toolbar = self.iface.mainWindow().findChild(QToolBar, 'MASRasterProcessingToolbar')
        if self.toolbar is None:
            self.toolbar = self.iface.addToolBar(u'MAS Raster Processing')
            self.toolbar.setObjectName('MASRasterProcessingToolbar')

        self.action_mosaic = QAction(QIcon(icon_path), u"&Mosaic Tool", self.iface.mainWindow())
        self.action_mosaic.triggered.connect(self.run)
        self.iface.addPluginToRasterMenu(self.menu, self.action_mosaic)
        self.toolbar.addAction(self.action_mosaic)
        self.actions.append(self.action_mosaic)
        # self.add_action(icon_path, self.tr("Mosaic Tool"), self.run)

    def add_action(self, icon_path, text, callback, parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if add_to_toolbar:
            self.toolbar.addAction(action)
        if add_to_menu:
            self.iface.addPluginToRasterMenu(self.menu, action)
        self.actions.append(action)
        return action


    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(self.tr(u'&MAS Raster Processing'), action)
            self.iface.removeToolBarIcon(action)
        if self.toolbar:
            del self.toolbar

    def run(self):
        dialog = MosaicDialog(self.iface, self.iface.mainWindow())  # Pass iface here
        dialog.exec_()
