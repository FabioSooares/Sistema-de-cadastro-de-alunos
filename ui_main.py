# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        icon = QIcon()
        icon.addFile(u":/Icons/\u00edcone.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border:none;\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, -1, 0, -1)
        self.Main_Conteiner = QFrame(self.centralwidget)
        self.Main_Conteiner.setObjectName(u"Main_Conteiner")
        self.Main_Conteiner.setFrameShape(QFrame.StyledPanel)
        self.Main_Conteiner.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main_Conteiner)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(40, 0, 10, 0)
        self.Header = QFrame(self.Main_Conteiner)
        self.Header.setObjectName(u"Header")
        self.Header.setFrameShape(QFrame.StyledPanel)
        self.Header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 7, 0, 0)
        self.btn_toggle = QPushButton(self.Header)
        self.btn_toggle.setObjectName(u"btn_toggle")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon1)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.Header)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(24)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.Header)

        self.Main_Frame = QFrame(self.Main_Conteiner)
        self.Main_Frame.setObjectName(u"Main_Frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Main_Frame.sizePolicy().hasHeightForWidth())
        self.Main_Frame.setSizePolicy(sizePolicy)
        self.Main_Frame.setStyleSheet(u"")
        self.Main_Frame.setFrameShape(QFrame.StyledPanel)
        self.Main_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Main_Frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.Pages = QStackedWidget(self.Main_Frame)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setMinimumSize(QSize(500, 280))
        self.Pages.setMaximumSize(QSize(2000, 1500))
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.horizontalLayout = QHBoxLayout(self.pg_home)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.lbl_logo_login_2 = QLabel(self.pg_home)
        self.lbl_logo_login_2.setObjectName(u"lbl_logo_login_2")
        self.lbl_logo_login_2.setMinimumSize(QSize(480, 280))
        self.lbl_logo_login_2.setMaximumSize(QSize(850, 400))
        self.lbl_logo_login_2.setPixmap(QPixmap(u":/icons/Icons/Logo CEAI.png"))
        self.lbl_logo_login_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.lbl_logo_login_2)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastrar = QWidget()
        self.pg_cadastrar.setObjectName(u"pg_cadastrar")
        self.verticalLayout_8 = QVBoxLayout(self.pg_cadastrar)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 0, 0, 0)
        self.tabWidget = QTabWidget(self.pg_cadastrar)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-radius:30px")
        self.tab_aluno = QWidget()
        self.tab_aluno.setObjectName(u"tab_aluno")
        self.verticalLayout_6 = QVBoxLayout(self.tab_aluno)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_4 = QFrame(self.tab_aluno)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(194, 232, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(20)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 5)

        self.txt_nome = QLineEdit(self.frame_4)
        self.txt_nome.setObjectName(u"txt_nome")
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        self.txt_nome.setFont(font2)
        self.txt_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_nome.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 1, 0, 1, 4)

        self.txt_serie = QLineEdit(self.frame_4)
        self.txt_serie.setObjectName(u"txt_serie")
        self.txt_serie.setFont(font2)
        self.txt_serie.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_serie.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_serie, 1, 4, 1, 4)

        self.txt_nascimento = QLineEdit(self.frame_4)
        self.txt_nascimento.setObjectName(u"txt_nascimento")
        self.txt_nascimento.setFont(font2)
        self.txt_nascimento.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_nascimento.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nascimento, 1, 8, 1, 1)

        self.txt_naturalidade = QLineEdit(self.frame_4)
        self.txt_naturalidade.setObjectName(u"txt_naturalidade")
        self.txt_naturalidade.setFont(font2)
        self.txt_naturalidade.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_naturalidade.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_naturalidade, 2, 0, 1, 2)

        self.txt_nacionalidade = QLineEdit(self.frame_4)
        self.txt_nacionalidade.setObjectName(u"txt_nacionalidade")
        self.txt_nacionalidade.setFont(font2)
        self.txt_nacionalidade.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_nacionalidade.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_nacionalidade, 2, 2, 1, 4)

        self.txt_telefone_aluno = QLineEdit(self.frame_4)
        self.txt_telefone_aluno.setObjectName(u"txt_telefone_aluno")
        self.txt_telefone_aluno.setFont(font2)
        self.txt_telefone_aluno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_telefone_aluno.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_telefone_aluno, 2, 6, 1, 3)

        self.txt_pai = QLineEdit(self.frame_4)
        self.txt_pai.setObjectName(u"txt_pai")
        self.txt_pai.setFont(font2)
        self.txt_pai.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_pai.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_pai, 3, 0, 1, 5)

        self.txt_mae = QLineEdit(self.frame_4)
        self.txt_mae.setObjectName(u"txt_mae")
        self.txt_mae.setFont(font2)
        self.txt_mae.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_mae.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_mae, 3, 5, 1, 4)

        self.txt_rg_aluno = QLineEdit(self.frame_4)
        self.txt_rg_aluno.setObjectName(u"txt_rg_aluno")
        self.txt_rg_aluno.setFont(font2)
        self.txt_rg_aluno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_rg_aluno.setEchoMode(QLineEdit.Normal)
        self.txt_rg_aluno.setCursorPosition(0)
        self.txt_rg_aluno.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_rg_aluno, 4, 0, 1, 5)

        self.txt_cpf_aluno = QLineEdit(self.frame_4)
        self.txt_cpf_aluno.setObjectName(u"txt_cpf_aluno")
        self.txt_cpf_aluno.setFont(font2)
        self.txt_cpf_aluno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_cpf_aluno.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cpf_aluno, 4, 5, 1, 4)

        self.txt_cep = QLineEdit(self.frame_4)
        self.txt_cep.setObjectName(u"txt_cep")
        self.txt_cep.setFont(font2)
        self.txt_cep.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cep, 5, 0, 1, 1)

        self.txt_endereco = QLineEdit(self.frame_4)
        self.txt_endereco.setObjectName(u"txt_endereco")
        self.txt_endereco.setFont(font2)
        self.txt_endereco.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_endereco.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_endereco, 5, 1, 1, 8)

        self.txt_bairro_aluno = QLineEdit(self.frame_4)
        self.txt_bairro_aluno.setObjectName(u"txt_bairro_aluno")
        self.txt_bairro_aluno.setFont(font2)
        self.txt_bairro_aluno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_bairro_aluno.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_bairro_aluno, 6, 0, 1, 4)

        self.txt_cidade_aluno = QLineEdit(self.frame_4)
        self.txt_cidade_aluno.setObjectName(u"txt_cidade_aluno")
        self.txt_cidade_aluno.setFont(font2)
        self.txt_cidade_aluno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_cidade_aluno.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_cidade_aluno, 6, 4, 1, 5)

        self.txt_professora = QLineEdit(self.frame_4)
        self.txt_professora.setObjectName(u"txt_professora")
        self.txt_professora.setFont(font2)
        self.txt_professora.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_professora.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_professora, 7, 0, 1, 3)

        self.txt_turma = QLineEdit(self.frame_4)
        self.txt_turma.setObjectName(u"txt_turma")
        self.txt_turma.setFont(font2)
        self.txt_turma.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_turma.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_turma, 7, 3, 1, 4)

        self.txt_email_aluno = QLineEdit(self.frame_4)
        self.txt_email_aluno.setObjectName(u"txt_email_aluno")
        self.txt_email_aluno.setFont(font2)
        self.txt_email_aluno.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_email_aluno.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_email_aluno, 7, 7, 1, 2)

        self.txt_alergia = QLineEdit(self.frame_4)
        self.txt_alergia.setObjectName(u"txt_alergia")
        self.txt_alergia.setFont(font2)
        self.txt_alergia.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_alergia.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_alergia, 8, 0, 1, 9)

        self.btn_cadastrar_aluno_2 = QPushButton(self.frame_4)
        self.btn_cadastrar_aluno_2.setObjectName(u"btn_cadastrar_aluno_2")
        self.btn_cadastrar_aluno_2.setMinimumSize(QSize(0, 35))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(14)
        self.btn_cadastrar_aluno_2.setFont(font3)
        self.btn_cadastrar_aluno_2.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 255);\n"
