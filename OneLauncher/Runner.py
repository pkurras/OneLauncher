# coding=utf-8
###########################################################################
# Runner for OneLauncher.
#
# Based on PyLotRO
# (C) 2009 AJackson <ajackson@bcs.org.uk>
#
# Based on LotROLinux
# (C) 2007-2008 AJackson <ajackson@bcs.org.uk>
#
#
# (C) 2019-2021 June Stepp <contact@JuneStepp.me>
#
# This file is part of OneLauncher
#
# OneLauncher is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# OneLauncher is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with OneLauncher.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################
import sys

from PySide6 import QtCore, QtGui, QtWidgets

from OneLauncher import Settings


def main():
    global app
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QtWidgets.QApplication(sys.argv)

    # Set font size explicitly to stop OS text size options from
    # breaking the UI.
    font = QtGui.QFont()
    font.setPointSize(10)
    app.setFont(font)

    handle_windows_dark_theme()

    # Import has to be done here, because some code run by
    # MainWindow imports requires the QApplication to exist.
    from OneLauncher.MainWindow import MainWindow
    main_window = MainWindow()
    main_window.run()

    sys.exit(app.exec())


def handle_windows_dark_theme():
    if not Settings.usingWindows:
        return

    settings = QtCore.QSettings("HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize",
                                QtCore.QSettings.NativeFormat)
    # If user has dark theme activated
    if not settings.value("AppsUseLightTheme"):
        # Use QPalette to set custom dark theme for Windows.
        # The builtin Windows dark theme for Windows is not ready
        # as of 7-5-2021
        app.setStyle(QtWidgets.QStyleFactory.create("Fusion"))
        dark_palette = QtGui.QPalette()
        dark_color = QtGui.QColor(45, 45, 45)
        disabled_color = QtGui.QColor(127, 127, 127)

        dark_palette.setColor(QtGui.QPalette.Window, dark_color)
        dark_palette.setColor(QtGui.QPalette.WindowText, QtCore.Qt.white)
        dark_palette.setColor(QtGui.QPalette.Base,
                              QtGui.QColor(18, 18, 18))
        dark_palette.setColor(QtGui.QPalette.AlternateBase, dark_color)
        dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtCore.Qt.white)
        dark_palette.setColor(QtGui.QPalette.ToolTipText, QtCore.Qt.white)
        dark_palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        dark_palette.setColor(QtGui.QPalette.Disabled,
                              QtGui.QPalette.Text, disabled_color)
        dark_palette.setColor(QtGui.QPalette.Button, dark_color)
        dark_palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.white)
        dark_palette.setColor(QtGui.QPalette.Disabled,
                              QtGui.QPalette.ButtonText, disabled_color)
        dark_palette.setColor(QtGui.QPalette.BrightText, QtCore.Qt.red)
        dark_palette.setColor(QtGui.QPalette.Link,
                              QtGui.QColor(42, 130, 218))

        dark_palette.setColor(QtGui.QPalette.Highlight,
                              QtGui.QColor(42, 130, 218))
        dark_palette.setColor(
            QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        dark_palette.setColor(QtGui.QPalette.Disabled,
                              QtGui.QPalette.HighlightedText, disabled_color)

        app.setPalette(dark_palette)
        app.setStyleSheet(
            "QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
