import socket
import produto
import json

HOST = '127.0.0.1'  # Endereco IP
PORT = 12000        # Porta

class Server:
    def __init__(self, host, port ):
        self._host = host
        self._port = port
        self._listaProds = [] # Lista com todos os produtos

    def iniciar(self):
        '''Adicionar e listar produtos (segundo a escolha do cliente)'''


        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self._host, self._port)) # Selecionar o endereco e porta
            s.listen() # Escutar solicitacoes
        
            conn, addr = s.accept()
            try:
                with conn:
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
                            break
        
        
                print('Fim do servidor ')
            except Exception as E:
                print('Erro na conexao...{0}'.format(E))

if __name__ == "__main__":
    S = Server(HOST,PORT)
    S.iniciar()
