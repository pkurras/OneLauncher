# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_dlgSettings(object):
    def setupUi(self, dlgSettings):
        if not dlgSettings.objectName():
            dlgSettings.setObjectName(u"dlgSettings")
        dlgSettings.setWindowModality(Qt.ApplicationModal)
        dlgSettings.resize(469, 366)
        font = QFont()
        font.setPointSize(12)
        dlgSettings.setFont(font)
        dlgSettings.setModal(True)
        self.showAdvancedSettingsCheckbox = QCheckBox(dlgSettings)
        self.showAdvancedSettingsCheckbox.setObjectName(u"showAdvancedSettingsCheckbox")
        self.showAdvancedSettingsCheckbox.setGeometry(QRect(20, 332, 211, 28))
        self.showAdvancedSettingsCheckbox.setChecked(False)
        self.tabWidget = QTabWidget(dlgSettings)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 471, 371))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gameNameLabel = QLabel(self.tab)
        self.gameNameLabel.setObjectName(u"gameNameLabel")
        self.gameNameLabel.setGeometry(QRect(10, 17, 131, 23))
        self.gameNameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gameNameLineEdit = QLineEdit(self.tab)
        self.gameNameLineEdit.setObjectName(u"gameNameLineEdit")
        self.gameNameLineEdit.setGeometry(QRect(150, 12, 300, 31))
        self.gameNameLineEdit.setClearButtonEnabled(True)
        self.gameDescriptionLabel = QLabel(self.tab)
        self.gameDescriptionLabel.setObjectName(u"gameDescriptionLabel")
        self.gameDescriptionLabel.setGeometry(QRect(10, 57, 131, 23))
        self.gameDescriptionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gameDescriptionLineEdit = QLineEdit(self.tab)
        self.gameDescriptionLineEdit.setObjectName(u"gameDescriptionLineEdit")
        self.gameDescriptionLineEdit.setGeometry(QRect(150, 52, 300, 31))
        self.gameDescriptionLineEdit.setClearButtonEnabled(True)
        self.gameNewsfeedLabel = QLabel(self.tab)
        self.gameNewsfeedLabel.setObjectName(u"gameNewsfeedLabel")
        self.gameNewsfeedLabel.setGeometry(QRect(10, 262, 131, 23))
        self.gameNewsfeedLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gameNewsfeedLineEdit = QLineEdit(self.tab)
        self.gameNewsfeedLineEdit.setObjectName(u"gameNewsfeedLineEdit")
        self.gameNewsfeedLineEdit.setGeometry(QRect(150, 257, 300, 31))
        self.gameNewsfeedLineEdit.setClearButtonEnabled(False)
        self.defaultGameLauncherButton = QPushButton(self.tab)
        self.defaultGameLauncherButton.setObjectName(u"defaultGameLauncherButton")
        self.defaultGameLauncherButton.setGeometry(QRect(160, 110, 281, 25))
        self.tabWidget.addTab(self.tab, "")
        self.tabGame = QWidget()
        self.tabGame.setObjectName(u"tabGame")
        self.clientTypeComboBox = QComboBox(self.tabGame)
        self.clientTypeComboBox.setObjectName(u"clientTypeComboBox")
        self.clientTypeComboBox.setGeometry(QRect(151, 136, 300, 33))
        self.patchClientLabel = QLabel(self.tabGame)
        self.patchClientLabel.setObjectName(u"patchClientLabel")
        self.patchClientLabel.setGeometry(QRect(12, 261, 131, 23))
        self.patchClientLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.patchClientLineEdit = QLineEdit(self.tabGame)
        self.patchClientLineEdit.setObjectName(u"patchClientLineEdit")
        self.patchClientLineEdit.setGeometry(QRect(150, 257, 300, 31))
        self.gameDirButton = QToolButton(self.tabGame)
        self.gameDirButton.setObjectName(u"gameDirButton")
        self.gameDirButton.setGeometry(QRect(415, 56, 36, 30))
        self.highResLabel = QLabel(self.tabGame)
        self.highResLabel.setObjectName(u"highResLabel")
        self.highResLabel.setGeometry(QRect(13, 97, 131, 23))
        self.highResLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.clientLabel = QLabel(self.tabGame)
        self.clientLabel.setObjectName(u"clientLabel")
        self.clientLabel.setGeometry(QRect(13, 141, 131, 23))
        self.clientLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gameDirLabel = QLabel(self.tabGame)
        self.gameDirLabel.setObjectName(u"gameDirLabel")
        self.gameDirLabel.setGeometry(QRect(13, 60, 131, 23))
        self.gameDirLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gameDirLineEdit = QLineEdit(self.tabGame)
        self.gameDirLineEdit.setObjectName(u"gameDirLineEdit")
        self.gameDirLineEdit.setGeometry(QRect(151, 55, 260, 31))
        self.highResCheckBox = QCheckBox(self.tabGame)
        self.highResCheckBox.setObjectName(u"highResCheckBox")
        self.highResCheckBox.setGeometry(QRect(155, 95, 21, 31))
        self.gameLanguageLabel = QLabel(self.tabGame)
        self.gameLanguageLabel.setObjectName(u"gameLanguageLabel")
        self.gameLanguageLabel.setGeometry(QRect(12, 17, 131, 23))
        self.gameLanguageLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gameLanguageComboBox = QComboBox(self.tabGame)
        self.gameLanguageComboBox.setObjectName(u"gameLanguageComboBox")
        self.gameLanguageComboBox.setGeometry(QRect(151, 12, 300, 33))
        self.tabWidget.addTab(self.tabGame, "")
        self.tabWine = QWidget()
        self.tabWine.setObjectName(u"tabWine")
        self.wineFormGroupBox = QGroupBox(self.tabWine)
        self.wineFormGroupBox.setObjectName(u"wineFormGroupBox")
        self.wineFormGroupBox.setGeometry(QRect(10, 18, 451, 151))
        self.wineFormGroupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.wineFormGroupBox.setFlat(True)
        self.wineFormGroupBox.setCheckable(True)
        self.wineFormGroupBox.setChecked(True)
        self.wineGroupBox = QFormLayout(self.wineFormGroupBox)
        self.wineGroupBox.setObjectName(u"wineGroupBox")
        self.wineGroupBox.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.wineGroupBox.setContentsMargins(15, 15, 15, 15)
        self.prefixLabel = QLabel(self.wineFormGroupBox)
        self.prefixLabel.setObjectName(u"prefixLabel")

        self.wineGroupBox.setWidget(0, QFormLayout.LabelRole, self.prefixLabel)

        self.prefixLineEdit = QLineEdit(self.wineFormGroupBox)
        self.prefixLineEdit.setObjectName(u"prefixLineEdit")
        self.prefixLineEdit.setDragEnabled(True)

        self.wineGroupBox.setWidget(0, QFormLayout.FieldRole, self.prefixLineEdit)

        self.wineExecutableLabel = QLabel(self.wineFormGroupBox)
        self.wineExecutableLabel.setObjectName(u"wineExecutableLabel")

        self.wineGroupBox.setWidget(1, QFormLayout.LabelRole, self.wineExecutableLabel)

        self.wineExecutableLineEdit = QLineEdit(self.wineFormGroupBox)
        self.wineExecutableLineEdit.setObjectName(u"wineExecutableLineEdit")
        self.wineExecutableLineEdit.setDragEnabled(True)

        self.wineGroupBox.setWidget(1, QFormLayout.FieldRole, self.wineExecutableLineEdit)

        self.wineAdvancedFrame = QFrame(self.tabWine)
        self.wineAdvancedFrame.setObjectName(u"wineAdvancedFrame")
        self.wineAdvancedFrame.setGeometry(QRect(-1, 159, 461, 141))
        self.wineAdvancedFrame.setFrameShape(QFrame.NoFrame)
        self.wineAdvancedFrame.setFrameShadow(QFrame.Plain)
        self.formLayoutWidget_2 = QWidget(self.wineAdvancedFrame)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(0, 10, 461, 131))
        self.wineAdvancedForm = QFormLayout(self.formLayoutWidget_2)
        self.wineAdvancedForm.setObjectName(u"wineAdvancedForm")
        self.wineAdvancedForm.setContentsMargins(15, 15, 15, 15)
        self.wineDebugLabel = QLabel(self.formLayoutWidget_2)
        self.wineDebugLabel.setObjectName(u"wineDebugLabel")

        self.wineAdvancedForm.setWidget(0, QFormLayout.LabelRole, self.wineDebugLabel)

        self.wineDebugLineEdit = QLineEdit(self.formLayoutWidget_2)
        self.wineDebugLineEdit.setObjectName(u"wineDebugLineEdit")

        self.wineAdvancedForm.setWidget(0, QFormLayout.FieldRole, self.wineDebugLineEdit)

        self.tabWidget.addTab(self.tabWine, "")
        self.wineAdvancedFrame.raise_()
        self.wineFormGroupBox.raise_()
        self.tabProgram = QWidget()
        self.tabProgram.setObjectName(u"tabProgram")
        self.setupWizardButton = QPushButton(self.tabProgram)
        self.setupWizardButton.setObjectName(u"setupWizardButton")
        self.setupWizardButton.setGeometry(QRect(181, 160, 261, 25))
        self.defaultLanguageComboBox = QComboBox(self.tabProgram)
        self.defaultLanguageComboBox.setObjectName(u"defaultLanguageComboBox")
        self.defaultLanguageComboBox.setGeometry(QRect(170, 12, 281, 33))
        self.defaultLanguageLabel = QLabel(self.tabProgram)
        self.defaultLanguageLabel.setObjectName(u"defaultLanguageLabel")
        self.defaultLanguageLabel.setGeometry(QRect(12, 17, 151, 23))
        self.defaultLanguageLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.defaultLanguageForUICheckBox = QCheckBox(self.tabProgram)
        self.defaultLanguageForUICheckBox.setObjectName(u"defaultLanguageForUICheckBox")
        self.defaultLanguageForUICheckBox.setGeometry(QRect(178, 52, 21, 51))
        self.defaultLanguageForUILabel = QLabel(self.tabProgram)
        self.defaultLanguageForUILabel.setObjectName(u"defaultLanguageForUILabel")
        self.defaultLanguageForUILabel.setGeometry(QRect(-6, 52, 201, 51))
        self.defaultLanguageForUILabel.setAlignment(Qt.AlignCenter)
        self.defaultLanguageForUILabel.setWordWrap(True)
        self.gamesSortingModeLabel = QLabel(self.tabProgram)
        self.gamesSortingModeLabel.setObjectName(u"gamesSortingModeLabel")
        self.gamesSortingModeLabel.setGeometry(QRect(12, 113, 151, 23))
        self.gamesSortingModeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.gamesSortingModeComboBox = QComboBox(self.tabProgram)
        self.gamesSortingModeComboBox.setObjectName(u"gamesSortingModeComboBox")
        self.gamesSortingModeComboBox.setGeometry(QRect(170, 108, 281, 33))
        self.tabWidget.addTab(self.tabProgram, "")
        self.setupWizardButton.raise_()
        self.defaultLanguageComboBox.raise_()
        self.defaultLanguageLabel.raise_()
        self.defaultLanguageForUILabel.raise_()
        self.defaultLanguageForUICheckBox.raise_()
        self.gamesSortingModeLabel.raise_()
        self.gamesSortingModeComboBox.raise_()
        self.settingsButtonBox = QDialogButtonBox(dlgSettings)
        self.settingsButtonBox.setObjectName(u"settingsButtonBox")
        self.settingsButtonBox.setGeometry(QRect(0, 332, 450, 32))
        self.settingsButtonBox.setOrientation(Qt.Horizontal)
        self.settingsButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)
        self.tabWidget.raise_()
        self.settingsButtonBox.raise_()
        self.showAdvancedSettingsCheckbox.raise_()

        self.retranslateUi(dlgSettings)
        self.settingsButtonBox.rejected.connect(dlgSettings.reject)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dlgSettings)
    # setupUi

    def retranslateUi(self, dlgSettings):
        dlgSettings.setWindowTitle(QCoreApplication.translate("dlgSettings", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.showAdvancedSettingsCheckbox.setToolTip(QCoreApplication.translate("dlgSettings", u"<html><head/><body><p>Enable advanced options</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.showAdvancedSettingsCheckbox.setText(QCoreApplication.translate("dlgSettings", u"Advanced Options", None))
#if QT_CONFIG(tooltip)
        self.gameNameLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.gameNameLabel.setText(QCoreApplication.translate("dlgSettings", u"Name", None))
#if QT_CONFIG(tooltip)
        self.gameNameLineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.gameDescriptionLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.gameDescriptionLabel.setText(QCoreApplication.translate("dlgSettings", u"Description", None))
#if QT_CONFIG(tooltip)
        self.gameDescriptionLineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.gameNewsfeedLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.gameNewsfeedLabel.setText(QCoreApplication.translate("dlgSettings", u"RSS Newsfeed", None))
#if QT_CONFIG(tooltip)
        self.gameNewsfeedLineEdit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.defaultGameLauncherButton.setText(QCoreApplication.translate("dlgSettings", u"Run Default Game Launcher", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("dlgSettings", u"Game Info", None))
#if QT_CONFIG(tooltip)
        self.clientTypeComboBox.setToolTip(QCoreApplication.translate("dlgSettings", u"Game client version to use. 64-bit is the most modern. It does work with WINE", None))
#endif // QT_CONFIG(tooltip)
        self.patchClientLabel.setText(QCoreApplication.translate("dlgSettings", u"Patch Client DLL", None))
#if QT_CONFIG(tooltip)
        self.gameDirButton.setToolTip(QCoreApplication.translate("dlgSettings", u"Select game directory from file system", None))
#endif // QT_CONFIG(tooltip)
        self.gameDirButton.setText(QCoreApplication.translate("dlgSettings", u"...", None))
#if QT_CONFIG(tooltip)
        self.highResLabel.setToolTip(QCoreApplication.translate("dlgSettings", u"Enable high resolution game files. You may need to patch the game after enabling this", None))
#endif // QT_CONFIG(tooltip)
        self.highResLabel.setText(QCoreApplication.translate("dlgSettings", u"Hi-Res Graphics", None))
#if QT_CONFIG(tooltip)
        self.clientLabel.setToolTip(QCoreApplication.translate("dlgSettings", u"Game client version to use. 64-bit is the most modern. It does work with WINE", None))
#endif // QT_CONFIG(tooltip)
        self.clientLabel.setText(QCoreApplication.translate("dlgSettings", u"Game Client", None))
#if QT_CONFIG(tooltip)
        self.gameDirLabel.setToolTip(QCoreApplication.translate("dlgSettings", u"Game install directory. There should be a file called patchclient.dll here", None))
#endif // QT_CONFIG(tooltip)
        self.gameDirLabel.setText(QCoreApplication.translate("dlgSettings", u"Game Directory", None))
#if QT_CONFIG(tooltip)
        self.gameDirLineEdit.setToolTip(QCoreApplication.translate("dlgSettings", u"Game install directory. There should be a file called patchclient.dll here", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.highResCheckBox.setToolTip(QCoreApplication.translate("dlgSettings", u"Enable high resolution game files. You may need to patch the game after enabling this", None))
#endif // QT_CONFIG(tooltip)
        self.highResCheckBox.setText("")
#if QT_CONFIG(tooltip)
        self.gameLanguageLabel.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.gameLanguageLabel.setText(QCoreApplication.translate("dlgSettings", u"Language", None))
#if QT_CONFIG(tooltip)
        self.gameLanguageComboBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGame), QCoreApplication.translate("dlgSettings", u"Game", None))
#if QT_CONFIG(tooltip)
        self.wineFormGroupBox.setToolTip(QCoreApplication.translate("dlgSettings", u"Enable manual WINE configuration. Otherwise, WINE and DXVK all get downloaded and managed automatically", None))
#endif // QT_CONFIG(tooltip)
        self.wineFormGroupBox.setTitle(QCoreApplication.translate("dlgSettings", u"Manually Configure", None))
#if QT_CONFIG(tooltip)
        self.prefixLabel.setToolTip(QCoreApplication.translate("dlgSettings", u"Path to WINE prefix", None))
#endif // QT_CONFIG(tooltip)
        self.prefixLabel.setText(QCoreApplication.translate("dlgSettings", u"Prefix", None))
#if QT_CONFIG(tooltip)
        self.prefixLineEdit.setToolTip(QCoreApplication.translate("dlgSettings", u"Path to WINE prefix", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.wineExecutableLabel.setToolTip(QCoreApplication.translate("dlgSettings", u"Path to WINE executable", None))
#endif // QT_CONFIG(tooltip)
        self.wineExecutableLabel.setText(QCoreApplication.translate("dlgSettings", u"Executable", None))
#if QT_CONFIG(tooltip)
        self.wineExecutableLineEdit.setToolTip(QCoreApplication.translate("dlgSettings", u"Path to WINE executable", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.wineDebugLabel.setToolTip(QCoreApplication.translate("dlgSettings", u"Value for WINEDEBUG environment variable", None))
#endif // QT_CONFIG(tooltip)
        self.wineDebugLabel.setText(QCoreApplication.translate("dlgSettings", u"WINEDEBUG", None))
#if QT_CONFIG(tooltip)
        self.wineDebugLineEdit.setToolTip(QCoreApplication.translate("dlgSettings", u"Value for WINEDEBUG environment variable", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWine), QCoreApplication.translate("dlgSettings", u"Wine", None))
        self.setupWizardButton.setText(QCoreApplication.translate("dlgSettings", u"Run Setup Wizard", None))
#if QT_CONFIG(tooltip)
        self.defaultLanguageComboBox.setToolTip(QCoreApplication.translate("dlgSettings", u"Default language to use for games", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.defaultLanguageLabel.setToolTip(QCoreApplication.translate("dlgSettings", u"Default language to use for games", None))
#endif // QT_CONFIG(tooltip)
        self.defaultLanguageLabel.setText(QCoreApplication.translate("dlgSettings", u"Default Language", None))
#if QT_CONFIG(tooltip)
        self.defaultLanguageForUICheckBox.setToolTip(QCoreApplication.translate("dlgSettings", u"Use the default language for OneLauncher even when the current game is set to a different language", None))
#endif // QT_CONFIG(tooltip)
        self.defaultLanguageForUICheckBox.setText("")
#if QT_CONFIG(tooltip)
        self.defaultLanguageForUILabel.setToolTip(QCoreApplication.translate("dlgSettings", u"Use the default language for OneLauncher even when the current game is set to a different language", None))
#endif // QT_CONFIG(tooltip)
        self.defaultLanguageForUILabel.setText(QCoreApplication.translate("dlgSettings", u"Always Use Default Language For UI", None))
#if QT_CONFIG(tooltip)
        self.gamesSortingModeLabel.setToolTip(QCoreApplication.translate("dlgSettings", u"Default language to use for games", None))
#endif // QT_CONFIG(tooltip)
        self.gamesSortingModeLabel.setText(QCoreApplication.translate("dlgSettings", u"Games Sorting Mode", None))
#if QT_CONFIG(tooltip)
        self.gamesSortingModeComboBox.setToolTip(QCoreApplication.translate("dlgSettings", u"Default language to use for games", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabProgram), QCoreApplication.translate("dlgSettings", u"OneLauncher", None))
    # retranslateUi

