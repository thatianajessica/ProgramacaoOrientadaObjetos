import socket
from pessoa import Pessoa
import pickle

HOST = '127.0.0.1'  # Endereco IP do servidor
PORT = 12000        # Porta utilizada no servidor

class Cliente:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        
    def iniciar(self):
        '''Criar e enviar as informacoes duma pessoa '''

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                print("Conectado!")
                #Enviar uma pessoa
                P = Pessoa('Nome da pessoa', 'email da pessoa')
                s.send(pickle.dumps(P))
                print('Fim do cliente')
        
        except Exception as E:
            print('Erro na conexao...{0}'.format(E))

if __name__ == "__main__":
    C = Cliente(HOST,PORT)
    C.iniciar()