"    border-radius:17px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255,255,255);\n"
"	background-color: rgb(0, 0, 255);\n"
"    border-radius:17px\n"
"}")

        self.gridLayout.addWidget(self.btn_cadastrar_aluno_2, 9, 3, 1, 4)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tab_aluno, "")
        self.tab_professor = QWidget()
        self.tab_professor.setObjectName(u"tab_professor")
        self.verticalLayout_11 = QVBoxLayout(self.tab_professor)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_5 = QFrame(self.tab_professor)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(194, 232, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 4)

        self.txt_nome_prof = QLineEdit(self.frame_5)
        self.txt_nome_prof.setObjectName(u"txt_nome_prof")
        self.txt_nome_prof.setFont(font2)
        self.txt_nome_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_nome_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_nome_prof, 1, 0, 1, 4)

        self.txt_nascimento_prof = QLineEdit(self.frame_5)
        self.txt_nascimento_prof.setObjectName(u"txt_nascimento_prof")
        self.txt_nascimento_prof.setFont(font2)
        self.txt_nascimento_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_nascimento_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_nascimento_prof, 1, 4, 1, 2)

        self.txt_naturalidade_prof = QLineEdit(self.frame_5)
        self.txt_naturalidade_prof.setObjectName(u"txt_naturalidade_prof")
        self.txt_naturalidade_prof.setFont(font2)
        self.txt_naturalidade_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_naturalidade_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_naturalidade_prof, 2, 0, 1, 1)

        self.txt_nacionalidade_prof = QLineEdit(self.frame_5)
        self.txt_nacionalidade_prof.setObjectName(u"txt_nacionalidade_prof")
        self.txt_nacionalidade_prof.setFont(font2)
        self.txt_nacionalidade_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_nacionalidade_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_nacionalidade_prof, 2, 1, 1, 4)

        self.txt_telefone_prof = QLineEdit(self.frame_5)
        self.txt_telefone_prof.setObjectName(u"txt_telefone_prof")
        self.txt_telefone_prof.setFont(font2)
        self.txt_telefone_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_telefone_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_telefone_prof, 2, 5, 1, 1)

        self.txt_rg_prof = QLineEdit(self.frame_5)
        self.txt_rg_prof.setObjectName(u"txt_rg_prof")
        self.txt_rg_prof.setFont(font2)
        self.txt_rg_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_rg_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_rg_prof, 3, 0, 1, 2)

        self.txt_cpf_prof_2 = QLineEdit(self.frame_5)
        self.txt_cpf_prof_2.setObjectName(u"txt_cpf_prof_2")
        self.txt_cpf_prof_2.setFont(font2)
        self.txt_cpf_prof_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_cpf_prof_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cpf_prof_2, 3, 2, 1, 4)

        self.txt_cep_prof = QLineEdit(self.frame_5)
        self.txt_cep_prof.setObjectName(u"txt_cep_prof")
        self.txt_cep_prof.setFont(font2)
        self.txt_cep_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_cep_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cep_prof, 4, 0, 1, 1)

        self.txt_endereco_prof = QLineEdit(self.frame_5)
        self.txt_endereco_prof.setObjectName(u"txt_endereco_prof")
        self.txt_endereco_prof.setFont(font2)
        self.txt_endereco_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_endereco_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_endereco_prof, 4, 1, 1, 5)

        self.txt_bairro_prof = QLineEdit(self.frame_5)
        self.txt_bairro_prof.setObjectName(u"txt_bairro_prof")
        self.txt_bairro_prof.setFont(font2)
        self.txt_bairro_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_bairro_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_bairro_prof, 5, 0, 1, 3)

        self.txt_cidade_prof = QLineEdit(self.frame_5)
        self.txt_cidade_prof.setObjectName(u"txt_cidade_prof")
        self.txt_cidade_prof.setFont(font2)
        self.txt_cidade_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_cidade_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_cidade_prof, 5, 3, 1, 3)

        self.txt_disciplinas_prof = QLineEdit(self.frame_5)
        self.txt_disciplinas_prof.setObjectName(u"txt_disciplinas_prof")
        self.txt_disciplinas_prof.setFont(font2)
        self.txt_disciplinas_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_disciplinas_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_disciplinas_prof, 6, 0, 1, 2)

        self.txt_turma_prof = QLineEdit(self.frame_5)
        self.txt_turma_prof.setObjectName(u"txt_turma_prof")
        self.txt_turma_prof.setFont(font2)
        self.txt_turma_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_turma_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_turma_prof, 6, 2, 1, 4)

        self.txt_email_prof = QLineEdit(self.frame_5)
        self.txt_email_prof.setObjectName(u"txt_email_prof")
        self.txt_email_prof.setFont(font2)
        self.txt_email_prof.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:9px")
        self.txt_email_prof.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.txt_email_prof, 7, 0, 1, 6)

        self.btn_cadastrar_professor_3 = QPushButton(self.frame_5)
        self.btn_cadastrar_professor_3.setObjectName(u"btn_cadastrar_professor_3")
        self.btn_cadastrar_professor_3.setMinimumSize(QSize(0, 35))
        self.btn_cadastrar_professor_3.setFont(font3)
        self.btn_cadastrar_professor_3.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 170, 255);\n"
