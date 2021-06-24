import json
from tinydb import TinyDB, Query

class MyEncoder(json.JSONEncoder):
    def default(self, o):
        d = vars(o) # Atributos do objeto
        d['tipo'] = o.__class__.__name__  #Adicionar o tipo de objeto
        return d

    @staticmethod
    def decode(d):
        '''recebe como parâmetro um dicionario'''
        if d['tipo'] == 'Cor':
            return Cor(d['_nome'])
        if d['tipo'] == 'Produto':
            return Produto(d['_cod'], d['_nome'], d['_preco'],d['_cores'])

class Cor:
    def __init__(self, nome):
        self._nome = nome


    def __repr__(self):
        return f'Cor({self._nome})'

class Produto:
    def __init__(self, cod, nome, preco,cores):
        self._cod = cod
        self._nome = nome
        self._preco = preco
        self._cores = cores

    @staticmethod
    def adicionar(P):
        '''Adicionar P na lista de produtos'''
        Produto.append(P)

    def __repr__(self):
        return f'Produto{self._cod, self._nome, self._preco, self._cores}'


