# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'continuous_data_form.ui'
#
# Created: Wed Mar 27 14:45:38 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ContinuousDataForm(object):
    def setupUi(self, ContinuousDataForm):
        ContinuousDataForm.setObjectName(_fromUtf8("ContinuousDataForm"))
        ContinuousDataForm.resize(570, 582)
        ContinuousDataForm.setMinimumSize(QtCore.QSize(570, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        ContinuousDataForm.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/meta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ContinuousDataForm.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(ContinuousDataForm)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.simple_table = QtGui.QTableWidget(ContinuousDataForm)
        self.simple_table.setMinimumSize(QtCore.QSize(550, 80))
        self.simple_table.setMaximumSize(QtCore.QSize(550, 80))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.simple_table.setFont(font)
        self.simple_table.setFrameShape(QtGui.QFrame.NoFrame)
        self.simple_table.setFrameShadow(QtGui.QFrame.Plain)
        self.simple_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.simple_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.simple_table.setAlternatingRowColors(True)
        self.simple_table.setGridStyle(QtCore.Qt.DashLine)
        self.simple_table.setRowCount(2)
        self.simple_table.setColumnCount(8)
        self.simple_table.setObjectName(_fromUtf8("simple_table"))
        item = QtGui.QTableWidgetItem()
        self.simple_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.simple_table.setHorizontalHeaderItem(7, item)
        self.verticalLayout_2.addWidget(self.simple_table)
        self.grp_box_pre_post = QtGui.QGroupBox(ContinuousDataForm)
        self.grp_box_pre_post.setObjectName(_fromUtf8("grp_box_pre_post"))
        self.verticalLayout = QtGui.QVBoxLayout(self.grp_box_pre_post)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.g1_pre_post_table = QtGui.QTableWidget(self.grp_box_pre_post)
        self.g1_pre_post_table.setMinimumSize(QtCore.QSize(490, 81))
        self.g1_pre_post_table.setMaximumSize(QtCore.QSize(490, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.g1_pre_post_table.setFont(font)
        self.g1_pre_post_table.setFrameShape(QtGui.QFrame.NoFrame)
        self.g1_pre_post_table.setFrameShadow(QtGui.QFrame.Plain)
        self.g1_pre_post_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g1_pre_post_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g1_pre_post_table.setAlternatingRowColors(True)
        self.g1_pre_post_table.setShowGrid(True)
        self.g1_pre_post_table.setGridStyle(QtCore.Qt.DashLine)
        self.g1_pre_post_table.setRowCount(2)
        self.g1_pre_post_table.setColumnCount(7)
        self.g1_pre_post_table.setObjectName(_fromUtf8("g1_pre_post_table"))
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.g1_pre_post_table.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.g1_pre_post_table)
        self.grp_1_lbl = QtGui.QLabel(self.grp_box_pre_post)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.grp_1_lbl.setFont(font)
        self.grp_1_lbl.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grp_1_lbl.setObjectName(_fromUtf8("grp_1_lbl"))
        self.verticalLayout.addWidget(self.grp_1_lbl)
        self.g2_pre_post_table = QtGui.QTableWidget(self.grp_box_pre_post)
        self.g2_pre_post_table.setMinimumSize(QtCore.QSize(490, 81))
        self.g2_pre_post_table.setMaximumSize(QtCore.QSize(490, 81))
        self.g2_pre_post_table.setFrameShape(QtGui.QFrame.NoFrame)
        self.g2_pre_post_table.setFrameShadow(QtGui.QFrame.Plain)
        self.g2_pre_post_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g2_pre_post_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.g2_pre_post_table.setAlternatingRowColors(True)
        self.g2_pre_post_table.setGridStyle(QtCore.Qt.DashLine)
        self.g2_pre_post_table.setRowCount(2)
        self.g2_pre_post_table.setColumnCount(7)
        self.g2_pre_post_table.setObjectName(_fromUtf8("g2_pre_post_table"))
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.g2_pre_post_table.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.g2_pre_post_table)
        self.grp_2_lbl = QtGui.QLabel(self.grp_box_pre_post)
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.grp_2_lbl.setFont(font)
        self.grp_2_lbl.setObjectName(_fromUtf8("grp_2_lbl"))
        self.verticalLayout.addWidget(self.grp_2_lbl)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.clear_Btn = QtGui.QPushButton(self.grp_box_pre_post)
        self.clear_Btn.setObjectName(_fromUtf8("clear_Btn"))
        self.horizontalLayout_3.addWidget(self.clear_Btn)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtGui.QLabel(self.grp_box_pre_post)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        self.correlation_pre_post = QtGui.QLineEdit(self.grp_box_pre_post)
        self.correlation_pre_post.setMinimumSize(QtCore.QSize(40, 0))
        self.correlation_pre_post.setMaximumSize(QtCore.QSize(40, 16777215))
        self.correlation_pre_post.setObjectName(_fromUtf8("correlation_pre_post"))
        self.horizontalLayout_3.addWidget(self.correlation_pre_post)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.grp_box_pre_post)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_13 = QtGui.QLabel(ContinuousDataForm)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_2.addWidget(self.label_13)
        self.effect_cbo_box = QtGui.QComboBox(ContinuousDataForm)
        self.effect_cbo_box.setMinimumSize(QtCore.QSize(76, 20))
        self.effect_cbo_box.setMaximumSize(QtCore.QSize(76, 20))
        self.effect_cbo_box.setObjectName(_fromUtf8("effect_cbo_box"))
        self.horizontalLayout_2.addWidget(self.effect_cbo_box)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 2, 1)
        self.ci_label = QtGui.QLabel(ContinuousDataForm)
        self.ci_label.setObjectName(_fromUtf8("ci_label"))
        self.gridLayout.addWidget(self.ci_label, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 3, 2, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_14 = QtGui.QLabel(ContinuousDataForm)
        self.label_14.setMinimumSize(QtCore.QSize(0, 20))
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_4.addWidget(self.label_14)
        self.effect_txt_box = QtGui.QLineEdit(ContinuousDataForm)
        self.effect_txt_box.setMinimumSize(QtCore.QSize(50, 20))
        self.effect_txt_box.setMaximumSize(QtCore.QSize(50, 20))
        self.effect_txt_box.setObjectName(_fromUtf8("effect_txt_box"))
        self.horizontalLayout_4.addWidget(self.effect_txt_box)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_15 = QtGui.QLabel(ContinuousDataForm)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_5.addWidget(self.label_15)
        self.low_txt_box = QtGui.QLineEdit(ContinuousDataForm)
        self.low_txt_box.setMinimumSize(QtCore.QSize(50, 20))
        self.low_txt_box.setMaximumSize(QtCore.QSize(50, 20))
        self.low_txt_box.setObjectName(_fromUtf8("low_txt_box"))
        self.horizontalLayout_5.addWidget(self.low_txt_box)
        self.label_2 = QtGui.QLabel(ContinuousDataForm)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_5.addWidget(self.label_2)
        self.high_txt_box = QtGui.QLineEdit(ContinuousDataForm)
        self.high_txt_box.setMinimumSize(QtCore.QSize(50, 20))
        self.high_txt_box.setMaximumSize(QtCore.QSize(50, 20))
        self.high_txt_box.setObjectName(_fromUtf8("high_txt_box"))
        self.horizontalLayout_5.addWidget(self.high_txt_box)
        self.label_16 = QtGui.QLabel(ContinuousDataForm)
        self.label_16.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_5.addWidget(self.label_16)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(ContinuousDataForm)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.CI_spinbox = QtGui.QDoubleSpinBox(ContinuousDataForm)
        self.CI_spinbox.setDecimals(1)
        self.CI_spinbox.setMinimum(40.0)
        self.CI_spinbox.setMaximum(100.0)
        self.CI_spinbox.setSingleStep(0.1)
        self.CI_spinbox.setProperty("value", 95.0)
        self.CI_spinbox.setObjectName(_fromUtf8("CI_spinbox"))
        self.horizontalLayout.addWidget(self.CI_spinbox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(ContinuousDataForm)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(ContinuousDataForm)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ContinuousDataForm.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ContinuousDataForm.reject)
        QtCore.QMetaObject.connectSlotsByName(ContinuousDataForm)

    def retranslateUi(self, ContinuousDataForm):
        ContinuousDataForm.setWindowTitle(_translate("ContinuousDataForm", "Continuous Data", None))
        item = self.simple_table.verticalHeaderItem(0)
        item.setText(_translate("ContinuousDataForm", "group 1", None))
        item = self.simple_table.verticalHeaderItem(1)
        item.setText(_translate("ContinuousDataForm", "group 2", None))
        item = self.simple_table.horizontalHeaderItem(0)
        item.setText(_translate("ContinuousDataForm", "n", None))
        item = self.simple_table.horizontalHeaderItem(1)
        item.setText(_translate("ContinuousDataForm", "mean", None))
        item = self.simple_table.horizontalHeaderItem(2)
        item.setText(_translate("ContinuousDataForm", "sd", None))
        item = self.simple_table.horizontalHeaderItem(3)
        item.setText(_translate("ContinuousDataForm", "se", None))
        item = self.simple_table.horizontalHeaderItem(4)
        item.setText(_translate("ContinuousDataForm", "var", None))
        item = self.simple_table.horizontalHeaderItem(5)
        item.setText(_translate("ContinuousDataForm", "pval", None))
        item = self.simple_table.horizontalHeaderItem(6)
        item.setText(_translate("ContinuousDataForm", "low", None))
        item = self.simple_table.horizontalHeaderItem(7)
        item.setText(_translate("ContinuousDataForm", "high", None))
        self.grp_box_pre_post.setTitle(_translate("ContinuousDataForm", "pre / post", None))
        item = self.g1_pre_post_table.verticalHeaderItem(0)
        item.setText(_translate("ContinuousDataForm", "pre", None))
        item = self.g1_pre_post_table.verticalHeaderItem(1)
        item.setText(_translate("ContinuousDataForm", "post", None))
        item = self.g1_pre_post_table.horizontalHeaderItem(0)
        item.setText(_translate("ContinuousDataForm", "n", None))
        item = self.g1_pre_post_table.horizontalHeaderItem(1)
        item.setText(_translate("ContinuousDataForm", "mean", None))
        item = self.g1_pre_post_table.horizontalHeaderItem(2)
        item.setText(_translate("ContinuousDataForm", "sd", None))
        item = self.g1_pre_post_table.horizontalHeaderItem(3)
        item.setText(_translate("ContinuousDataForm", "se", None))
        item = self.g1_pre_post_table.horizontalHeaderItem(4)
        item.setText(_translate("ContinuousDataForm", "var", None))
        item = self.g1_pre_post_table.horizontalHeaderItem(5)
        item.setText(_translate("ContinuousDataForm", "low", None))
        item = self.g1_pre_post_table.horizontalHeaderItem(6)
        item.setText(_translate("ContinuousDataForm", "high", None))
        self.grp_1_lbl.setText(_translate("ContinuousDataForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:8pt; font-weight:600; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">group 1</span></p></body></html>", None))
        item = self.g2_pre_post_table.verticalHeaderItem(0)
        item.setText(_translate("ContinuousDataForm", "pre", None))
        item = self.g2_pre_post_table.verticalHeaderItem(1)
        item.setText(_translate("ContinuousDataForm", "post", None))
        item = self.g2_pre_post_table.horizontalHeaderItem(0)
        item.setText(_translate("ContinuousDataForm", "n", None))
        item = self.g2_pre_post_table.horizontalHeaderItem(1)
        item.setText(_translate("ContinuousDataForm", "mean", None))
        item = self.g2_pre_post_table.horizontalHeaderItem(2)
        item.setText(_translate("ContinuousDataForm", "sd", None))
        item = self.g2_pre_post_table.horizontalHeaderItem(3)
        item.setText(_translate("ContinuousDataForm", "se", None))
        item = self.g2_pre_post_table.horizontalHeaderItem(4)
        item.setText(_translate("ContinuousDataForm", "var", None))
        item = self.g2_pre_post_table.horizontalHeaderItem(5)
        item.setText(_translate("ContinuousDataForm", "low", None))
        item = self.g2_pre_post_table.horizontalHeaderItem(6)
        item.setText(_translate("ContinuousDataForm", "high", None))
        self.grp_2_lbl.setText(_translate("ContinuousDataForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Verdana\'; font-size:8pt; font-weight:600; font-style:italic;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">group 2</span></p></body></html>", None))
        self.clear_Btn.setText(_translate("ContinuousDataForm", "Clear Form", None))
        self.label.setText(_translate("ContinuousDataForm", "correlation:", None))
        self.correlation_pre_post.setText(_translate("ContinuousDataForm", "0.0", None))
        self.label_13.setText(_translate("ContinuousDataForm", "effect", None))
        self.ci_label.setText(_translate("ContinuousDataForm", "(X% confidence interval)", None))
        self.label_14.setText(_translate("ContinuousDataForm", "est.", None))
        self.label_15.setText(_translate("ContinuousDataForm", "[", None))
        self.label_2.setText(_translate("ContinuousDataForm", ",", None))
        self.label_16.setText(_translate("ContinuousDataForm", "]", None))
        self.label_3.setText(_translate("ContinuousDataForm", "Confidence Level:", None))
        self.CI_spinbox.setSuffix(_translate("ContinuousDataForm", " %", None))

import icons_rc
