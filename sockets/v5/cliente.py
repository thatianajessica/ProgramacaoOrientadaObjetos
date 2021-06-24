import socket
from produto import Cor, Produto, MyEncoder
import json
import time
import random

HOST = '127.0.0.1'  # Endereco IP do servidor
PORT = 12000        # Porta utilizada no servidor

class Cliente:
    def __init__(self, conn):
        self._conn = conn

    def enviarProduto(self):
        '''Cria e envia um produto (aleatoriamente) usando o socket conn'''
        self._conn.send(b'adicionar')
        resposta = self._conn.recv(2048)
        print(resposta.decode())
        cod = random.randint(1,10000)
        preco = random.randint(1,2000)
        P = Produto(cod, 'nome-' + str(cod), preco, [Cor('azul'), Cor('branco')])

        self._conn.send(str.encode(json.dumps(P, cls=MyEncoder)))
        resposta = self._conn.recv(2048)
        print(resposta.decode())
    
    def receberLista(self):
        '''Receber a lista de produtos utilizando o socket conn'''
        self._conn.send(b'listar')
        dados = b''
        while True:
            d= self._conn.recv(2048)
            dados += d
            if  len(d)< 2048:
                break

        L = json.loads(dados.decode(),object_hook=MyEncoder.decode)
        return L

    def buscarProduto(self, cod):
        with  TinyDB('dados-exemplo.json') as db:
        Q = Query()
        l = db.search(Q.cod = cod)
        for x in l:
            print(x)

        

    def terminar(self):
        '''Enviar mensagem de fim utilizando o socket conn'''
        self._conn.send(b'terminar')

if __name__ == "__main__":
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Conectado!")
            
            C = Cliente(s)
            for i in range(10):
                #Enviar/adicionar produtos
                C.enviarProduto()
                # Receber a lista do servidor
                L = C.receberLista()
                print('--------------')
                for l in L:
                    print(l)
                print('--------------')
                time.sleep(random.uniform(0.1,3))

            #Fim

            C.terminar()
            print('Fim do cliente')
    
    except Exception as E:
        print('Erro na conexao...{0}'.format(E))
        raise E
    
