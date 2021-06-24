import socket

HOST = '127.0.0.1'  # Endereco IP
PORT = 12000        # Porta

class Server:
    def __init__(self, host, port ):
        self._host = host
        self._port = port

    def iniciar(self):
        '''Aceitar um cliente, enviar e receber uma mensagem '''
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self._host, self._port)) # Selecionar o endereco e porta
            s.listen() # Escutar solicitacoes
        
            conn, addr = s.accept()
            try:
                with conn:
                    #Note o uso do b na string (strings binarias)
                    conn.send(b'Oi, sou o servidor')
        
                    #recebe até 1024 bytes do cliente
                    msg = conn.recv(1024)
                    # Decode: converte uma string binaria para uma string ASCII
                    print('Mensagem recebida: {0}'.format(msg.decode()))
        
                    print('Fim do servidor ')
            except Exception as E:
                print('Erro na conexao...{0}'.format(E))

if __name__ == "__main__":
    S = Server(HOST,PORT)
    S.iniciar()
