import sys 
from  PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


class TabelaProdutos (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabela de Produtos")

        self.setGeometry(100,100,1000,500)

        self.vertical_layout = QVBoxLayout()

        self.tabela = QTableWidget ()
        self.tabela.setColumnCount(7)
        self.tabela.setRowCount(5)
        colunas = ["Código", "Produto","Tipo", "Fabricante", "Quantidade", "Preço", "Total"]

        self.tabela.setHorizontalHeaderLabels(colunas)


        self.tabela.setItem(0,0, QTableWidgetItem ("001"))
        self.tabela.setItem(0,1, QTableWidgetItem ("Mouse"))
        self.tabela.setItem(0,2, QTableWidgetItem ("Informática"))
        self.tabela.setItem(0,3, QTableWidgetItem ("Logitech"))
        self.tabela.setItem(0,4, QTableWidgetItem ("10"))
        self.tabela.setItem(0,5, QTableWidgetItem ("R$ 50,00"))
        self.tabela.setItem(0,6, QTableWidgetItem ("R$ 500,00"))

        self.tabela.setItem(1,0, QTableWidgetItem ("002"))
        self.tabela.setItem(1,1, QTableWidgetItem ("Teclado"))
        self.tabela.setItem(1,2, QTableWidgetItem ("Informática"))
        self.tabela.setItem(1,3, QTableWidgetItem ("Logitech"))
        self.tabela.setItem(1,4, QTableWidgetItem ("50"))
        self.tabela.setItem(1,5, QTableWidgetItem ("R$ 150,00"))
        self.tabela.setItem(1,6, QTableWidgetItem ("R$ 7.520,00"))


        self.tabela.setItem(2,0, QTableWidgetItem ("003"))
        self.tabela.setItem(2,1, QTableWidgetItem ("Extrato de Tomate"))
        self.tabela.setItem(2,2, QTableWidgetItem ("Alimento"))
        self.tabela.setItem(2,3, QTableWidgetItem ("Cargill"))
        self.tabela.setItem(2,4, QTableWidgetItem ("20"))
        self.tabela.setItem(2,5, QTableWidgetItem ("R$ 10,00"))
        self.tabela.setItem(2,6, QTableWidgetItem ("R$ 200,00"))


        self.tabela.setItem(3,0, QTableWidgetItem ("004"))
        self.tabela.setItem(3,1, QTableWidgetItem ("Esmalte"))
        self.tabela.setItem(3,2, QTableWidgetItem ("Beleza"))
        self.tabela.setItem(3,3, QTableWidgetItem ("Risque"))
        self.tabela.setItem(3,4, QTableWidgetItem ("50"))
        self.tabela.setItem(3,5, QTableWidgetItem ("R$ 5,00"))
        self.tabela.setItem(3,6, QTableWidgetItem ("R$ 250,00"))

        self.tabela.setItem(4,0, QTableWidgetItem ("005"))
        self.tabela.setItem(4,1, QTableWidgetItem ("Bom Ar"))
        self.tabela.setItem(4,2, QTableWidgetItem ("Limpeza"))
        self.tabela.setItem(4,3, QTableWidgetItem ("Bom Ar"))
        self.tabela.setItem(4,4, QTableWidgetItem ("10"))
        self.tabela.setItem(4,5, QTableWidgetItem ("R$ 50,00"))
        self.tabela.setItem(4,6, QTableWidgetItem ("R$ 500,00"))



        self.vertical_layout.addWidget(self.tabela)
        self.setLayout(self.vertical_layout)



app = QApplication(sys.argv)
janela = TabelaProdutos()
janela.show()
app.exec_()








