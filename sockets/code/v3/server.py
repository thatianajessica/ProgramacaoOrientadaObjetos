import socket
from pessoa import Pessoa
import pickle

HOST = '127.0.0.1'  # Endereco IP
PORT = 12000        # Porta

class Server:
    def __init__(self, host, port ):
        self._host = host
        self._port = port

    def iniciar(self):
        '''Receber um objeto tipo pessoa'''

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self._host, self._port)) # Selecionar o endereco e porta
            s.listen() # Escutar solicitacoes
        
            conn, addr = s.accept()
            try:
                with conn:
                    dados = conn.recv(1024)
                    P = pickle.loads(dados)
                    print(P)
                    print('Fim do servidor ')
            except Exception as E:
                print('Erro na conexao...{0}'.format(E))

if __name__ == "__main__":
    S = Server(HOST,PORT)
    S.iniciar()
