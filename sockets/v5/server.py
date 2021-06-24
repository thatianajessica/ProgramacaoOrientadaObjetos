import socket
import produto
import json
from threading import Thread

HOST = '127.0.0.1'  # Endereco IP
PORT = 12000        # Porta

class ServerWork(Thread):
    def __init__(self, conn):
        '''Inicializa a tarefa com o socket do cliente'''
        Thread.__init__(self)
        self._conn = conn
        self._listaProds = [] # Lista com todos os produtos

    def run(self):
        '''Escutar as solicitações do cliente'''
        with self._conn as conn:
            while True:
                dados = conn.recv(2048)
                opc = dados.decode()
                if opc == "adicionar":
                    conn.send(b'esperando produtos...')
                    prods = conn.recv(2048)
                    P = json.loads(prods.decode(),object_hook=produto.MyEncoder.decode)
                    print('Produto {0} recebido.'.format(P))
                    conn.send(b'produto recebido [OK]')
                    self._listaProds.append(P)
                elif opc == "listar":
                    conn.send(str.encode(json.dumps(self._listaProds, cls=produto.MyEncoder)))
                elif opc == "terminar":
                    print('Fim do cliente')
                    break

class Server:
    def __init__(self, host, port ):
        self._host = host
        self._port = port

    def iniciar(self):
        '''Utiliza ServerWork para atender os clientes '''

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((self._host, self._port)) # Selecionar o endereco e porta
                s.listen() # Escutar solicitacoes

                while True:
                    # Novo cliente
                    conn, addr = s.accept()
                    T = ServerWork(conn)
                    T.start() # Um thread para cada nova conexão 
        
        except Exception as E:
            print('Erro na conexao...{0}'.format(E))


if __name__ == "__main__":
    S = Server(HOST,PORT)
    S.iniciar()
