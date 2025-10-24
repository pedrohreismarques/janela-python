import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QLabel, QCheckBox, QSpacerItem,
                             QSizePolicy)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt, QSize

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(600, 800)
        self.setup_ui()
        self.set_styles()

    def setup_ui(self):
        # ----- LAYOUT PRINCIPAL VERTICAL -----
        
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ----- LAYOUT PRINCIPAL SUPERIOR -----
        
        top_container = QWidget()
        top_container_layout = QVBoxLayout(top_container)
        top_container_layout.setAlignment(Qt.AlignCenter)
        top_container_layout.setContentsMargins(50, 80, 50, 50)
        top_container_layout.setSpacing(20)

        # ----- TÍTULO -----
        
        title_label = QLabel("Welcome to email")
        title_label.setFont(QFont("Arial", 24))
        title_label.setAlignment(Qt.AlignCenter)
        top_container_layout.addWidget(title_label)

        # ----- SUBTÍTULO -----
        
        subtitle_label = QLabel("Please login to your account")
        subtitle_label.setFont(QFont("Arial", 12))
        subtitle_label.setAlignment(Qt.AlignCenter)
        top_container_layout.addWidget(subtitle_label)

        # ----- ESPAÇADOR VERTICAL -----
        
        top_container_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # ----- EMAIL -----

        email_label = QLabel("Email Address")
        email_label.setFont(QFont("Arial", 10))
        email_input = QLineEdit()
        email_input.setPlaceholderText("Input your email:")
        email_input.setFixedSize(500, 40)
        email_input.setObjectName("email_input")

        # ----- SENHA -----

        password_label = QLabel("Password")
        password_label.setFont(QFont("Arial", 10))
        password_input = QLineEdit()
        password_input.setPlaceholderText("Input your password:")
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setFixedSize(500, 40)
        password_input.setObjectName("password_input")

        # ----- LAYOUT "EMAIL ADDRESS" -----

        email_group_layout = QVBoxLayout()
        email_group_layout.setSpacing(5)
        email_group_layout.addWidget(email_label)
        email_group_layout.addWidget(email_input)

        # ----- LAYOUT "PASSWORD" -----

        password_group_layout = QVBoxLayout()
        password_group_layout.setSpacing(5)
        password_group_layout.addWidget(password_label)
        password_group_layout.addWidget(password_input)

        # ----- ADD GRUPOS AO LAYOUT SUPERIOR -----

        top_container_layout.addLayout(email_group_layout)
        top_container_layout.addLayout(password_group_layout)

        # ----- LAYOUT "REMEMBER ME" E "I FORGOT MY PASSWORD" -----

        options_layout = QHBoxLayout()
        remember_me = QCheckBox("Remember me")
        remember_me.setFont(QFont("Arial", 10))
        remember_me.setChecked(True) # Para ficar mais parecido com a imagem

        forgot_password = QLabel('<a href="#">Forgot your password?</a>')
        forgot_password.setOpenExternalLinks(False) # Não abre link de verdade, é só visual
        forgot_password.setFont(QFont("Arial", 10))
        forgot_password.setStyleSheet("color: #4A90E2;") # Cor do link

        options_layout.addWidget(remember_me)
        options_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        options_layout.addWidget(forgot_password, alignment=Qt.AlignRight)

        # ----- LAYOUT "OPÇÕES" -----

        top_container_layout.addLayout(options_layout)

        # ----- BOTÃO LOGIN -----

        login_button = QPushButton("LOGIN")
        login_button.setObjectName("login_button")
        login_button.setFixedSize(400, 45)
        login_button.setFont(QFont("Arial", 12, QFont.Bold))
        top_container_layout.addWidget(login_button, alignment=Qt.AlignCenter)

        # ----- LAYOUT "NEW USER" -----

        new_user_layout = QHBoxLayout()
        new_user_label = QLabel("New User?")
        new_user_label.setFont(QFont("Arial", 10))
        create_account = QLabel('<a href="#">Create an Account</a>')
        create_account.setOpenExternalLinks(False)
        create_account.setFont(QFont("Arial", 10, QFont.Bold))
        create_account.setStyleSheet("color: #4A90E2;")

        new_user_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        new_user_layout.addWidget(new_user_label)
        new_user_layout.addWidget(create_account)
        new_user_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        top_container_layout.addLayout(new_user_layout)

        # ----- DIVISOR "OR" -----

        or_label = QLabel("OR")
        or_label.setFont(QFont("Arial", 10))
        or_label.setAlignment(Qt.AlignCenter)
        or_label.setStyleSheet("color: gray;")
        top_container_layout.addWidget(or_label)

        # ----- ADD CONT. SUPERIOR AO LAYOUT -----

        main_layout.addWidget(top_container)

        # ----- PARTE INFERIOR (FUNDO ESCURO) -----

        bottom_container = QWidget()
        bottom_container.setObjectName("bottom_container")
        bottom_container_layout = QHBoxLayout(bottom_container)
        bottom_container_layout.setAlignment(Qt.AlignCenter)
        bottom_container_layout.setContentsMargins(50, 40, 50, 60)
        bottom_container_layout.setSpacing(20)

        # ----- BOTÃO FACEBOOK -----

        fb_button = QPushButton("f Login with Facebook")
        fb_button.setObjectName("fb_button")
        fb_button.setFixedSize(180, 45)
        fb_button.setFont(QFont("Arial", 10, QFont.Bold))
        bottom_container_layout.addWidget(fb_button)

        # ----- BOTÃO GOOGLE -----

        google_button = QPushButton("G+ Login with Google")
        google_button.setObjectName("google_button")
        google_button.setFixedSize(180, 45)
        google_button.setFont(QFont("Arial", 10, QFont.Bold))
        bottom_container_layout.addWidget(google_button)

        # ----- ADD CONT. INFERIOR AO LAYOUT -----

        main_layout.addWidget(bottom_container)

    def set_styles(self):

        style_sheet = """
            QWidget {
                background-color: #f7f7f7; /* Cor de fundo clara para a janela */
            }

            /* Estilo para a parte inferior escura */
            #bottom_container {
                background-color: #2c3e50; /* Cor de fundo escura (azul marinho) */
            }

            /* Estilo dos campos de texto (QLineEdit) */
            QLineEdit {
                border: 1px solid #bdc3c7; /* Borda cinza clara */
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                color: #555;
            }

            /* Estilo do botão LOGIN */
            #login_button {
                background-color: #4A90E2; /* Azul */
                color: white;
                border: none;
                border-radius: 5px;
            }
            #login_button:hover {
                background-color: #357ABD;
            }

            /* Estilo do botão Facebook */
            #fb_button {
                background-color: #3b5998; /* Azul Facebook */
                color: white;
                border: none;
                border-radius: 5px;
            }
            #fb_button:hover {
                background-color: #2d4373;
            }

            /* Estilo do botão Google */
            #google_button {
                background-color: #db4437; /* Vermelho Google */
                color: white;
                border: none;
                border-radius: 5px;
            }
            #google_button:hover {
                background-color: #c33d31;
            }
            
            /* Estilo para labels (para garantir a cor do texto) */
            QLabel {
                color: #333; /* Cor do texto padrão */
            }
            
            /* Estilo para o campo de email e senha, para replicar o visual 'vazio' e 'preenchido' */
            #email_input, #password_input {
                background-color: white;
            }
            #email_input[placeholderText="johndoe@gmail.com"] {
                color: #999; /* Cor do placeholder mais clara */
            }
        """
        self.setStyleSheet(style_sheet)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    janela = LoginWindow()
    janela.show()
    app.exec_()