"    border-radius:17px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255,255,255);\n"
"	background-color: rgb(0, 0, 255);\n"
"    border-radius:17px\n"
"}")

        self.gridLayout_2.addWidget(self.btn_cadastrar_professor_3, 8, 1, 1, 4)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.tabWidget.addTab(self.tab_professor, "")
        self.tab_turma = QWidget()
        self.tab_turma.setObjectName(u"tab_turma")
        self.tab_turma.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"border-radius:15px\n"
"")
        self.gridLayout_4 = QGridLayout(self.tab_turma)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, -1, -1, -1)
        self.label_5 = QLabel(self.tab_turma)
        self.label_5.setObjectName(u"label_5")
        font4 = QFont()
        font4.setFamilies([u"Comic Sans MS"])
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setItalic(True)
        self.label_5.setFont(font4)
        self.label_5.setTabletTracking(False)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(194, 232, 255);\n"
"border-radius:10px")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, -1, -1)
        self.tableWidget = QTableWidget(self.tab_turma)
        if (self.tableWidget.columnCount() < 15):
            self.tableWidget.setColumnCount(15)
        font5 = QFont()
        font5.setFamilies([u"Comic Sans MS"])
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: rgb(249, 252, 86);\n"
"	color: rgb(0,0,0);\n"
"	\n"
"	font: 700 italic 11pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(194, 232, 255);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.tableWidget)

        self.frame_3 = QFrame(self.tab_turma)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setStyleSheet(u"background-color: rgb(194, 232, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(3, 70, 3, 0)
        self.btn_excel = QPushButton(self.frame_3)
        self.btn_excel.setObjectName(u"btn_excel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_excel.sizePolicy().hasHeightForWidth())
        self.btn_excel.setSizePolicy(sizePolicy1)
        self.btn_excel.setMinimumSize(QSize(120, 25))
        self.btn_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel.setStyleSheet(u"QPushButton {\n"
"   	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 170, 255);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0,0,0);\n"
"	background-color: rgb(38, 255, 0);\n"
"    border-radius:10px\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_excel)

        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(120, 25))
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"		background-color: rgb(0, 170, 255);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0,0,0);\n"
"	background-color: rgb(252, 252, 0);\n"
"    border-radius:10px\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_3)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(120, 25))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 0, 0);\n"
"    border-radius:10px\n"
"}")

        self.verticalLayout_7.addWidget(self.btn_excluir)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addWidget(self.frame_3)


        self.gridLayout_4.addLayout(self.horizontalLayout_6, 4, 0, 1, 1)

        self.lineEdit = QLineEdit(self.tab_turma)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"background-color: rgb(194, 232, 255);\n"
"\n"
"border-radius:8px")

        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_turma, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_8 = QHBoxLayout(self.tab)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tableWidget_2 = QTableWidget(self.tab)
        if (self.tableWidget_2.columnCount() < 15):
            self.tableWidget_2.setColumnCount(15)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(12, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(13, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(14, __qtablewidgetitem29)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"QHeaderView::section {\n"
"	background-color: rgb(249, 252, 86);\n"
"	color: rgb(0,0,0);\n"
"	\n"
"	font: 700 italic 11pt \"Comic Sans MS\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"background-color: rgb(194, 232, 255);\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.tableWidget_2)

        self.frame_11 = QFrame(self.tab)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 0))
        self.frame_11.setStyleSheet(u"background-color: rgb(194, 232, 255);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(3, 70, 3, 0)
        self.btn_excel_2 = QPushButton(self.frame_11)
        self.btn_excel_2.setObjectName(u"btn_excel_2")
        sizePolicy1.setHeightForWidth(self.btn_excel_2.sizePolicy().hasHeightForWidth())
        self.btn_excel_2.setSizePolicy(sizePolicy1)
        self.btn_excel_2.setMinimumSize(QSize(120, 25))
        self.btn_excel_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excel_2.setStyleSheet(u"QPushButton {\n"
"   	color: rgb(0, 0, 0);\n"
"	background-color: rgb(0, 170, 255);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0,0,0);\n"
"	background-color: rgb(38, 255, 0);\n"
"    border-radius:10px\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_excel_2)

        self.btn_alterar_2 = QPushButton(self.frame_11)
        self.btn_alterar_2.setObjectName(u"btn_alterar_2")
        self.btn_alterar_2.setMinimumSize(QSize(120, 25))
        self.btn_alterar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_2.setStyleSheet(u"QPushButton {\n"
"	color: rgb(0, 0, 0);\n"
"		background-color: rgb(0, 170, 255);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0,0,0);\n"
"	background-color: rgb(252, 252, 0);\n"
"    border-radius:10px\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_alterar_2)

        self.btn_excluir_2 = QPushButton(self.frame_11)
        self.btn_excluir_2.setObjectName(u"btn_excluir_2")
        self.btn_excluir_2.setMinimumSize(QSize(120, 25))
        self.btn_excluir_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir_2.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"	background-color: rgb(0, 170, 255);\n"
"    border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 0, 0);\n"
"    border-radius:10px\n"
"}")

        self.verticalLayout_9.addWidget(self.btn_excluir_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.horizontalLayout_8.addWidget(self.frame_11)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_8.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastrar)
        self.pg_contato = QWidget()
        self.pg_contato.setObjectName(u"pg_contato")
        self.verticalLayout_10 = QVBoxLayout(self.pg_contato)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_6 = QFrame(self.pg_contato)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_6)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_12.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_12.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_6)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_12.addWidget(self.label_12)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_5)


        self.verticalLayout_10.addWidget(self.frame_6)

        self.Pages.addWidget(self.pg_contato)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_5 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_7 = QFrame(self.pg_sobre)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setSpacing(40)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(54, 0, 54, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(40, 0))
        self.frame_8.setMaximumSize(QSize(400, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(50, 0))
        self.label_13.setMaximumSize(QSize(400, 400))
        self.label_13.setPixmap(QPixmap(u":/icons/Icons/FS.png"))
        self.label_13.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(40, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.frame_10)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.label_8 = QLabel(self.pg_sobre)
        self.label_8.setObjectName(u"label_8")
        font6 = QFont()
        font6.setFamilies([u"Comic Sans MS"])
        font6.setPointSize(26)
        self.label_8.setFont(font6)

        self.verticalLayout_5.addWidget(self.label_8)

        self.label_9 = QLabel(self.pg_sobre)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_9)

        self.Pages.addWidget(self.pg_sobre)

        self.horizontalLayout_7.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.Main_Frame)

        self.Footer = QFrame(self.Main_Conteiner)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setFrameShape(QFrame.StyledPanel)
        self.Footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.Footer)
        self.label_2.setObjectName(u"label_2")
        font7 = QFont()
        font7.setFamilies([u"Comic Sans MS"])
        font7.setPointSize(12)
        self.label_2.setFont(font7)

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.Footer)


        self.gridLayout_6.addWidget(self.Main_Conteiner, 0, 1, 1, 1)

        self.Left_Conteiner = QFrame(self.centralwidget)
        self.Left_Conteiner.setObjectName(u"Left_Conteiner")
        self.Left_Conteiner.setMaximumSize(QSize(9, 16777215))
        self.Left_Conteiner.setFrameShape(QFrame.StyledPanel)
        self.Left_Conteiner.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Left_Conteiner)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, -1, 0, -1)
        self.frame = QFrame(self.Left_Conteiner)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font8 = QFont()
        font8.setFamilies([u"Comic Sans MS"])
        font8.setPointSize(10)
        self.label_3.setFont(font8)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.Left_Conteiner)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, -1, 0, -1)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy2)
        self.toolBox.setMinimumSize(QSize(0, 0))
        self.toolBox.setMaximumSize(QSize(250, 16777215))
        self.toolBox.setFont(font7)
        self.toolBox.setLayoutDirection(Qt.LeftToRight)
        self.toolBox.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(65,65,65)\n"
