# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QLineEdit, QMainWindow, QSizePolicy, QTextBrowser,
    QToolButton, QWidget)

class Ui_winMain(object):
    def setupUi(self, winMain):
        if not winMain.objectName():
            winMain.setObjectName(u"winMain")
        winMain.resize(790, 470)
        font = QFont()
        font.setPointSize(12)
        winMain.setFont(font)
        winMain.setUnifiedTitleAndToolBarOnMac(False)
        self.actionPatch = QAction(winMain)
        self.actionPatch.setObjectName(u"actionPatch")
        self.actionPatch.setFont(font)
        self.actionLOTRO = QAction(winMain)
        self.actionLOTRO.setObjectName(u"actionLOTRO")
        self.actionDDO = QAction(winMain)
        self.actionDDO.setObjectName(u"actionDDO")
        self.centralwidget = QWidget(winMain)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblWorld = QLabel(self.centralwidget)
        self.lblWorld.setObjectName(u"lblWorld")
        self.lblWorld.setGeometry(QRect(400, 60, 120, 24))
        self.lblWorld.setFont(font)
        self.lblAccount = QLabel(self.centralwidget)
        self.lblAccount.setObjectName(u"lblAccount")
        self.lblAccount.setGeometry(QRect(400, 99, 120, 24))
        self.lblAccount.setFont(font)
        self.lblPassword = QLabel(self.centralwidget)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setGeometry(QRect(400, 135, 120, 24))
        self.lblPassword.setFont(font)
        self.cboWorld = QComboBox(self.centralwidget)
        self.cboWorld.setObjectName(u"cboWorld")
        self.cboWorld.setGeometry(QRect(525, 55, 201, 34))
        self.cboWorld.setFont(font)
        self.txtPassword = QLineEdit(self.centralwidget)
        self.txtPassword.setObjectName(u"txtPassword")
        self.txtPassword.setGeometry(QRect(525, 133, 260, 32))
        self.txtPassword.setFont(font)
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.txtPassword.setClearButtonEnabled(True)
        self.imgMain = QLabel(self.centralwidget)
        self.imgMain.setObjectName(u"imgMain")
        self.imgMain.setGeometry(QRect(50, 40, 300, 136))
        self.btnLogin = QToolButton(self.centralwidget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(410, 181, 101, 41))
        self.btnLogin.setFont(font)
        self.btnLogin.setPopupMode(QToolButton.MenuButtonPopup)
        self.chkSaveSettings = QCheckBox(self.centralwidget)
        self.chkSaveSettings.setObjectName(u"chkSaveSettings")
        self.chkSaveSettings.setGeometry(QRect(530, 172, 260, 29))
        self.chkSaveSettings.setFont(font)
        self.txtStatus = QTextBrowser(self.centralwidget)
        self.txtStatus.setObjectName(u"txtStatus")
        self.txtStatus.setGeometry(QRect(400, 240, 385, 221))
        self.txtStatus.setFont(font)
        self.txtStatus.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.txtStatus.setOpenLinks(False)
        self.btnAbout = QToolButton(self.centralwidget)
        self.btnAbout.setObjectName(u"btnAbout")
        self.btnAbout.setGeometry(QRect(670, 10, 31, 27))
        self.btnAbout.setFocusPolicy(Qt.ClickFocus)
        self.btnExit = QToolButton(self.centralwidget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setGeometry(QRect(750, 10, 31, 27))
        self.btnExit.setFocusPolicy(Qt.ClickFocus)
        self.txtFeed = QTextBrowser(self.centralwidget)
        self.txtFeed.setObjectName(u"txtFeed")
        self.txtFeed.setGeometry(QRect(10, 180, 381, 281))
        self.txtFeed.setOpenExternalLinks(True)
        self.txtFeed.setOpenLinks(True)
        self.btnMinimize = QToolButton(self.centralwidget)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setGeometry(QRect(710, 10, 31, 27))
        self.btnMinimize.setFocusPolicy(Qt.ClickFocus)
        self.btnSwitchGame = QToolButton(self.centralwidget)
        self.btnSwitchGame.setObjectName(u"btnSwitchGame")
        self.btnSwitchGame.setGeometry(QRect(733, 60, 51, 27))
        self.btnSwitchGame.setFocusPolicy(Qt.ClickFocus)
        self.btnSwitchGame.setIconSize(QSize(32, 32))
        self.btnSwitchGame.setPopupMode(QToolButton.MenuButtonPopup)
        self.btnSwitchGame.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.btnOptions = QToolButton(self.centralwidget)
        self.btnOptions.setObjectName(u"btnOptions")
        self.btnOptions.setGeometry(QRect(10, 10, 31, 27))
        self.btnOptions.setFocusPolicy(Qt.ClickFocus)
        self.btnOptions.setAutoRaise(False)
        self.chkSavePassword = QCheckBox(self.centralwidget)
        self.chkSavePassword.setObjectName(u"chkSavePassword")
        self.chkSavePassword.setGeometry(QRect(530, 201, 260, 29))
        self.chkSavePassword.setFont(font)
        self.btnAddonManager = QToolButton(self.centralwidget)
        self.btnAddonManager.setObjectName(u"btnAddonManager")
        self.btnAddonManager.setGeometry(QRect(50, 10, 31, 27))
        self.btnAddonManager.setFocusPolicy(Qt.ClickFocus)
        self.cboAccount = QComboBox(self.centralwidget)
        self.cboAccount.setObjectName(u"cboAccount")
        self.cboAccount.setGeometry(QRect(525, 95, 260, 32))
        self.cboAccount.setEditable(True)
        self.cboAccount.setInsertPolicy(QComboBox.NoInsert)
        winMain.setCentralWidget(self.centralwidget)
        self.lblWorld.raise_()
        self.lblAccount.raise_()
        self.lblPassword.raise_()
        self.cboWorld.raise_()
        self.txtPassword.raise_()
        self.imgMain.raise_()
        self.btnLogin.raise_()
        self.chkSaveSettings.raise_()
        self.txtStatus.raise_()
        self.btnAbout.raise_()
        self.btnExit.raise_()
        self.txtFeed.raise_()
        self.btnMinimize.raise_()
        self.btnSwitchGame.raise_()
        self.chkSavePassword.raise_()
        self.btnAddonManager.raise_()
        self.cboAccount.raise_()
        self.btnOptions.raise_()
        QWidget.setTabOrder(self.cboWorld, self.cboAccount)
        QWidget.setTabOrder(self.cboAccount, self.txtPassword)
        QWidget.setTabOrder(self.txtPassword, self.btnLogin)
        QWidget.setTabOrder(self.btnLogin, self.chkSaveSettings)
        QWidget.setTabOrder(self.chkSaveSettings, self.chkSavePassword)
        QWidget.setTabOrder(self.chkSavePassword, self.txtFeed)
        QWidget.setTabOrder(self.txtFeed, self.btnMinimize)
        QWidget.setTabOrder(self.btnMinimize, self.btnSwitchGame)
        QWidget.setTabOrder(self.btnSwitchGame, self.btnOptions)
        QWidget.setTabOrder(self.btnOptions, self.btnExit)
        QWidget.setTabOrder(self.btnExit, self.btnAddonManager)
        QWidget.setTabOrder(self.btnAddonManager, self.btnAbout)
        QWidget.setTabOrder(self.btnAbout, self.txtStatus)

        self.retranslateUi(winMain)

        QMetaObject.connectSlotsByName(winMain)
    # setupUi

    def retranslateUi(self, winMain):
#if QT_CONFIG(statustip)
        winMain.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        winMain.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        winMain.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        winMain.setWindowFilePath("")
        self.actionPatch.setText(QCoreApplication.translate("winMain", u"Patch", None))
        self.actionPatch.setIconText(QCoreApplication.translate("winMain", u"Patch", None))
#if QT_CONFIG(tooltip)
        self.actionPatch.setToolTip(QCoreApplication.translate("winMain", u"Patch", None))
#endif // QT_CONFIG(tooltip)
        self.actionLOTRO.setText(QCoreApplication.translate("winMain", u"Lord of the Rings Online", None))
        self.actionDDO.setText(QCoreApplication.translate("winMain", u"Dungeons and Dragons Online", None))
#if QT_CONFIG(tooltip)
        self.lblWorld.setToolTip(QCoreApplication.translate("winMain", u"<html><head/><body><p>Game server</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lblWorld.setText(QCoreApplication.translate("winMain", u"World", None))
        self.lblAccount.setText(QCoreApplication.translate("winMain", u"Account", None))
        self.lblPassword.setText(QCoreApplication.translate("winMain", u"Password", None))
#if QT_CONFIG(tooltip)
        self.cboWorld.setToolTip(QCoreApplication.translate("winMain", u"<html><head/><body><p>Select game server</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.imgMain.setText("")
#if QT_CONFIG(tooltip)
        self.btnLogin.setToolTip(QCoreApplication.translate("winMain", u"<html><head/><body><p>Start your adventure!</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnLogin.setText(QCoreApplication.translate("winMain", u"Play", None))
#if QT_CONFIG(tooltip)
        self.chkSaveSettings.setToolTip(QCoreApplication.translate("winMain", u"<html><head/><body><p>Save last used world and account name</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chkSaveSettings.setText(QCoreApplication.translate("winMain", u"Remember these settings", None))
#if QT_CONFIG(tooltip)
        self.btnAbout.setToolTip(QCoreApplication.translate("winMain", u"<html><head/><body><p>About</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnAbout.setText(QCoreApplication.translate("winMain", u"?", None))
#if QT_CONFIG(tooltip)
        self.btnExit.setToolTip(QCoreApplication.translate("winMain", u"<html><head/><body><p>Exit</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnExit.setText(QCoreApplication.translate("winMain", u"X", None))
#if QT_CONFIG(tooltip)
        self.btnMinimize.setToolTip(QCoreApplication.translate("winMain", u"<html><head/><body><p>Minimize</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnMinimize.setText(QCoreApplication.translate("winMain", u"-", None))
#if QT_CONFIG(tooltip)
        self.btnSwitchGame.setToolTip(QCoreApplication.translate("winMain", u"<html><head/><body><p>Switch game</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnSwitchGame.setText("")
#if QT_CONFIG(tooltip)
        self.btnOptions.setToolTip(QCoreApplication.translate("winMain", u"<html><head/><body><p>Settings</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnOptions.setText("")
#if QT_CONFIG(tooltip)
        self.chkSavePassword.setToolTip(QCoreApplication.translate("winMain", u"<html><head/><body><p>Save last used password</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.chkSavePassword.setText(QCoreApplication.translate("winMain", u"Remember password", None))
#if QT_CONFIG(tooltip)
        self.btnAddonManager.setToolTip(QCoreApplication.translate("winMain", u"<html><head/><body><p>Addon manager</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btnAddonManager.setText("")
    # retranslateUi

