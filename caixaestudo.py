import sys
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton

class caixa(QWidget):
    
    def __init__(self):

        super().__init__()

        self.setGeometry(50,50,1200,800)

        self.esquerda = QLabel()
        self.esquerda.setStyleSheet("QLabel{background-color:blue}")

        
        #criar os elementos que irão para a coluna da esquerda

        #criar uma label para adicionar uma imagem e DEPOIS adicionar a coluna da esquerda

        self.imagem_label = QLabel()
        self.imagem_label.setPixmap(QPixmap(".venv/imagens/logopadaria.png"))
        self.imagem_label.setScaledContents(True)
        self.imagem_label.setFixedSize(600,300)
        
        self.codigo_produto_label = QLabel("código do produto:")


        # adicionar os elementos que ficaram ao lado esquerdo a um layout vertical que sera aplicado na coluna da esquerda

        self.vertical_esquerda_layout = QVBoxLayout()
        self.vertical_esquerda_layout.addWidget(self.imagem_label)
        self.vertical_esquerda_layout.addWidget(self.codigo_produto_label)

        self.esquerda.setLayout(self.vertical_esquerda_layout)
        self.direita = QLabel()
        self.direita.setStyleSheet("QLabel{background-color:yellow}")

        self.horizontal = QHBoxLayout()

        #adicionar a coluna da esquerda no layout horizontal

        self.horizontal.addWidget(self.esquerda)
        self.horizontal.addWidget(self.direita)

        #adicionar o layout horizontal na tela

        self.setLayout(self.horizontal)

Ap = QApplication(sys.argv)
j = caixa()
j.show()
Ap.exec_()