"\n"
"}\n"
"\n"
"QToolBox{\n"
"text-algin: left;\n"
"	background-color: rgb(187, 231, 255);\n"
"\n"
"}\n"
"\n"
"QToolBox::tab{ \n"
"	Border-radius:5px;\n"
"	background-color: rgb(194,232,255);\n"
"	text-algin: left;\n"
"\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 98, 427))
        self.page.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 4, 0, 0)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font9 = QFont()
        font9.setFamilies([u"Comic Sans MS"])
        font9.setPointSize(15)
        self.btn_home.setFont(font9)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(239, 78, 69);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"    border-radius:15px\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.page)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font9)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(252, 227, 36);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(252, 252, 0);\n"
"    border-radius:15px\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_cadastrar)

        self.btn_contato = QPushButton(self.page)
        self.btn_contato.setObjectName(u"btn_contato")
        self.btn_contato.setMinimumSize(QSize(0, 30))
        self.btn_contato.setFont(font9)
        self.btn_contato.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_contato.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(113, 191, 79);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(38, 255, 0);\n"
"    border-radius:15px\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_contato)

        self.btn_sobre = QPushButton(self.page)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setFont(font9)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(108, 97, 169);\n"
"    border-radius:15px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: rgb(255, 255, 255);\n"
"	background-color: rgb(83, 0, 116);\n"
"    border-radius:15px\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Painel de controle:")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 211, 427))
        self.page_2.setStyleSheet(u"background-color: rgb(194, 232, 255);")
        self.horizontalLayout_5 = QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.toolBox.addItem(self.page_2, u"Informa\u00e7\u00f5es adicionais:")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.gridLayout_6.addWidget(self.Left_Conteiner, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Cadastro CEAI", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de cadastro", None))
        self.lbl_logo_login_2.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">ALUNO:</span></p></body></html>", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do Aluno", None))
        self.txt_serie.setPlaceholderText(QCoreApplication.translate("MainWindow", u"S\u00e9rie/ Ano", None))
        self.txt_nascimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
        self.txt_naturalidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Naturalidade", None))
        self.txt_nacionalidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nacionalidade", None))
        self.txt_telefone_aluno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone para contato", None))
        self.txt_pai.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome do Pai", None))
        self.txt_mae.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome da M\u00e3e", None))
        self.txt_rg_aluno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG Da crian\u00e7a", None))
        self.txt_cpf_aluno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF Da crian\u00e7a", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.txt_bairro_aluno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_cidade_aluno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.txt_professora.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Professora", None))
        self.txt_turma.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Turma", None))
        self.txt_email_aluno.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.txt_alergia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"A crian\u00e7a \u00e9 portadora de alguma alergia? Qual?", None))
        self.btn_cadastrar_aluno_2.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_aluno), QCoreApplication.translate("MainWindow", u"Cadastrar Aluno(a)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">PROFESSOR (A)</p></body></html>", None))
        self.txt_nome_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome ", None))
        self.txt_nascimento_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
        self.txt_naturalidade_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Naturalidade", None))
        self.txt_nacionalidade_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nacionalidade", None))
        self.txt_telefone_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_rg_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.txt_cpf_prof_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.txt_cep_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_endereco_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.txt_bairro_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.txt_cidade_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.txt_disciplinas_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leciona as disciplinas: ", None))
        self.txt_turma_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Leciona a turma: ", None))
        self.txt_email_prof.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.btn_cadastrar_professor_3.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_professor), QCoreApplication.translate("MainWindow", u"Cadastrar Professor(a)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Turmas</p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"S\u00e9rie/Ano", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nascimento", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Pai", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"M\u00e3e", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Naturalidade", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nacionalidade", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Turma", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Alergia", None));
        self.btn_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Pesquisar: ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_turma), QCoreApplication.translate("MainWindow", u"Turmas", None))
        ___qtablewidgetitem15 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem16 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"S\u00e9rie/Ano", None));
        ___qtablewidgetitem17 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Nascimento", None));
        ___qtablewidgetitem18 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Pai", None));
        ___qtablewidgetitem19 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"M\u00e3e", None));
        ___qtablewidgetitem20 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem21 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem22 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Naturalidade", None));
        ___qtablewidgetitem23 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Nacionalidade", None));
        ___qtablewidgetitem24 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem25 = self.tableWidget_2.horizontalHeaderItem(10)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem26 = self.tableWidget_2.horizontalHeaderItem(11)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem27 = self.tableWidget_2.horizontalHeaderItem(12)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem28 = self.tableWidget_2.horizontalHeaderItem(13)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Turma", None));
        ___qtablewidgetitem29 = self.tableWidget_2.horizontalHeaderItem(14)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Alergia", None));
        self.btn_excel_2.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar_2.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir_2.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Docentes", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/Icons/whatsApp.png\"/><span style=\" font-size:18pt; vertical-align:super;\"> (75) 99213-1117</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/Icons/Gmail.png\"/><span style=\" font-size:18pt; vertical-align:super;\">fabiososantos2@gmail.com</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/Icons/Instagram.png\"/><span style=\" font-size:18pt; vertical-align:super;\">_fabiosooares_</span></p></body></html>", None))
        self.label_13.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SOBRE</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Este sistema de cadastro foi desenvolvido com o intuito de simplificar o cadastro de novos alunos no Centro Educacional Arco-\u00edris (CEAI), sendo assim, o mesmo possibilitar\u00e1 que o mesmo servi\u00e7o de antes seja realizado com mais praticidade e menos tempo. O desenvolvedor F\u00e1bio Soares, Profissional da \u00e1rea de an\u00e1lise e desenvolvimento de sistemas realizou todo o processo de cria\u00e7\u00e3o do sistema, d\u00eas de a cria\u00e7\u00e3o das telas at\u00e9 a implementa\u00e7\u00e3o do banco de dados que aqui foi utilizado. </span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Powed By: F\u00e1bio Soares", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Powed By: F\u00e1bio Soares", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar ", None))
        self.btn_contato.setText(QCoreApplication.translate("MainWindow", u"Contato", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Painel de controle:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#001e36;\">Usu\u00e1rio: Arco-\u00edris</span></p><p align=\"center\"><span style=\" color:#001e36;\">Sistema: Cadastro de alunos</span></p><p align=\"center\"><span style=\" color:#001e36;\">Status: Ativo</span></p><p align=\"center\"><span style=\" color:#001e36;\">Desenvolvedor: F\u00e1bio Soares</span></p><p align=\"center\"><span style=\" color:#001e36;\"><br/></span></p><p align=\"center\"><span style=\" color:#001e36;\">Version -- 1.0</span></p><p align=\"center\"><span style=\" color:#001e36;\"><br/></span></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es adicionais:", None))
    # retranslateUi

