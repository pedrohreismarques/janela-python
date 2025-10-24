# Importar o pacote sys(sistema) para o sistema operacional gerenciar a nossa janela e permitir com que ela entre em serviços.
import sys

# Importar a biblioteca PyQt5 5.widgets
# Essa biblioteca tem vários controles para usarmos na nossa janela.
# São eles:
# - QApplication -> Permite abrir e exibir a janela 
# - Q widget -> A estrutura da janela, com os elementos
#       - barra de título, maximizar, minimizar, e fechar
# - QLabel -> Um rótulo, ou seja, um texto simples de apresentação
# - QLineEdit -> Uma caixa de texto
# - QPushButton -> Um botão para clicar
# - QVBoxLayout -> Utilizado para organizar os elementos
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QComboBox

# Importar uma  nova biblioteca para trabalhar com imagens
# Vamos usar o controle chamado QPixmap do pacote GUI
from PyQt5.QtGui import QPixmap

# Iniciar a construção da janela usando como base o controle QWidget.
# Ele possui aas configurações iniciais de uma janela
class CadastroProduto(QWidget):
    # Para iniciar a janela, iremos usar a função chamada __init__, que irá inicializar a nossa janela
    # O temor self é um reflexo qeu trata da própria classe, neste CadastroProduto
    def __init__(self):
        super().__init__()

        # Define o texto que aparece na barra de título
        self.setWindowTitle("Cadastro de Produtos")

        #  Definir a posição inicial da nossa janela.
        # Iremos setar valoers para x e y e, também as dimensões largaura e altura
        self.setGeometry(100,100,800,800)
        self.setFixedWidth(700)

        # Vamos criar duas labels que representarão as partes superior, onde ficará a imagem, e a parte inferior, onde ficará os controles.
        self.superior_label = QLabel()
        self.superior_label.setPixmap(QPixmap(".venv/loja.jpg"))
        self.superior_label.setScaledContents(True)
        
        # Ajustar a altura da label
        self.superior_label.setFixedHeight(400)

        self.inferior_label = QLabel()
        self.inferior_label.setStyleSheet("QLabel{background-color: #F5DC6B}")

        self.nome_label = QLabel("Nome do produto:")
        self.nome_label.setStyleSheet("QLabel{font-size:15pt}")
        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.tipo_label = QLabel("Selecione o tipo de produto:")
        self.tipo_label.setStyleSheet("QLabel{font-size:15pt}")
        self.tipo_combo = QComboBox()
        self.tipo_combo.setStyleSheet("QComboBox{font-size:15pt}")
        self.tipo_combo.addItem("Informática")
        self.tipo_combo.addItem("Vestuário")
        self.tipo_combo.addItem("Alimentos")
        self.tipo_combo.addItem("Floricultura")
        self.tipo_combo.addItem("Papelaria")
        self.tipo_combo.addItem("Livraria")

        self.descricao_label = QLabel("Descrição do produto")
        self.descricao_label.setStyleSheet("QLabel{font-size:15pt}")
        self.descricao_edit = QLineEdit()
        self.descricao_edit.setStyleSheet("QLineEdit{font-size:15pt}")
        self.descricao_edit.setFixedHeight(100)

        self.preco_label = QLabel("Preço do produto")
        self.preco_label.setStyleSheet("QLabel{font-size:15pt}")
        self.preco_edit = QLineEdit()
        self.preco_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.gravar_botao = QPushButton("Gravar")
        self.gravar_botao.setStyleSheet("QPushButton{font-size:15pt; background-color: red; color:white}")
        
        # Adicionar ao botão gravar um comando de acionamento, pois quando este botão for clicado ele chamará uma função
        # que executará a gravação dos dados do produto em um arquivo de texto
        self.gravar_botao.clicked.connect(self.gravar)

        # Organizar estes controles em um layout vertical
        self.v_controles = QVBoxLayout()

        self.v_controles.addWidget(self.nome_label)
        self.v_controles.addWidget(self.nome_edit)
        self.v_controles.addWidget(self.tipo_label)
        self.v_controles.addWidget(self.tipo_combo)
        self.v_controles.addWidget(self.descricao_label)
        self.v_controles.addWidget(self.descricao_edit)
        self.v_controles.addWidget(self.preco_label)
        self.v_controles.addWidget(self.preco_edit)
        self.v_controles.addWidget(self.gravar_botao)

        # Adicionar os controles na parte inferior
        self.inferior_label.setLayout(self.v_controles)

        # Vamos criar um controle de layout vertical para dispor as labels superior e inferior
        # uma abaixo da outra respectivamente
        self.v_layout = QVBoxLayout()

        self.v_layout.addWidget(self.superior_label)
        self.v_layout.addWidget(self.inferior_label)

        # Adicionar o layout organizado na janela
        self.setLayout(self.v_layout)
    
    def gravar(self):
        arquivo = open("cadastro.txt","a",encoding="utf8")
        arquivo.write("----------------------------------------\n")
        arquivo.write(f"Produto: {self.nome_edit.text()}\n")
        arquivo.write(f"Tipo: {self.tipo_combo.currentText()}\n")
        arquivo.write(f"Descrição: {self.descricao_edit.text()}\n")
        arquivo.write(f"Preço: R$ {self.preco_edit.text()}\n\n")
        arquivo.write("----------------------------------------\n")

        arquivo.close()



# Vamos vincular o funcionamento da janela com o gerenciamento do sistema operacional.
# Assim o sistema operacional saberá lidar lidar com a janela em memória.
app = QApplication(sys.argv)
# instância da janela para por em funcionamento
janela = CadastroProduto()
# exibir a janela na tela
janela.show()
# executar a janela
app.exec_()