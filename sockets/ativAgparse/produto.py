import json
from tinydb import TinyDB, Query

class ProdutoJaExiste(Exception):
    def __init__(self):
        super().__init__("Produto ja está no database")

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
    _produtos = {}
    def __init__(self, cod, nome, preco,cores):
        self._cod = cod
        self._nome = nome
        self._preco = preco
        self._cores = cores
        

    @staticmethod
    def adicionar(P):
        Produto.append(P)

    @staticmethod
    def armazenarDatabase(P):
        if P._cod in Produto._produtos:
            raise ProdutoJaExiste

        Produto._produtos[P._cod] = P 
        with  TinyDB('database_produtos.json') as db: # arquivo database
            # Inserir um objeto no arquivo dados-exemplo.json
            # Insert recebe como parâmetro um dicionário
                db.insert((Produto._produtos[P._cod]).toDict()) #insert recebe dicionario, e P é um produto, aqui converte

    @staticmethod
    def consultarDatabase(codigo):
        with  TinyDB('database_produtos.json') as db:
            Q = Query()
            l = db.search(Q._cod == codigo)
            #print(type(l)) ##l é uma lista de dicionarios onde os elementos do dicionario sao do tipo do json <'tinydb.database.Document'>
            #print(type(l[0]))
            for x in l:
                #print(type(x))
                P = Produto.fromDict(x) #extraindo do dicionario,obtem se os objetos da classe produto
                print(type(P))
            return P ##mas quando retorna pro cliente, eles se tornam da classe bytes (ver continuacao no Cliente.py)

    def toDict(self):
        '''Retorna a representacao como dicionario'''
        s = json.dumps(self, cls=MyEncoder)
        return json.loads(s)

    @staticmethod
    def fromDict(d):
        '''Retorna a representacao como cor ou produto'''
        s = json.dumps(d)
        return json.loads(s, object_hook=MyEncoder.decode)

    def __repr__(self):
        return f'Produto{self._cod, self._nome, self._preco, self._cores}'

