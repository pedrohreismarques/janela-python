import sys
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton

class CadastroClientes(QWidget):
    def __init__(self):
        super ().__init__()

        self.setWindowTitle("Cadastro de Cliente")
        self.setGeometry(50,50,1400,800)
        self.setFixedSize(1400,800)

        self.setWindowIcon(QIcon(".venv/icon.png"))

        self.horizontal_layout = QHBoxLayout()
        self.esquerda_label = QLabel()
        self.esquerda_label.setPixmap(QPixmap(".venv/janela.jpg"))
        self.esquerda_label.setScaledContents(True)

        self.direita_label = QLabel()
        self.direita_label.setFixedWidth(400)
        self.direita_label.setStyleSheet("QLabel{background-color:#162223}")

        self.vertical_layout = QVBoxLayout()
        self.titulo_label = QLabel("Cadastro de Cliente")
        self.titulo_label.setStyleSheet("QLabel{font-family:Playbill; font-size:60pt; color:white}")
        self.vertical_layout.addWidget(self.titulo_label)

        # ----------------- Nome do Cliente -------------------------------- 
        self.nome_label = QLabel("Nome completo:")
        self.nome_label.setStyleSheet("QLabel{font-family:corbel; font-size:15pt; color:white}")

        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{font-size:15pt; color:black}")

        self.vertical_layout.addWidget(self.nome_label)
        self.vertical_layout.addWidget(self.nome_edit)
        # ---------------- Fim do Nome do CLiente --------------------------

        # -------------------- Gênero --------------------------------------
        self.genero_label = QLabel("Gênero:")
        self.genero_label.setStyleSheet("QLabel{font-family:corbel; font-size:15pt; color:white}")
        
        self.genero_combo = QComboBox()
        self.genero_combo.setStyleSheet("QComboBox{font-family:corbel; font-size:15pt; color:black}")
        self.genero_combo.addItem("Masculino")
        self.genero_combo.addItem("Feminino")
        self.genero_combo.addItem("Indefinido")
        self.genero_combo.addItem("Prefiro não informar")

        self.vertical_layout.addWidget(self.genero_label)
        self.vertical_layout.addWidget(self.genero_combo)

        # -------------------- Fim do Gênero -------------------------------

        # ----------------- CPF -------------------------------------------- 
        self.cpf_label = QLabel("CPF:")
        self.cpf_label.setStyleSheet("QLabel{font-family:corbel; font-size:15pt; color:white}")

        self.cpf_edit = QLineEdit()
        self.cpf_edit.setStyleSheet("QLineEdit{font-size:15pt; color:black}")

        self.vertical_layout.addWidget(self.cpf_label)
        self.vertical_layout.addWidget(self.cpf_edit)
        # ---------------- Fim do CPF --------------------------------------
        
        # ----------------- Data de Nascimento -----------------------------
        self.nascimento_label = QLabel("Data de Nascimento:")
        self.nascimento_label.setStyleSheet("QLabel{font-family:corbel; font-size:15pt; color:white}")

        self.nascimento_edit = QLineEdit()
        self.nascimento_edit.setStyleSheet("QLineEdit{font-size:15pt; color:black}")

        self.vertical_layout.addWidget(self.nascimento_label)
        self.vertical_layout.addWidget(self.nascimento_edit)
        # ---------------- Fim da Data de Nascimento ------------------------

        # -------------------- Email ----------------------------------------
        self.email_label = QLabel("Email:")
        self.email_label.setStyleSheet("QLabel{font-family:corbel; font-size:15pt; color:white}")

        self.email_edit = QLineEdit()
        self.email_edit.setStyleSheet("QLineEdit{font-size:15pt; color:black}")

        self.vertical_layout.addWidget(self.email_label)
        self.vertical_layout.addWidget(self.email_edit)
        # -------------------- Fim do Email ---------------------------------

        # -------------------- Telefone -------------------------------------
        self.telefone_label = QLabel("Telefone:")
        self.telefone_label.setStyleSheet("QLabel{font-family:corbel; font-size:15pt; color:white}")

        self.telefone_edit = QLineEdit()
        self.telefone_edit.setStyleSheet("QLineEdit{font-size:15pt; color:black}")

        self.vertical_layout.addWidget(self.telefone_label)
        self.vertical_layout.addWidget(self.telefone_edit)
        # -------------------- Fim do Telefone -------------------------------

         # -------------------- Endereço -------------------------------------
        self.endereco_label = QLabel("Endereço:")
        self.endereco_label.setStyleSheet("QLabel{font-family:corbel; font-size:15pt; color:white}")

        self.endereco_edit = QLineEdit()
        self.endereco_edit.setStyleSheet("QLineEdit{font-size:15pt; color:black}")

        self.vertical_layout.addWidget(self.endereco_label)
        self.vertical_layout.addWidget(self.endereco_edit)
        # -------------------- Fim do Endereço -------------------------------

        # --------------------- Botão Cadastrar ------------------------------
        self.botao_cadastrar = QPushButton("Cadastrar")
        self.botao_cadastrar.setStyleSheet("QPushButton{font-family:corbel; font-size:15pt; background-color:#9AB2E3; color:black}")
        
        self.vertical_layout.addWidget(self.botao_cadastrar)
        # --------------------- Fim do Botão Cadastrar -----------------------

        self.direita_label.setLayout(self.vertical_layout)

        self.horizontal_layout.addWidget(self.esquerda_label)
        self.horizontal_layout.addWidget(self.direita_label)
        
        self.setLayout(self.horizontal_layout)

        self.botao_cadastrar.clicked.connect(self.cadastrar)

    def cadastrar(self):
        arquivo = open("cadastro_cliente.txt","a",encoding="utf8")
        
        arquivo.write("----------------------------------------\n")
        arquivo.write(f"NOME: {self.nome_edit.text()}\n")
        arquivo.write(f"GÊNERO: {self.genero_combo.currentText()}\n")
        arquivo.write(f"CPF: {self.cpf_edit.text()}\n")
        arquivo.write(f"DATA DE NASCIMENTO: {self.nascimento_edit.text()}\n")
        arquivo.write(f"EMAIL: {self.email_edit.text()}\n")
        arquivo.write(f"TELEFONE: {self.telefone_edit.text()}\n")
        arquivo.write(f"ENDEREÇO: {self.endereco_edit.text()}\n")
        arquivo.write("----------------------------------------")

        arquivo.close()

app = QApplication(sys.argv)
janela = CadastroClientes()
janela.show()
app.exec_()