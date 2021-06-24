import socket
from produto import Cor, Produto, MyEncoder
import json
import argparse

#HOST = '127.0.0.1'  # Endereco IP do servidor
#PORT = 12000        # Porta utilizada no servidor



class Cliente:
    def __init__(self, host, port):
        self._host = host
        self._port = port

    @staticmethod
    def enviarProduto(P, conn):
        '''Enviar o produto P usando o socket conn'''
        conn.send(b'adicionar')
        resposta = conn.recv(2048)
        print(resposta.decode())
        conn.send(str.encode(json.dumps(P, cls=MyEncoder)))
        resposta = conn.recv(2048)
        print(resposta.decode())

    @staticmethod
    def consultarProdutoDatabase(codigo, conn):
        '''Consultar o produto P usando o socket conn'''
        conn.send(b'consultar')
        resposta = conn.recv(2048)
        print(resposta.decode())
        conn.send(str(codigo).encode())
        resposta = conn.recv(2048)
        print(type(resposta)) ##era pra vir um produto, mas veio algo da classe <bytes> por causa da funcao de recv do sockets suponho
        L = json.loads(resposta.decode(),object_hook=MyEncoder.decode) ##emboa resposta seja <bytes> e o metodo decode do MyEncoder receba como parametro um dicionario, isso funcionou
        #print(L)
        print(type(L))##estimei que com isso converteria para uma lista para entao poder extrair o produto com pop, mas, já é um produto
        return L
       

    @staticmethod
    def receberLista(conn):
        '''Receber a lista de produtos utilizando o socket conn'''
        conn.send(b'listar')
        dados= conn.recv(2048)
        L = json.loads(dados.decode(),object_hook=MyEncoder.decode)
        return L
    
    @staticmethod
    def terminar(conn):
        '''Enviar mensagem de fim utilizando o socket conn'''
        conn.send(b'terminar')

    @staticmethod   
    def acao(acao, P, codigo):
        if(acao == args.adicionar):
            Cliente.enviarProduto(P, s)
            retorno = None
        elif(acao == args.listar):
            retorno = Cliente.receberLista(s)
        elif(acao == args.consultar):
            retorno = Cliente.consultarProdutoDatabase(codigo, s)
        return retorno     

    def iniciar(self): 
        '''Enviar 3 produtos e listar os produtos no banco de dados (recebidos do servidor)'''
        
        try:   
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((args.HOST, args.PORT))
                print("Conectado!")
        
                C1 = Cor('verde')
                C2 = Cor('branco')
                C3 = Cor('preto')
                P1 = Produto(1, 'Produto1', 200, [C1 , C3])
                P2 = Produto(2, 'produto2', 300, [C1 , C2])
                P3 = Produto(3, 'produto3', 400, [C2 , C3])
                P4 = Produto(4, 'produto4', 500, [C2 , C3])
                P5 = Produto(5, 'produto5', 600, [C1 , C2])
        
                retorno = Cliente.acao(args.adicionar,args.produto,args.codigo)
                #Enviar/adicionar produtos
                #Cliente.enviarProduto(P1, s)
                #Cliente.enviarProduto(P2, s)
                #Cliente.enviarProduto(P3, s)
                #Cliente.enviarProduto(P4, s)
                #Cliente.enviarProduto(P5, s)
                # Receber a lista do servidor
                #lista_consulta = Cliente.consultarProdutoDatabase(1, s)
                #print(lista_consulta)
                #lista_consulta2 = Cliente.consultarProdutoDatabase(3, s)
                #print(lista_consulta2)

                #L = Cliente.receberLista(s)
                print(retorno)
        
                #Fim
                Cliente.terminar(s)
                print('Fim do cliente')
        
        except Exception as E:
            print('Erro na conexao...{0}'.format(E))
        
if __name__ == "__main__":
    C1 = Cor('verde')
    C2 = Cor('branco')
    C3 = Cor('preto')

    P1 = Produto(1, 'Produto1', 200, [C1 , C3])

    parser = argparse.ArgumentParser( 
    description='''
    Este script permite 3 ações:
    - adicionar
    - listar
    - consultar''', formatter_class=argparse.RawTextHelpFormatter )


    parser.add_argument('--adicionar', type=str, default='adicionar',help='Açoes a serem realizadas com produtos que contem 4 atributos = codigo, nome, preco, cores ao database')
    parser.add_argument('--listar', type=str, default=None,help='Listar produtos que contem 4 atributos = codigo, nome, preco, cores')
    parser.add_argument('--buscar', type=str, default=None,help='Buscar um determinado produto que contem 4 atributos = codigo, nome, preco, cores')
    #parser.add_argument('--acao', type=str, default=adicionar,help='Buscar um determinado produto que contem 4 atributos = codigo, nome, preco, cores')
    
    parser.add_argument('--produto', type=Produto, default=P1 , help='Objeto produto')
    parser.add_argument('--HOST', type=str, default='127.0.0.1' , help='Local host')
    parser.add_argument('--PORT', type=int, default= 12000, help='Local port')
    parser.add_argument('--codigo', type=int, default=1 , help='Objeto produto')
    
    args = parser.parse_args()

    C = Cliente(args.HOST,args.PORT)
    C.iniciar() 
