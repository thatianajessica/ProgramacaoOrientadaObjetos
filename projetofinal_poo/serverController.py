#Classe do controlador do servidor SEEEEEEERVIDOOOOOOOOOOR

from usuarioModel import *


class ControllerSC:
    '''
    O controlador define 2 ações:
     - adicionar_pessoa: para adicionar novas pessoas no banco de
       dados.  
     - listar_pessoas: retornar a lista das pessoas

     Note que as 2 ações supracitadas utilizam a classe do Modelo para
     consultar/atualizar o banco de dados
    '''

    def __init__(self):
        pass
    
    @staticmethod
    def entrarSC(login, senha):
        resultado = Usuario.entrar(login, senha)
        return resultado

    def atualizar_email(self, cpf, novoEmail):
        '''Atualiza o email de um dada pessoa'''
        try:
            Pessoa.mudarEmail(cpf, novoEmail)
            self.view.limpar()
            self.view.email_alterado()

        except:
            self.view.erro_email()
    
    def excluir_pessoa(self, cpf):
        '''Remove uma pessoa já cadastrada na lista'''
        try:
            Pessoa.sumirComAPessoa(cpf)
            self.view.limpar()
            self.view.excluir_ok()
        except:
            self.view.excluir_erro()
            
    def listar_pessoas(self):
        '''Lista todas as pessoas cadastradas'''
        self.view.listar(Pessoa.listar())
        
