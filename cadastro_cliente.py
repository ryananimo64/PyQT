from PyQt5.QtWidgets import QWidget,QLabel,QBoxLayout,QVBoxLayout,QHBoxLayout,QApplication,QLineEdit,QPushButton
import sys 

class CadastroCliente(QWidget):
    def __init__(self):
        super().__init__()

        #Vamos configurar a geometria da
        #tela. setandos  valores  de x e y
        #além  de largura e altura
        self.setGeometry(10,30,800,600)

        # Texto para barra de Título
        self.setWindowTitle("Cadastrar Cliente")

        # gerenciador de leyout vertical
        self.layout_v = QVBoxLayout()

        # labels para os dados do cliente 
        self.label_nome = QLabel("Nome Do Cliente: ")
        self.label_nome.setStyleSheet("QLabel{font-size:20pt}")

        # LineEdit para o nome do cliente
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12pt}")

        # adicionar a lebel nome  e o lineedit ao
        # layout vertical
        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)

        # Email
        self.label_email = QLabel("Email do Cliente: ")
        self.label_email.setStyleSheet("QLabel {font-size:22pt}")

        self.edit_email =  QLineEdit()
        self.edit_email.setStyleSheet("QLineEdit{font-size:12pt}")

        self.layout_v.addWidget(self.label_email)
        self.layout_v.addWidget(self.edit_email)

        # Telefone
        self.label_telefone = QLabel("Telefone do Cliente: ")
        self.label_telefone.setStyleSheet("QLabel{font-size:22pt}")

        self.edit_telefone = QLineEdit()
        self.edit_telefone.setStyleSheet("QLineEdit {font-size:22pt}")

        self.layout_v.addWidget(self.label_telefone)
        self.layout_v.addWidget(self.edit_telefone)

        # Idade
        self.label_idade = QLabel("Idade do Cliente: ")
        self.label_idade.setStyleSheet("QLabel{font-size:22pt}")

        self.edit_idade = QLineEdit()
        self.edit_idade.setStyleSheet("QLineEdit {font-size:22pt}")

        self.layout_v.addWidget(self.label_idade)
        self.layout_v.addWidget(self.edit_idade)

        #BUTÂO
        self.botao = QPushButton("Cadastrar")
        self.botao.setStyleSheet("QPushButton{background-color:red;color:white;font-size:12pt;font-weight:bold}")

        self.layout_v.addWidget(self.botao)

        # adicionar o layout v a tela
        self.setLayout(self.layout_v)



app = QApplication(sys.argv)
#instância da classe Cadastrocliente
# para inicia a janela
tela = CadastroCliente()
#exibir a tela durante a execução
tela.show()
# ao clicar no butão fechar a tela 
# deve fechar e sair da memoria
app.exec() 
