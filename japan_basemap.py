# -*- coding: utf-8 -*-

"""
/***************************************************************************
 JapanBasemap
                                 A QGIS plugin
 指定されたベクタに交差(intersect)する範囲内で、指定した地図情報レベルの国土基本図図郭を生成します
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-06-18
        copyright            : (C) 2022 by Epoppo
        email                : poppo.circle@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = "Epoppo"
__date__ = "2022-06-18"
__copyright__ = "(C) 2022 by Epoppo"

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = "$Format:%H$"

import inspect
import os
import sys

from qgis.core import QgsApplication, QgsProcessingAlgorithm

from .japan_basemap_provider import JapanBasemapProvider

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


class JapanBasemapPlugin(object):
    def __init__(self):
        self.provider = None

    def initProcessing(self):
        """Init Processing provider for QGIS >= 3.8."""
        self.provider = JapanBasemapProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
