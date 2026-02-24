# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'barcode_ux_230226.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
import UI.img

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1214, 747)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_13 = QGridLayout(self.centralwidget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.imageFr = QFrame(self.centralwidget)
        self.imageFr.setObjectName(u"imageFr")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageFr.sizePolicy().hasHeightForWidth())
        self.imageFr.setSizePolicy(sizePolicy)
        self.imageFr.setStyleSheet(u"#imageFr\n"
"{\n"
"	background-color:#CBD5E1;\n"
"	border-radius: 8px; /* Bo tr\u00f2n \u0111\u1ec1u 20px */\n"
"	border-bottom: 4px solid #94A3B8;\n"
"}")
        self.imageFr.setFrameShape(QFrame.Shape.StyledPanel)
        self.imageFr.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.imageFr)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, -1)
        self.imgFr_display = QLabel(self.imageFr)
        self.imgFr_display.setObjectName(u"imgFr_display")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(18)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.imgFr_display.sizePolicy().hasHeightForWidth())
        self.imgFr_display.setSizePolicy(sizePolicy1)
        self.imgFr_display.setMinimumSize(QSize(381, 508))
        self.imgFr_display.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin-left: 10px;\n"
"margin-right: 10px;")

        self.gridLayout_7.addWidget(self.imgFr_display, 1, 0, 1, 1)

        self.fr_dis = QFrame(self.imageFr)
        self.fr_dis.setObjectName(u"fr_dis")
        self.fr_dis.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.fr_dis.sizePolicy().hasHeightForWidth())
        self.fr_dis.setSizePolicy(sizePolicy2)
        self.fr_dis.setMinimumSize(QSize(401, 41))
        self.fr_dis.setStyleSheet(u"#fr_dis\n"
"{\n"
"	background-color:#020617;\n"
"	/*border-radius: 8px 8px 0 0; /* Bo tr\u00f2n \u0111\u1ec1u 20px */\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"}")
        self.fr_dis.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_dis.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.fr_dis)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.imgFr_icon = QLabel(self.fr_dis)
        self.imgFr_icon.setObjectName(u"imgFr_icon")
        sizePolicy.setHeightForWidth(self.imgFr_icon.sizePolicy().hasHeightForWidth())
        self.imgFr_icon.setSizePolicy(sizePolicy)
        self.imgFr_icon.setMinimumSize(QSize(21, 21))
        self.imgFr_icon.setStyleSheet(u"#imgFr_icon\n"
"{\n"
"	background-color:#020617;\n"
"    border-image: url(:/img/pic.png) 0 0 0 0 stretch stretch;\n"
"}")

        self.gridLayout_6.addWidget(self.imgFr_icon, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imgFr_title = QLabel(self.fr_dis)
        self.imgFr_title.setObjectName(u"imgFr_title")
        self.imgFr_title.setMinimumSize(QSize(121, 21))
        self.imgFr_title.setStyleSheet(u"#imgFr_title\n"
"{\n"
"	color: #FFFFFF;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 900;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 13px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")

        self.horizontalLayout_2.addWidget(self.imgFr_title)


        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.fr_dis, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.imageFr, 1, 0, 2, 1)

        self.footFr = QFrame(self.centralwidget)
        self.footFr.setObjectName(u"footFr")
        self.footFr.setMinimumSize(QSize(1186, 68))
        self.footFr.setStyleSheet(u"#footFr\n"
"{\n"
"	background-color:#020617;\n"
"	border-top: 4px solid #1c64f2;\n"
"	border-radius: 10px; /* Bo tr\u00f2n \u0111\u1ec1u 20px */\n"
"}")
        self.footFr.setFrameShape(QFrame.Shape.StyledPanel)
        self.footFr.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.footFr)
        self.gridLayout.setObjectName(u"gridLayout")
        self.footFr_title = QLabel(self.footFr)
        self.footFr_title.setObjectName(u"footFr_title")
        self.footFr_title.setMinimumSize(QSize(301, 31))
        self.footFr_title.setStyleSheet(u"#footFr_title\n"
"{\n"
"	color: #FFFFFF;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 900;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 11px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")

        self.gridLayout.addWidget(self.footFr_title, 0, 0, 1, 1)

        self.footFr_notice = QLabel(self.footFr)
        self.footFr_notice.setObjectName(u"footFr_notice")
        self.footFr_notice.setMinimumSize(QSize(821, 51))
        self.footFr_notice.setStyleSheet(u"#footFr_notice\n"
"{\n"
"	color: #FFFFFF;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 900;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 16px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")
        self.footFr_notice.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.footFr_notice, 0, 1, 1, 1)


        self.gridLayout_13.addWidget(self.footFr, 3, 0, 1, 3)

        self.terminationFr = QFrame(self.centralwidget)
        self.terminationFr.setObjectName(u"terminationFr")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.terminationFr.sizePolicy().hasHeightForWidth())
        self.terminationFr.setSizePolicy(sizePolicy3)
        self.terminationFr.setMinimumSize(QSize(458, 161))
        self.terminationFr.setStyleSheet(u"#terminationFr\n"
"{\n"
"	background-color:#CBD5E1;\n"
"	border-radius: 8px; /* Bo tr\u00f2n \u0111\u1ec1u 20px */\n"
"	border-bottom: 4px solid #94A3B8;\n"
"}")
        self.terminationFr.setFrameShape(QFrame.Shape.StyledPanel)
        self.terminationFr.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.terminationFr)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 44)
        self.terminationFr_icon = QLabel(self.terminationFr)
        self.terminationFr_icon.setObjectName(u"terminationFr_icon")
        sizePolicy2.setHeightForWidth(self.terminationFr_icon.sizePolicy().hasHeightForWidth())
        self.terminationFr_icon.setSizePolicy(sizePolicy2)
        self.terminationFr_icon.setMinimumSize(QSize(21, 21))
        self.terminationFr_icon.setStyleSheet(u"#terminationFr_icon\n"
"{\n"
"	background-color:#020617;\n"
"    border-image: url(:/img/terminal.png) 0 0 0 0 stretch stretch;\n"
"}")

        self.horizontalLayout_5.addWidget(self.terminationFr_icon)

        self.terminationFr_title = QLabel(self.terminationFr)
        self.terminationFr_title.setObjectName(u"terminationFr_title")
        self.terminationFr_title.setMinimumSize(QSize(421, 21))
        self.terminationFr_title.setStyleSheet(u"#terminationFr_title\n"
"{\n"
"	color: #000000;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 900;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 18px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")

        self.horizontalLayout_5.addWidget(self.terminationFr_title)


        self.gridLayout_12.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 14, -1)
        self.btnAddImg = QPushButton(self.terminationFr)
        self.btnAddImg.setObjectName(u"btnAddImg")
        sizePolicy2.setHeightForWidth(self.btnAddImg.sizePolicy().hasHeightForWidth())
        self.btnAddImg.setSizePolicy(sizePolicy2)
        self.btnAddImg.setMinimumSize(QSize(161, 51))
        self.btnAddImg.setStyleSheet(u"/* Tr\u1ea1ng th\u00e1i b\u00ecnh th\u01b0\u1eddng */\n"
"#btnAddImg {\n"
"    background-color: #2563EB;      /* M\u00e0u xanh ch\u1ee7 \u0111\u1ea1o */\n"
"    color: white;\n"
"    border-radius: 12px;           /* Bo g\u00f3c l\u1edbn nh\u01b0 trong h\u00ecnh */\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    letter-spacing: 1px;           /* Kho\u1ea3ng c\u00e1ch ch\u1eef cho tho\u00e1ng */\n"
"    border: none;\n"
"    padding: 10px 20px;            /* Kho\u1ea3ng c\u00e1ch \u0111\u1ec7m b\u00ean trong */\n"
"	border-bottom: 3px solid #000080;\n"
"}\n"
"\n"
"/* Tr\u1ea1ng th\u00e1i khi Hover v\u00e0o n\u00fat */\n"
"#btnAddImg:hover {\n"
"    background-color: #1D4ED8;      /* M\u00e0u \u0111\u1eadm h\u01a1n m\u1ed9t ch\u00fat */\n"
"    /* Ph\u00f3ng to b\u1eb1ng c\u00e1ch t\u0103ng padding \u0111\u1ec3 kh\u00f4ng l\u00e0m rung layout */\n"
"    padding: 15px 27px;             \n"
"    font-size: 15px;                /* Ch\u1eef to l\u00ean 1px */\n"
"}\n"
"#btnAddImg:pressed {\n"
"    backg"
                        "round-color: #3a5a80;   /* M\u00e0u khi b\u1ea5m */\n"
"    padding-left: 12px;           /* Gi\u1ea3m padding \u0111\u1ec3 c\u1ea3m gi\u00e1c nh\u1ecf l\u1ea1i */\n"
"    padding-top: 8px;\n"
"    transform: scale(0.95);       /* (Kh\u00f4ng h\u1ed7 tr\u1ee3 trong Qt CSS, ch\u1ec9 c\u00f3 th\u1ec3 d\u00f9ng animation) */\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btnAddImg)

        self.btnReadBarcode = QPushButton(self.terminationFr)
        self.btnReadBarcode.setObjectName(u"btnReadBarcode")
        sizePolicy2.setHeightForWidth(self.btnReadBarcode.sizePolicy().hasHeightForWidth())
        self.btnReadBarcode.setSizePolicy(sizePolicy2)
        self.btnReadBarcode.setMinimumSize(QSize(161, 51))
        self.btnReadBarcode.setStyleSheet(u"/* Tr\u1ea1ng th\u00e1i b\u00ecnh th\u01b0\u1eddng */\n"
"#btnReadBarcode {\n"
"    background-color: #2563EB;      /* M\u00e0u xanh ch\u1ee7 \u0111\u1ea1o */\n"
"    color: white;\n"
"    border-radius: 12px;           /* Bo g\u00f3c l\u1edbn nh\u01b0 trong h\u00ecnh */\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    letter-spacing: 1px;           /* Kho\u1ea3ng c\u00e1ch ch\u1eef cho tho\u00e1ng */\n"
"    border: none;\n"
"    padding: 10px 20px;            /* Kho\u1ea3ng c\u00e1ch \u0111\u1ec7m b\u00ean trong */\n"
"	border-bottom: 3px solid #000080;\n"
"}\n"
"\n"
"/* Tr\u1ea1ng th\u00e1i khi Hover v\u00e0o n\u00fat */\n"
"#btnReadBarcode:hover {\n"
"    background-color: #1D4ED8;      /* M\u00e0u \u0111\u1eadm h\u01a1n m\u1ed9t ch\u00fat */\n"
"    /* Ph\u00f3ng to b\u1eb1ng c\u00e1ch t\u0103ng padding \u0111\u1ec3 kh\u00f4ng l\u00e0m rung layout */\n"
"    padding: 15px 27px;             \n"
"    font-size: 15px;                /* Ch\u1eef to l\u00ean 1px */\n"
"}\n"
"#btnReadBarcode:pressed "
                        "{\n"
"    background-color: #3a5a80;   /* M\u00e0u khi b\u1ea5m */\n"
"    padding-left: 12px;           /* Gi\u1ea3m padding \u0111\u1ec3 c\u1ea3m gi\u00e1c nh\u1ecf l\u1ea1i */\n"
"    padding-top: 8px;\n"
"    transform: scale(0.95);       /* (Kh\u00f4ng h\u1ed7 tr\u1ee3 trong Qt CSS, ch\u1ec9 c\u00f3 th\u1ec3 d\u00f9ng animation) */\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.btnReadBarcode)


        self.gridLayout_12.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.terminationFr, 1, 2, 1, 1)

        self.configFr = QFrame(self.centralwidget)
        self.configFr.setObjectName(u"configFr")
        sizePolicy3.setHeightForWidth(self.configFr.sizePolicy().hasHeightForWidth())
        self.configFr.setSizePolicy(sizePolicy3)
        self.configFr.setMinimumSize(QSize(291, 161))
        self.configFr.setStyleSheet(u"#configFr\n"
"{\n"
"	background-color:#CBD5E1;\n"
"	border-radius: 8px; /* Bo tr\u00f2n \u0111\u1ec1u 20px */\n"
"	border-bottom: 4px solid #94A3B8;\n"
"}")
        self.configFr.setFrameShape(QFrame.Shape.StyledPanel)
        self.configFr.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.configFr)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, -1)
        self.fr_conf = QFrame(self.configFr)
        self.fr_conf.setObjectName(u"fr_conf")
        self.fr_conf.setMinimumSize(QSize(291, 35))
        self.fr_conf.setStyleSheet(u"#fr_conf\n"
"{\n"
"	background-color:#020617;\n"
"	/*border-radius: 8px 8px 0 0; /* Bo tr\u00f2n \u0111\u1ec1u 20px */\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"}\n"
"")
        self.fr_conf.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_conf.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.fr_conf)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.configFr_icon = QLabel(self.fr_conf)
        self.configFr_icon.setObjectName(u"configFr_icon")
        sizePolicy.setHeightForWidth(self.configFr_icon.sizePolicy().hasHeightForWidth())
        self.configFr_icon.setSizePolicy(sizePolicy)
        self.configFr_icon.setMinimumSize(QSize(21, 21))
        self.configFr_icon.setStyleSheet(u"#configFr_icon\n"
"{\n"
"	background-color:#020617;\n"
"    border-image: url(:/img/setting.png) 0 0 0 0 stretch stretch;\n"
"}")

        self.gridLayout_8.addWidget(self.configFr_icon, 0, 0, 1, 1)

        self.configFr_title = QLabel(self.fr_conf)
        self.configFr_title.setObjectName(u"configFr_title")
        self.configFr_title.setMinimumSize(QSize(241, 21))
        self.configFr_title.setStyleSheet(u"#configFr_title\n"
"{\n"
"	color: #FFFFFF;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 900;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 13px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")

        self.gridLayout_8.addWidget(self.configFr_title, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.fr_conf, 0, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(8, 0, 8, -1)
        self.configFr_project_lb = QLabel(self.configFr)
        self.configFr_project_lb.setObjectName(u"configFr_project_lb")
        self.configFr_project_lb.setMinimumSize(QSize(121, 21))
        self.configFr_project_lb.setStyleSheet(u"#configFr_project_lb\n"
"{\n"
"	color: #5D677E;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 900;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 13px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")

        self.verticalLayout_2.addWidget(self.configFr_project_lb)

        self.configFr_prj_list = QComboBox(self.configFr)
        self.configFr_prj_list.setObjectName(u"configFr_prj_list")
        self.configFr_prj_list.setMinimumSize(QSize(121, 31))

        self.verticalLayout_2.addWidget(self.configFr_prj_list)


        self.gridLayout_9.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, -1, 8, -1)
        self.configFr_line_lb = QLabel(self.configFr)
        self.configFr_line_lb.setObjectName(u"configFr_line_lb")
        self.configFr_line_lb.setMinimumSize(QSize(121, 21))
        self.configFr_line_lb.setStyleSheet(u"#configFr_line_lb\n"
"{\n"
"	color: #5D677E;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 900;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 13px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")

        self.verticalLayout_3.addWidget(self.configFr_line_lb)

        self.configFr_line_list = QComboBox(self.configFr)
        self.configFr_line_list.setObjectName(u"configFr_line_list")
        self.configFr_line_list.setMinimumSize(QSize(121, 31))

        self.verticalLayout_3.addWidget(self.configFr_line_list)


        self.gridLayout_9.addLayout(self.verticalLayout_3, 1, 1, 1, 1)

        self.configFr_operation_lb = QLabel(self.configFr)
        self.configFr_operation_lb.setObjectName(u"configFr_operation_lb")
        self.configFr_operation_lb.setMinimumSize(QSize(271, 21))
        self.configFr_operation_lb.setStyleSheet(u"#configFr_operation_lb\n"
"{\n"
"	color: #5D677E;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 900;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 13px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"	margin-left: 6px;\n"
"}")

        self.gridLayout_9.addWidget(self.configFr_operation_lb, 2, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, -1, 0)
        self.chkbox_individual = QCheckBox(self.configFr)
        self.chkbox_individual.setObjectName(u"chkbox_individual")
        self.chkbox_individual.setMinimumSize(QSize(131, 20))
        font = QFont()
        font.setFamilies([u"Small Fonts"])
        font.setWeight(QFont.ExtraBold)
        font.setItalic(False)
        self.chkbox_individual.setFont(font)
        self.chkbox_individual.setStyleSheet(u"#chkbox_individual\n"
"{\n"
"	color: #5D677E;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Small Fonts\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 800;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 10px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")

        self.horizontalLayout_3.addWidget(self.chkbox_individual)

        self.chkbox_bulk = QCheckBox(self.configFr)
        self.chkbox_bulk.setObjectName(u"chkbox_bulk")
        self.chkbox_bulk.setMinimumSize(QSize(111, 20))
        self.chkbox_bulk.setStyleSheet(u"#chkbox_bulk\n"
"{\n"
"	color: #5D677E;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Small Fonts\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 800;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 10px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")

        self.horizontalLayout_3.addWidget(self.chkbox_bulk)


        self.gridLayout_9.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)


        self.gridLayout_13.addWidget(self.configFr, 1, 1, 1, 1)

        self.logFr = QFrame(self.centralwidget)
        self.logFr.setObjectName(u"logFr")
        self.logFr.setStyleSheet(u"#logFr\n"
"{\n"
"	background-color:#CBD5E1;\n"
"	border-radius: 8px; /* Bo tr\u00f2n \u0111\u1ec1u 20px */\n"
"	border-bottom: 4px solid #94A3B8;\n"
"}")
        self.logFr.setFrameShape(QFrame.Shape.StyledPanel)
        self.logFr.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_11 = QGridLayout(self.logFr)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, -1)
        self.fr_log = QFrame(self.logFr)
        self.fr_log.setObjectName(u"fr_log")
        self.fr_log.setMinimumSize(QSize(771, 41))
        self.fr_log.setStyleSheet(u"#fr_log\n"
"{\n"
"	background-color:#94A3B8;\n"
"	/*border-radius: 8px 8px 0 0; /* Bo tr\u00f2n \u0111\u1ec1u 20px */\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"}")
        self.fr_log.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_log.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.fr_log)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, -1, -1, -1)
        self.logFr_icon = QLabel(self.fr_log)
        self.logFr_icon.setObjectName(u"logFr_icon")
        sizePolicy.setHeightForWidth(self.logFr_icon.sizePolicy().hasHeightForWidth())
        self.logFr_icon.setSizePolicy(sizePolicy)
        self.logFr_icon.setMinimumSize(QSize(31, 31))
        self.logFr_icon.setStyleSheet(u"#logFr_icon\n"
"{\n"
"	background-color:#020617;\n"
"    border-image: url(:/img/note.png) 0 0 0 0 stretch stretch;\n"
"}")

        self.gridLayout_10.addWidget(self.logFr_icon, 0, 0, 1, 1)

        self.logFr_title = QLabel(self.fr_log)
        self.logFr_title.setObjectName(u"logFr_title")
        self.logFr_title.setMinimumSize(QSize(691, 21))
        self.logFr_title.setStyleSheet(u"#logFr_title\n"
"{\n"
"	color: #FFFFFF;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 900;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 18px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")

        self.gridLayout_10.addWidget(self.logFr_title, 0, 1, 1, 1)


        self.gridLayout_11.addWidget(self.fr_log, 0, 0, 1, 1)

        self.tableView = QTableView(self.logFr)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(751, 338))
        self.tableView.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"margin-left: 10px;\n"
