from turtle import width
from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMessageBox, QMainWindow, QMessageBox, QTableWidgetItem)
from ui_main import Ui_MainWindow
import sys
from database import Data_base

class MainWindow(QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CEAI - Sistema de Cadastro de alunos")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)
    
    
        ################################
        #         Toggle button        #
        ####################################################
        self.btn_toggle.clicked.connect(self.leftConteiner)
        ####################################################
        #      Páginas do sistema      #
        ############################################################################################
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastrar))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        ############################################################################################
        #        Página cadastrar      #
        ################################
        self.btn_cadastrar_aluno_2.clicked.connect(self.cadastrarAlunos)
        
        
    
    def leftConteiner(self):
        
        width = self.Left_Conteiner.width()
        
        if width == 9:
            newWidth = 232
        else: 
            newWidth = 9
            
        self.animation = QtCore.QPropertyAnimation(self.Left_Conteiner, b'maximumWidth')
        self.animation.setDuration(1500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutBack)
        self.animation.start()
        
    def cadastrarAlunos(self):
        db = Data_base()
        db.connect()
        
        fullDataSet = (
            
            self.txt_cpf_aluno.text(), self.txt_nome.text(), self.txt_serie.text(), self.txt_nascimento.text(), 
            self.txt_naturalidade.text(), self.txt_nacionalidade.text(), self.txt_telefone_aluno.text(), self.txt_pai.text(), 
            self.txt_mae.text(), self.txt_rg_aluno.text(), self.txt_cpf_aluno.text(), self.txt_cep.text(), self.txt_endereco.text(), 
            self.txt_bairro_aluno.text(), self.txt_cidade_aluno.text(), self.txt_professora.text(), self.txt_turma.text(), 
            self.txt_email_aluno.text(), self.txt_alergia.text(), )
            
            #############################
            #Cadastrar no banco de dados#
            #############################
        resp = db.register_alunos(fullDataSet)
        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Casdastro Realizado")
            msg.setText("Cadastro Realizado com sucesso  ;) ")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar =(  Verifique se as informações foram preenchidadas corretamente!")
            msg.exec()
            db.close_connection()
            return
        
    
        
if __name__ == "__main__":
    db = Data_base()
    #db.connect()
    
    #db.create_tab_turmas
    #db.close_connection()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    app.exec()