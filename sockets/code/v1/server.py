import socket

HOST = '127.0.0.1'  # Endereco IP
PORT = 12000        # Porta

class Server:

    def __init__(self, host, port ):
        self._host = host
        self._port = port

    def iniciar(self):
        '''Inicia o servidor para aceitar solicitacoes'''
    
        # O uso de with permite fechar automaticamente as conexoes 
        # socket.AF_INET : IPv4
        # socket.SOCK_STREAM: TCP
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self._host, self._port)) # Selecionar o endereco e porta
            s.listen() # Escutar solicitacoes
        
            # accept espera por uma nova conexao. 
            # Quando um cliente se conectar, accept retorna :
            # - um socket (con) para se comunicar com o cliente
            # - o endereco do cliente
            conn, addr = s.accept()
        
            with conn:
                # Por enquanto o servidor imprime uma mensagem e encerra a conexao
                print('Nova conexao com o cliente {0}'.format(addr))

if __name__ == "__main__":
    S = Server(HOST,PORT)
    S.iniciar()
