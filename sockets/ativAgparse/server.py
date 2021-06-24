import socket
from produto import Produto
import produto
import json
import argparse



#HOST = '127.0.0.1'  # Endereco IP
#PORT = 12000        # Porta

class Server:
    def __init__(self, host, port ):
        self._host = args.HOST
        self._port = args.PORT
        self._listaProds = [] # Lista com todos os produtos

    def iniciar(self):
        '''Adicionar e listar produtos (segundo a escolha do cliente)'''


        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print(args.HOST, args.PORT)
            s.bind((self._host, self._port)) # Selecionar o endereco e porta
            s.listen() # Escutar solicitacoes
        
            conn, addr = s.accept()
            try:
                with conn:
                    while True:
                        dados = conn.recv(2048)
                        opc = dados.decode()
                        print(opc)
                        if opc == "adicionar":
                            conn.send(b'esperando produtos...')
                            prods = conn.recv(2048)
                            P = json.loads(prods.decode(),object_hook=produto.MyEncoder.decode)
                            print('Produto {0} recebido.'.format(P))
                            conn.send(b'produto recebido [OK]')
                            #self._listaProds.append(P)
                            Produto.armazenarDatabase(P)
                        elif opc == "listar":
                            conn.send(str.encode(json.dumps(self._listaProds, cls=produto.MyEncoder)))
                        elif opc == "consultar":
                            conn.send(b'esperando o codigo do produto...')
                            codigo = conn.recv(2048)
                            print(codigo)
                           # codigo = json.loads(prods.decode(),object_hook=produto.MyEncoder.decode) 
                            resultado = Produto.consultarDatabase(int(codigo.decode()))
                            conn.send(str.encode(json.dumps(resultado, cls=produto.MyEncoder)))
                        elif opc == "terminar":
                            break
        
        
                print('Fim do servidor ')
            except Exception as E:
                print('Erro na conexao...{0}'.format(E))

if __name__ == "__main__":

    parser = argparse.ArgumentParser( 
    description='''
    parser para passar o HOST e PORT''', formatter_class=argparse.RawTextHelpFormatter )

    parser.add_argument('--HOST', type=str, default='127.0.0.1' , help='Local host')
    parser.add_argument('--PORT', type=int, default= 12000  , help='Local port')
        
    args = parser.parse_args()

    S = Server(args.HOST,args.PORT)
    S.iniciar()
