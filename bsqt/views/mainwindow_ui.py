# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpinBox,
    QStatusBar, QTabWidget, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(535, 684)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_types = QTabWidget(self.centralwidget)
        self.list_types.setObjectName(u"list_types")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_types.sizePolicy().hasHeightForWidth())
        self.list_types.setSizePolicy(sizePolicy)
        self.latest = QWidget()
        self.latest.setObjectName(u"latest")
        self.verticalLayout_3 = QVBoxLayout(self.latest)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.latest_date_layout = QHBoxLayout()
        self.latest_date_layout.setObjectName(u"latest_date_layout")
        self.latest_after_frame = QFrame(self.latest)
        self.latest_after_frame.setObjectName(u"latest_after_frame")
        self.latest_after_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.latest_after_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.latest_after_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.latest_after_label = QLabel(self.latest_after_frame)
        self.latest_after_label.setObjectName(u"latest_after_label")

        self.horizontalLayout.addWidget(self.latest_after_label)

        self.latest_after_edit = QDateTimeEdit(self.latest_after_frame)
        self.latest_after_edit.setObjectName(u"latest_after_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.latest_after_edit.sizePolicy().hasHeightForWidth())
        self.latest_after_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.latest_after_edit)

        self.line = QFrame(self.latest_after_frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.latest_before_label = QLabel(self.latest_after_frame)
        self.latest_before_label.setObjectName(u"latest_before_label")

        self.horizontalLayout.addWidget(self.latest_before_label)

        self.latest_before_edit = QDateTimeEdit(self.latest_after_frame)
        self.latest_before_edit.setObjectName(u"latest_before_edit")
        sizePolicy1.setHeightForWidth(self.latest_before_edit.sizePolicy().hasHeightForWidth())
        self.latest_before_edit.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.latest_before_edit)


        self.latest_date_layout.addWidget(self.latest_after_frame)


        self.verticalLayout_3.addLayout(self.latest_date_layout)

        self.latest_verified_frame = QFrame(self.latest)
        self.latest_verified_frame.setObjectName(u"latest_verified_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.latest_verified_frame.sizePolicy().hasHeightForWidth())
        self.latest_verified_frame.setSizePolicy(sizePolicy2)
        self.latest_verified_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.latest_verified_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.latest_verified_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.latest_verified_button_group = QGroupBox(self.latest_verified_frame)
        self.latest_verified_button_group.setObjectName(u"latest_verified_button_group")
        self.latest_verified_button_group.setEnabled(True)
        self.latest_verified_button_group.setFlat(True)
        self.latest_verified_button_group.setCheckable(False)
        self.horizontalLayout_6 = QHBoxLayout(self.latest_verified_button_group)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.latest_verified_exclude = QRadioButton(self.latest_verified_button_group)
        self.latest_verified_exclude.setObjectName(u"latest_verified_exclude")

        self.horizontalLayout_6.addWidget(self.latest_verified_exclude)

        self.latest_verified_include = QRadioButton(self.latest_verified_button_group)
        self.latest_verified_include.setObjectName(u"latest_verified_include")
        self.latest_verified_include.setChecked(True)

        self.horizontalLayout_6.addWidget(self.latest_verified_include)

        self.latest_verified_only = QRadioButton(self.latest_verified_button_group)
        self.latest_verified_only.setObjectName(u"latest_verified_only")

        self.horizontalLayout_6.addWidget(self.latest_verified_only)


        self.horizontalLayout_4.addWidget(self.latest_verified_button_group)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.latest_automapper_checkbox = QCheckBox(self.latest_verified_frame)
        self.latest_automapper_checkbox.setObjectName(u"latest_automapper_checkbox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.latest_automapper_checkbox.sizePolicy().hasHeightForWidth())
        self.latest_automapper_checkbox.setSizePolicy(sizePolicy3)
        self.latest_automapper_checkbox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.verticalLayout_6.addWidget(self.latest_automapper_checkbox)


        self.verticalLayout_3.addWidget(self.latest_verified_frame)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.latest_sort_frame = QFrame(self.latest)
        self.latest_sort_frame.setObjectName(u"latest_sort_frame")
        self.latest_sort_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.latest_sort_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.latest_sort_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.latest_sort_label = QLabel(self.latest_sort_frame)
        self.latest_sort_label.setObjectName(u"latest_sort_label")

        self.horizontalLayout_7.addWidget(self.latest_sort_label)

        self.latest_sort_cbox = QComboBox(self.latest_sort_frame)
        self.latest_sort_cbox.addItem("")
        self.latest_sort_cbox.addItem("")
        self.latest_sort_cbox.addItem("")
        self.latest_sort_cbox.addItem("")
        self.latest_sort_cbox.addItem("")
        self.latest_sort_cbox.setObjectName(u"latest_sort_cbox")
        sizePolicy1.setHeightForWidth(self.latest_sort_cbox.sizePolicy().hasHeightForWidth())
        self.latest_sort_cbox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.latest_sort_cbox)


        self.horizontalLayout_8.addWidget(self.latest_sort_frame)

        self.frame = QFrame(self.latest)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.latest_page_size_label = QLabel(self.frame)
        self.latest_page_size_label.setObjectName(u"latest_page_size_label")

        self.horizontalLayout_2.addWidget(self.latest_page_size_label)

        self.latest_page_size = QSpinBox(self.frame)
        self.latest_page_size.setObjectName(u"latest_page_size")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.latest_page_size.sizePolicy().hasHeightForWidth())
        self.latest_page_size.setSizePolicy(sizePolicy4)
        self.latest_page_size.setMinimum(1)
        self.latest_page_size.setMaximum(100)
        self.latest_page_size.setValue(20)

        self.horizontalLayout_2.addWidget(self.latest_page_size)


        self.horizontalLayout_8.addWidget(self.frame)

        self.latest_search_button = QPushButton(self.latest)
        self.latest_search_button.setObjectName(u"latest_search_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.latest_search_button.sizePolicy().hasHeightForWidth())
        self.latest_search_button.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.latest_search_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.list_types.addTab(self.latest, "")

        self.verticalLayout.addWidget(self.list_types)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 513, 383))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.map_tree = QTreeWidget(self.scrollAreaWidgetContents)
        self.map_tree.setObjectName(u"map_tree")
        self.map_tree.setHeaderHidden(False)
        self.map_tree.header().setVisible(True)
        self.map_tree.header().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.map_tree)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.list_types.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.latest_after_label.setText(QCoreApplication.translate("MainWindow", u"After", None))
        self.latest_before_label.setText(QCoreApplication.translate("MainWindow", u"Before", None))
        self.latest_verified_button_group.setTitle(QCoreApplication.translate("MainWindow", u"Verified Mappers", None))
        self.latest_verified_exclude.setText(QCoreApplication.translate("MainWindow", u"Exclude", None))
        self.latest_verified_include.setText(QCoreApplication.translate("MainWindow", u"Include", None))
        self.latest_verified_only.setText(QCoreApplication.translate("MainWindow", u"Verified Only", None))
        self.latest_automapper_checkbox.setText(QCoreApplication.translate("MainWindow", u"Include automapper?", None))
        self.latest_sort_label.setText(QCoreApplication.translate("MainWindow", u"Sort", None))
        self.latest_sort_cbox.setItemText(0, QCoreApplication.translate("MainWindow", u"First Published", None))
        self.latest_sort_cbox.setItemText(1, QCoreApplication.translate("MainWindow", u"Updated", None))
        self.latest_sort_cbox.setItemText(2, QCoreApplication.translate("MainWindow", u"Last Published", None))
        self.latest_sort_cbox.setItemText(3, QCoreApplication.translate("MainWindow", u"Created", None))
        self.latest_sort_cbox.setItemText(4, QCoreApplication.translate("MainWindow", u"Curated", None))

        self.latest_page_size_label.setText(QCoreApplication.translate("MainWindow", u"Page Size", None))
        self.latest_search_button.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.list_types.setTabText(self.list_types.indexOf(self.latest), QCoreApplication.translate("MainWindow", u"Latest", None))
        ___qtreewidgetitem = self.map_tree.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Mapper", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Name", None));
    # retranslateUi

