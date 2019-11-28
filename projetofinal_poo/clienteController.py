# Classe do controlador do cliente
import tkinter as tk
from clienteView import AppGUI
from usuarioModel import *
import json
import socket

# Fará comunicação com o server
HOST = '127.0.0.1'  # Endereco IP
PORT = 12000        # Porta

class Controller:
    '''
    O controlador define 2 ações:
     - adicionar_pessoa: para adicionar novas pessoas no banco de
       dados.  
     - listar_pessoas: retornar a lista das pessoas

     Note que as 2 ações supracitadas utilizam a classe do Modelo para
     consultar/atualizar o banco de dados
    '''

    def __init__(self, host, port):

        # Comunicação com o servidor
        self._host = host
        self._port = port
        # Criar a Janela principal
        self.root = tk.Tk()
        self.root.geometry('400x200+100+100')
        self.root.title('Tocador de música - Janela login')

        # Criar a Janela do player, apos o login
        self.root_main = tk.Tk()
        self.root_main.geometry('800x400+100+100')
        self.root_main.title('Tocador de música - Janela Principal')

        # Criar o objeto View
        self.view = AppGUI(self.root,0, self)

        #Loop
        self.root.mainloop()

    
    def logar(self,usuario, senha):
        '''Recupera os dados de login inseridos na view e envia ao sevidor'''
        log_pass = json.dumps({'usuario': usuario, 'senha': senha}).encode() # Fiz um dicionario json e transformei em binário
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            conn.connect((HOST, PORT))
            try:
                conn.send(b'entrar') # Terá uma série de opções no série de opções no servidor e essa é uma das que serão chamadas
                conn.recv(2048)
                conn.send(log_pass) # Enviará para o servidor os dados que precisam ser validados
                resposta = conn.recv(2048).decode()
        
                if resposta == 'True': # Será que tem problema em fazer isso ?
                    print("entrei no true")
                    self.view.entrar()
                else:
                    print("entrei no false")
                    self.view.entrar_erro()

            except:
                self.view.entrar_erro()

    @staticmethod
    def cadastrar(nome, idade, pais, email, usuario, senha, conn):
        '''Recupera os dados de cadastro inseridos na view e envia ao servidor'''
        dados = json.dumps({'nome': nome, 'idade': idade, 'pais': email, 'email': email, 'usuario': usuario, 'senha': senha}).encode()
    
        conn.send(b'cadastrar')
        conn.send(dados)
        resposta =  conn.recv(2048)

        #if resposta == b'usuario ja cadastrado':
            #Chamar erro na view