"margin-right: 10px;\n"
"")

        self.gridLayout_11.addWidget(self.tableView, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.logFr, 2, 1, 1, 2)

        self.headFr = QFrame(self.centralwidget)
        self.headFr.setObjectName(u"headFr")
        self.headFr.setMinimumSize(QSize(1181, 81))
        self.headFr.setStyleSheet(u"#headFr\n"
"{\n"
"	background-color:#020617;\n"
"	border-bottom: 4px solid #1c64f2;\n"
"	border-radius: 8px; /* Bo tr\u00f2n \u0111\u1ec1u 20px */\n"
"}\n"
"")
        self.headFr.setFrameShape(QFrame.Shape.StyledPanel)
        self.headFr.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.headFr)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.headFr_lbIcon = QLabel(self.headFr)
        self.headFr_lbIcon.setObjectName(u"headFr_lbIcon")
        sizePolicy.setHeightForWidth(self.headFr_lbIcon.sizePolicy().hasHeightForWidth())
        self.headFr_lbIcon.setSizePolicy(sizePolicy)
        self.headFr_lbIcon.setMinimumSize(QSize(71, 63))
        self.headFr_lbIcon.setStyleSheet(u"#headFr_lbIcon\n"
"{\n"
"	background-color:#9CA3AF;\n"
"    border-image: url(:/img/barcode.png) 0 0 0 0 stretch stretch;\n"
"}")

        self.gridLayout_5.addWidget(self.headFr_lbIcon, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headFr_lbTitle = QLabel(self.headFr)
        self.headFr_lbTitle.setObjectName(u"headFr_lbTitle")
        self.headFr_lbTitle.setMinimumSize(QSize(371, 31))
        self.headFr_lbTitle.setStyleSheet(u"#headFr_lbTitle\n"
"{\n"
"	color: #FFFFFF;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 900;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: italic;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 24px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")

        self.verticalLayout.addWidget(self.headFr_lbTitle)

        self.headFr_lbSubT = QLabel(self.headFr)
        self.headFr_lbSubT.setObjectName(u"headFr_lbSubT")
        self.headFr_lbSubT.setMinimumSize(QSize(371, 31))
        self.headFr_lbSubT.setStyleSheet(u"#headFr_lbSubT\n"
"{\n"
"	color: #FFFFFF;              /* M\u00e0u tr\u1eafng */\n"
"    font-family: \"Segoe UI\", sans-serif; /* Font kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-weight: 900;            /* \u0110\u1ed9 d\u00e0y t\u1ed1i \u0111a */\n"
"    font-style: normal;          /* Ch\u1eef nghi\u00eang */\n"
"    font-size: 11px;             /* K\u00edch th\u01b0\u1edbc ch\u1eef */\n"
"    letter-spacing: 1px;         /* Kho\u1ea3ng c\u00e1ch gi\u1eefa c\u00e1c ch\u1eef */\n"
"}")

        self.verticalLayout.addWidget(self.headFr_lbSubT)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 1, 1, 1)

        self.frTong = QFrame(self.headFr)
        self.frTong.setObjectName(u"frTong")
        self.frTong.setStyleSheet(u"#frTong\n"
" {\n"
"    background-color: #1a1f2b; /* M\u00e0u n\u1ec1n t\u1ed1i xanh nh\u1eb9 */\n"
"    border: 1px solid #2d3748; /* Vi\u1ec1n m\u1edd \u0111\u1ec3 t\u1ea1o kh\u1ed1i */\n"
"    border-radius: 8px;\n"
"    min-width: 80px;\n"
"    max-width: 100px;\n"
"    min-height: 60px;\n"
"}")
        self.frTong.setFrameShape(QFrame.Shape.StyledPanel)
        self.frTong.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frTong)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frTong_total = QLabel(self.frTong)
        self.frTong_total.setObjectName(u"frTong_total")
        self.frTong_total.setMinimumSize(QSize(61, 16))
        font1 = QFont()
        font1.setBold(True)
        self.frTong_total.setFont(font1)
        self.frTong_total.setStyleSheet(u"#frTong_total\n"
"{\n"
"	text-align: center;	\n"
"	color:#FFFFFF;\n"
"	font-size:16px;\n"
"}")
        self.frTong_total.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.frTong_total, 0, 0, 1, 1)

        self.frTong_total_value = QLabel(self.frTong)
        self.frTong_total_value.setObjectName(u"frTong_total_value")
        self.frTong_total_value.setMinimumSize(QSize(61, 21))
        self.frTong_total_value.setFont(font1)
        self.frTong_total_value.setStyleSheet(u"#frTong_total_value\n"
"{\n"
"	text-align: center;	\n"
"	color:#FFFFFF;\n"
"	font-size:22px;\n"
"}")
        self.frTong_total_value.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.frTong_total_value, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frTong, 0, 2, 1, 1)

        self.frPass = QFrame(self.headFr)
        self.frPass.setObjectName(u"frPass")
        self.frPass.setStyleSheet(u"#frPass\n"
" {\n"
"    background-color: #1a1f2b; /* M\u00e0u n\u1ec1n t\u1ed1i xanh nh\u1eb9 */\n"
"    border: 1px solid #2d3748; /* Vi\u1ec1n m\u1edd \u0111\u1ec3 t\u1ea1o kh\u1ed1i */\n"
"    border-radius: 8px;\n"
"    min-width: 80px;\n"
"    max-width: 100px;\n"
"    min-height: 60px;\n"
"}")
        self.frPass.setFrameShape(QFrame.Shape.StyledPanel)
        self.frPass.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frPass)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frPass_vl = QLabel(self.frPass)
        self.frPass_vl.setObjectName(u"frPass_vl")
        self.frPass_vl.setMinimumSize(QSize(61, 21))
        self.frPass_vl.setFont(font1)
        self.frPass_vl.setStyleSheet(u"#frPass_vl\n"
"{\n"
"	text-align: center;	\n"
"	color:#22C55E;\n"
"	font-size:22px;\n"
"}")
        self.frPass_vl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.frPass_vl, 1, 0, 1, 1)

        self.frPass_lb = QLabel(self.frPass)
        self.frPass_lb.setObjectName(u"frPass_lb")
        self.frPass_lb.setMinimumSize(QSize(61, 16))
        self.frPass_lb.setFont(font1)
        self.frPass_lb.setStyleSheet(u"#frPass_lb\n"
"{\n"
"	text-align: center;	\n"
"	color:#22C55E;\n"
"	font-size:16px;\n"
"}")
        self.frPass_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.frPass_lb, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frPass, 0, 3, 1, 1)

        self.frFail = QFrame(self.headFr)
        self.frFail.setObjectName(u"frFail")
        self.frFail.setStyleSheet(u"#frFail\n"
" {\n"
"    background-color: #1a1f2b; /* M\u00e0u n\u1ec1n t\u1ed1i xanh nh\u1eb9 */\n"
"    border: 1px solid #2d3748; /* Vi\u1ec1n m\u1edd \u0111\u1ec3 t\u1ea1o kh\u1ed1i */\n"
"    border-radius: 8px;\n"
"    min-width: 80px;\n"
"    max-width: 100px;\n"
"    min-height: 60px;\n"
"}")
        self.frFail.setFrameShape(QFrame.Shape.StyledPanel)
        self.frFail.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frFail)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frFail_lb = QLabel(self.frFail)
        self.frFail_lb.setObjectName(u"frFail_lb")
        self.frFail_lb.setMinimumSize(QSize(61, 16))
        self.frFail_lb.setFont(font1)
        self.frFail_lb.setStyleSheet(u"#frFail_lb\n"
"{\n"
"	text-align: center;	\n"
"	color:#EF4444;\n"
"	font-size:16px;\n"
"}")
        self.frFail_lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.frFail_lb, 0, 0, 1, 1)

        self.frFail_vl = QLabel(self.frFail)
        self.frFail_vl.setObjectName(u"frFail_vl")
        self.frFail_vl.setMinimumSize(QSize(61, 21))
        self.frFail_vl.setFont(font1)
        self.frFail_vl.setStyleSheet(u"#frFail_vl\n"
"{\n"
"	text-align: center;	\n"
"	color:#EF4444;\n"
"	font-size:22px;\n"
"}")
        self.frFail_vl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.frFail_vl, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frFail, 0, 4, 1, 1)


        self.gridLayout_13.addWidget(self.headFr, 0, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.imgFr_display.setText("")
        self.imgFr_icon.setText("")
        self.imgFr_title.setText(QCoreApplication.translate("MainWindow", u"Image Display", None))
        self.footFr_title.setText(QCoreApplication.translate("MainWindow", u"Developed by Kent - PE Label Team", None))
        self.footFr_notice.setText(QCoreApplication.translate("MainWindow", u"Notice", None))
        self.terminationFr_icon.setText("")
        self.terminationFr_title.setText(QCoreApplication.translate("MainWindow", u"Inspection Terminal", None))
        self.btnAddImg.setText(QCoreApplication.translate("MainWindow", u"Add Image", None))
        self.btnReadBarcode.setText(QCoreApplication.translate("MainWindow", u"Read Barcode", None))
        self.configFr_icon.setText("")
        self.configFr_title.setText(QCoreApplication.translate("MainWindow", u"Configuration", None))
        self.configFr_project_lb.setText(QCoreApplication.translate("MainWindow", u"Project ID", None))
        self.configFr_prj_list.setCurrentText("")
        self.configFr_line_lb.setText(QCoreApplication.translate("MainWindow", u"Production Line", None))
        self.configFr_operation_lb.setText(QCoreApplication.translate("MainWindow", u"Operation Mode", None))
        self.chkbox_individual.setText(QCoreApplication.translate("MainWindow", u"Individual Check", None))
        self.chkbox_bulk.setText(QCoreApplication.translate("MainWindow", u"Bulk Check", None))
        self.logFr_icon.setText("")
        self.logFr_title.setText(QCoreApplication.translate("MainWindow", u"Operation Logs Record", None))
        self.headFr_lbIcon.setText("")
        self.headFr_lbTitle.setText(QCoreApplication.translate("MainWindow", u"LABEL BARCODE INSPECTOR", None))
        self.headFr_lbSubT.setText(QCoreApplication.translate("MainWindow", u"Read barcode and Inspect them for Label Approval", None))
        self.frTong_total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.frTong_total_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.frPass_vl.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.frPass_lb.setText(QCoreApplication.translate("MainWindow", u"Pass", None))
        self.frFail_lb.setText(QCoreApplication.translate("MainWindow", u"Fail", None))
        self.frFail_vl.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

