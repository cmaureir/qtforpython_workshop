# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'themewidget.ui',
# licensing of 'themewidget.ui' applies.
#
# Created: Fri Jul 13 16:59:48 2018
#      by: pyside2-uic  running on PySide2 5.11.1a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ThemeWidgetForm(object):
    def setupUi(self, ThemeWidgetForm):
        ThemeWidgetForm.setObjectName("ThemeWidgetForm")
        ThemeWidgetForm.resize(900, 600)
        self.gridLayout = QtWidgets.QGridLayout(ThemeWidgetForm)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.themeLabel = QtWidgets.QLabel(ThemeWidgetForm)
        self.themeLabel.setObjectName("themeLabel")
        self.horizontalLayout.addWidget(self.themeLabel)
        self.themeComboBox = QtWidgets.QComboBox(ThemeWidgetForm)
        self.themeComboBox.setObjectName("themeComboBox")
        self.horizontalLayout.addWidget(self.themeComboBox)
        self.animatedLabel = QtWidgets.QLabel(ThemeWidgetForm)
        self.animatedLabel.setObjectName("animatedLabel")
        self.horizontalLayout.addWidget(self.animatedLabel)
        self.animatedComboBox = QtWidgets.QComboBox(ThemeWidgetForm)
        self.animatedComboBox.setObjectName("animatedComboBox")
        self.horizontalLayout.addWidget(self.animatedComboBox)
        self.legendLabel = QtWidgets.QLabel(ThemeWidgetForm)
        self.legendLabel.setObjectName("legendLabel")
        self.horizontalLayout.addWidget(self.legendLabel)
        self.legendComboBox = QtWidgets.QComboBox(ThemeWidgetForm)
        self.legendComboBox.setObjectName("legendComboBox")
        self.horizontalLayout.addWidget(self.legendComboBox)
        self.antialiasCheckBox = QtWidgets.QCheckBox(ThemeWidgetForm)
        self.antialiasCheckBox.setChecked(False)
        self.antialiasCheckBox.setObjectName("antialiasCheckBox")
        self.horizontalLayout.addWidget(self.antialiasCheckBox)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)

        self.retranslateUi(ThemeWidgetForm)
        QtCore.QObject.connect(
            self.themeComboBox,
            QtCore.SIGNAL("currentIndexChanged(int)"),
            ThemeWidgetForm.updateUI,
        )
        QtCore.QObject.connect(
            self.antialiasCheckBox,
            QtCore.SIGNAL("toggled(bool)"),
            ThemeWidgetForm.updateUI,
        )
        QtCore.QObject.connect(
            self.legendComboBox,
            QtCore.SIGNAL("currentIndexChanged(int)"),
            ThemeWidgetForm.updateUI,
        )
        QtCore.QObject.connect(
            self.animatedComboBox,
            QtCore.SIGNAL("currentIndexChanged(int)"),
            ThemeWidgetForm.updateUI,
        )
        QtCore.QMetaObject.connectSlotsByName(ThemeWidgetForm)

    def retranslateUi(self, ThemeWidgetForm):
        self.themeLabel.setText(
            QtWidgets.QApplication.translate("ThemeWidgetForm", "Theme:", None, -1)
        )
        self.animatedLabel.setText(
            QtWidgets.QApplication.translate("ThemeWidgetForm", "Animation:", None, -1)
        )
        self.legendLabel.setText(
            QtWidgets.QApplication.translate("ThemeWidgetForm", "Legend:", None, -1)
        )
        self.antialiasCheckBox.setText(
            QtWidgets.QApplication.translate(
                "ThemeWidgetForm", "Anti-aliasing", None, -1
            )
        )
