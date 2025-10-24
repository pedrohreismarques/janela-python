import sys
import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon, QKeySequence
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QInputDialog, QShortcut

class CadastroMercado(QWidget):

    def __init__(self):
        super().__init__()

        self.total = 0.0
        self.linha = 0

        self.setWindowTitle("Cadastro de Produtos")
        self.setGeometry(50, 50, 1400, 800)
        self.setFixedSize(1400, 800)
        self.setWindowIcon(QIcon(".venv/icon.png"))

        self.horizontal_layout = QHBoxLayout()

        # ---- ESQUERDO ----
        self.esquerda_widget = QWidget()
        self.esquerda_widget.setFixedWidth(500)
        self.esquerda_widget.setStyleSheet("background-color: #E60701")
        self.vertical_layout = QVBoxLayout()  # layout principal do formulário

        # ===== IMAGEM =====
        self.imagem_label = QLabel()
        self.imagem_label.setPixmap(QPixmap(".venv/extra.png"))
        self.imagem_label.setScaledContents(True) 
        self.imagem_label.setFixedSize(450, 300) 
        self.vertical_layout.addWidget(self.imagem_label)
        # ========================================

        # ---- FORMULÁRIO ----
        self.codigo_label = QLabel("Código do produto:")
        self.codigo_label.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.codigo_edit = QLineEdit()
        self.codigo_edit.setStyleSheet("background-color: white; font-size: 14pt;")
        self.codigo_edit.setFixedHeight(30)
        self.vertical_layout.addWidget(self.codigo_label)
        self.vertical_layout.addWidget(self.codigo_edit)

        self.tipo_label = QLabel("Tipo do produto:")
        self.tipo_label.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.tipo_combo = QComboBox()
        self.tipo_combo.setFixedHeight(30)
        self.tipo_combo.setStyleSheet("QComboBox{color:white; font-size:15pt}")
        self.tipo_combo.addItems(["Pães", "Frios", "Bebidas", "Laticínios", "Limpeza", "Petshop", "Beleza", "Congelados", "Não Perecíveis"])
        self.vertical_layout.addWidget(self.tipo_label)
        self.vertical_layout.addWidget(self.tipo_combo)

        self.descricao_label = QLabel("Descrição do produto:")
        self.descricao_label.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.descricao_edit = QLineEdit()
        self.descricao_edit.setStyleSheet("background-color: white; font-size: 14pt;")
        self.descricao_edit.setFixedHeight(80)
        self.vertical_layout.addWidget(self.descricao_label)
        self.vertical_layout.addWidget(self.descricao_edit)

        self.quantidade_label = QLabel("Quantidade do produto:")
        self.quantidade_label.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.quantidade_edit = QLineEdit()
        self.quantidade_edit.setStyleSheet("background-color: white; font-size: 14pt;")
        self.quantidade_edit.setFixedHeight(30)
        self.vertical_layout.addWidget(self.quantidade_label)
        self.vertical_layout.addWidget(self.quantidade_edit)

        self.preco_label = QLabel("Preço unitário:")
        self.preco_label.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.preco_edit = QLineEdit()
        self.preco_edit.setStyleSheet("background-color: white; font-size: 15pt;")
        self.preco_edit.setFixedHeight(30)
        self.vertical_layout.addWidget(self.preco_label)
        self.vertical_layout.addWidget(self.preco_edit)

        self.sub_label = QLabel("Sub-Total:")
        self.sub_label.setStyleSheet("QLabel{color:white; font-size:15pt}")
        self.sub_edit = QLineEdit("Tecle F2 para calcular o sub-total")
        self.sub_edit.setEnabled(False)
        self.sub_edit.setStyleSheet("QLineEdit{background-color:white;font-size:15pt}")
        self.vertical_layout.addWidget(self.sub_label)
        self.vertical_layout.addWidget(self.sub_edit)

        self.esquerda_widget.setLayout(self.vertical_layout)

        # ---- DIREITO + TABELA (LAYOUT) ----
        self.direita_widget = QWidget()
        self.direita_layout = QVBoxLayout()

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(6)
        self.tabela.setRowCount(10)
        self.tabela.setHorizontalHeaderLabels(["Código", "Tipo", "Descrição", "Quantidade", "Preço Unitário", "Preço Total"])

        self.direita_layout.addWidget(self.tabela)
        self.direita_widget.setLayout(self.direita_layout)

        self.total_label = QLabel("Preço Total:")
        self.total_label.setStyleSheet("font-size: 16pt; font-weight: bold;")

        self.total_edit = QLineEdit()
        self.total_edit.setStyleSheet("background-color: white; font-size: 14pt; padding: 5px;")

        self.direita_layout.addWidget(self.total_label)
        self.direita_layout.addWidget(self.total_edit)

        # ---- ADICIONAR OS DOIS LADOS NA JANELA ----
        self.horizontal_layout.addWidget(self.esquerda_widget)
        self.horizontal_layout.addWidget(self.direita_widget)
        self.setLayout(self.horizontal_layout)

    # ---- FUNÇÃO PARA CÁLCULO DE SUBTOTAL ----
        self.keyPressEvent = self.captura_tecla
    
    def captura_tecla(self, e):
        
        if(e.key()==Qt.Key_F2):
            self.sub_edit.setText(str(float(self.quantidade_edit.text()) * float(self.preco_edit.text())))

        elif(e.key()==Qt.Key_F3):
            print(self.codigo_edit.text())
            self.tabela.setItem(self.linha,0,QTableWidgetItem(self.codigo_edit.text()))

            print(self.tipo_combo.currentText())
            self.tabela.setItem(self.linha,1,QTableWidgetItem(self.tipo_combo.currentText()))

            print(self.descricao_edit.text())
            self.tabela.setItem(self.linha,2,QTableWidgetItem(self.descricao_edit.text()))

            print(self.quantidade_edit.text())
            self.tabela.setItem(self.linha,3,QTableWidgetItem(self.quantidade_edit.text()))

            print(self.preco_edit.text())
            self.tabela.setItem(self.linha,4,QTableWidgetItem(self.preco_edit.text()))

            print(self.sub_edit.text())
            self.tabela.setItem(self.linha,5,QTableWidgetItem(self.sub_edit.text()))

            self.linha = self.linha + 1
            self.total = self.total + float(self.sub_edit.text())

            self.total_edit.setText(str(self.total))

        elif(e.key()==Qt.Key_F4):
            op = QMessageBox.question(self, "Pagamento","Deseja efetuar o pagamento?")

            if op == QMessageBox.Yes:

                rs,ok = QInputDialog().getText(self,"Forma Pagamento","Escolha uma forma de Pagamento:\n1 - Pix\n2 - Cartão de Crédito\n3 - Cartão de Débito\n4 - Dinheiro\n5 - Voucher")

                if ok:

                    #Vamos criar uma lista (array) para guardar todos os dados da tabela para criar uma nota fiscal

                    dados = []

                    for linha in range (self.tabela.rowCount()):
                    
                       dados_linha = []

                       for coluna in range (self.tabela.columnCount()):

                            item = self.tabela.item(linha, coluna)

                            if item:

                                dados_linha.append(item.text())

                            else: 

                                break
                            
                                #dados_linha.append("")

                    dados.append(dados_linha)

                    nota = """
<html>
<head>
<title> Nota fiscal </title>

<style>

    body {

    text-align:center;
    }


    table{

    margin-left:auto;
    margin-right:auto;
    border:1px solid black;


    }

</style>

</head>
<body>

<h1>Nota Fiscal de Compra</h1>

<table>

<tr>

    <th>Cód.</th>
    <th>Nome</th>
    <th>Desc.</th>
    <th>Qtd.</th>
    <th>Preço</th>
    <th>Preço total</th>

</tr>

"""
                    for lin in dados:

                        nota = nota + "<tr>"
                        
                        for col in lin:

                            nota = nota+ "<td>"+col+"</td>"
                        
                        nota = nota + "</tr>"

                    nota = nota + """

<tr>

    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>

</tr>

</table>

</body>
</html>
                            """
                    
                    arq = open ("nota.html","w")
                    arq.write(nota)
                    arq.close()
                    webbrowser.open("nota.html")

            else:

                #vamos criar uma lista(array) para guardar todos os dados da tabela para criar uma nota fiscal

                dados = []

                for linha in range (self.tabela.rowCount()):
                    
                    dados_linha = []

                    for coluna in range (self.tabela.columnCount()):

                        item = self.tabela.item(linha, coluna)

                        if item:

                            dados_linha.append(item.text())

                        else: 

                            break
                            
                            #dados_linha.append("")

                    dados.append(dados_linha)
                print(dados)


app = QApplication(sys.argv)
janela = CadastroMercado()
janela.show()
app.exec_()