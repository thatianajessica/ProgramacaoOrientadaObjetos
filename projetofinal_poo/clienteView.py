import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
       

class AppGUI:

    def __init__(self, master, tipo, controller):

        self.controller = controller
        self.tipo = tipo
        self.frame = tk.Frame(master)
        self.frame.pack()

        if(self.tipo == 0):
            self.controller.root_main.iconify()
            self.frame = tk.Frame(master)
            self.frame.pack()

            #Variáveis capturadoras de informação
            self.vusuario = StringVar()
            self.vsenha = StringVar()

            #Botões e entradas

            self.llogin = tk.Label(self.frame, text="Usuário:")
            self.lsenha = tk.Label(self.frame, text="Senha:")
            self.eusuario = tk.Entry(self.frame, textvariable=self.vusuario)
            self.esenha = tk.Entry(self.frame, textvariable=self.vsenha, show = "*")
            self.btnEntrar = tk.Button(self.frame, text="Entrar")
            self.btnCadastrar = tk.Button(self.frame, text="Cadastrar")

            #Adicionar Widgets
            self.llogin.grid(row=0,column=0)
            self.lsenha.grid(row=1,column=0)
            self.eusuario.grid(row=0,column=1)
            self.esenha.grid(row=1,column=1)
            self.btnCadastrar.grid(row=2,column=0)
            self.btnEntrar.grid(row=2,column=1)

            ##acao do botao para cadastrar - abrirá uma nova janela top.level
            self.btnCadastrar.bind("<Button>", lambda e: self.cadastrar())

            ##acao do botao para entrar - abrira uma nova janela root
            self.btnEntrar.bind("<Button>", lambda e: controller.logar(self.vusuario.get(), self.vsenha.get()))

        if(self.tipo == 1):
            self.frame = tk.Frame(self.controller.root_main)
            self.frame.pack()

            self.lemexecucao = tk.Label(self.frame, text="Em Execucao:")
            self.lartista = tk.Label(self.frame, text="Artista:")
            self.btnVerPlaylist = tk.Button(self.frame, text="VerPlaylist")
            self.btnFavoritar = tk.Button(self.frame, text="Favoritar")
            self.btnExecutar = tk.Button(self.frame, text="Executar")
            self.btnPausar = tk.Button(self.frame, text="Pausar")
            self.btnnPular = tk.Button(self.frame, text="Pular")
            self.btnVoltar = tk.Button(self.frame, text="Voltar")

            #Adicionar Widgets
            self.lemexecucao.grid(row=0,column=0)
            self.lartista.grid(row=1,column=0)
            self.btnVerPlaylist.grid(row=2,column=0)
            self.btnFavoritar.grid(row=2,column=1)
            self.btnExecutar.grid(row=2,column=2)
            self.btnPausar.grid(row=3,column=0)
            self.btnnPular.grid(row=3,column=1)
            self.btnVoltar.grid(row=3,column=2)


            self.btnVerPlaylist.bind("<Button>", lambda e: self.abrirPlaylist());




    def cadastrar(self):
        ##deixar comentado, motivo ver comentario na funcao de limpar
        #self.eusuario['state'] = 'disabled'
        #self.esenha['state'] = 'disabled'
        self.controller.root.iconify()
        self.win = tk.Toplevel()
        self.win.wm_title("Cadastro")
        self.win.geometry('400x200')
        self.frame = tk.Frame(self.win)
        self.frame.pack()


        #captura informações para cadastro
        self.vnome = StringVar()
        self.vemail = StringVar()
        self.vidade = StringVar()
        self.vpais = StringVar()
        self.vusuario = StringVar()
        self.vsenha = StringVar()

        #Botões e campos de entrada
        self.lusuario = tk.Label(self.frame, text="Usuário:")
        self.lsenha = tk.Label(self.frame, text="Senha:")
        self.lnome = tk.Label(self.frame, text="Nome:")
        self.lemail = tk.Label(self.frame, text="Email:")
        self.lidade = tk.Label(self.frame, text="Idade:")
        self.lpais = tk.Label(self.frame, text="País:")
        self.eusuario = tk.Entry(self.frame, textvariable=self.vusuario)
        self.esenha = tk.Entry(self.frame, textvariable=self.vsenha, show = "*")
        self.enome = tk.Entry(self.frame, textvariable=self.vnome)
        self.eemail = tk.Entry(self.frame, textvariable=self.vemail)
        self.eidade = tk.Entry(self.frame, textvariable=self.vidade)
        self.epais = tk.Entry(self.frame, textvariable=self.vpais)
        self.btnTerminar = tk.Button(self.frame, text="Terminar") #Finaliza a operação de cadastro

        self.lnome.grid(row=0,column=0)
        self.enome.grid(row=0,column=1)
        self.lidade.grid(row=1,column=0)
        self.eidade.grid(row=1,column=1)
        self.lpais.grid(row=2,column=0)
        self.epais.grid(row=2,column=1)
        self.lemail.grid(row=3,column=0)
        self.eemail.grid(row=3,column=1)
        self.lusuario.grid(row=4,column=0)
        self.eusuario.grid(row=4,column=1)
        self.lsenha.grid(row=5,column=0)
        self.esenha.grid(row=5,column=1)
        self.btnTerminar.grid(row=6,column=0)

        self.btnTerminar.bind("<Button>", lambda e: self.limpar())

    
    def limpar(self):
        '''Remover os textos dos campos'''
        self.win.destroy()
        self.controller.root.deiconify()
        ## linhas 94 e 95 deveria funcionar para reabilitar os campos loguin e senha da tela root1, mas só desabilita o do loguin. Vou deixar comentado por hora
        #self.eusuario['state'] = 'normal'
        #self.esenha['state'] = 'normal'
        self.vusuario.set("")
        self.vsenha.set("")
        #Focus no campo 
        self.eusuario.focus_set()
        
    def entrar(self):
        self.controller.root.iconify()
        self.controller.root_main.deiconify()
        MinhatelaPrincipal = AppGUI(self.controller.root_main, 1, self.controller)
        self.controller.root_main.mainloop()

    def entrar_erro(self):
        messagebox.showinfo("Erro", "Dados incorretos")
    
    def retornarMainWindow(self):
        self.win.destroy()
        self.controller.root_main.deiconify()

    def abrirPlaylist(self):
        self.controller.root.iconify()
        self.controller.root_main.iconify()
        self.win = tk.Toplevel()
        self.win.wm_title("Playlist Favoritas")
        self.win.geometry('400x200')
        self.frame = tk.Frame(self.win)
        self.frame.pack()


        #captura informações para cadastro
        self.vnome = StringVar()
        self.vemail = StringVar()
        self.vidade = StringVar()
        self.vpais = StringVar()
        self.vusuario = StringVar()
        self.vsenha = StringVar()

        #Botões e campos de entrada
        self.lusuario = tk.Label(self.frame, text="Usuário:")
        self.lsenha = tk.Label(self.frame, text="Senha:")
        self.lnome = tk.Label(self.frame, text="Nome:")
        self.lemail = tk.Label(self.frame, text="Email:")
        self.lidade = tk.Label(self.frame, text="Idade:")
        self.lpais = tk.Label(self.frame, text="País:")
        self.eusuario = tk.Entry(self.frame, textvariable=self.vusuario)
        self.esenha = tk.Entry(self.frame, textvariable=self.vsenha, show = "*")
        self.enome = tk.Entry(self.frame, textvariable=self.vnome)
        self.eemail = tk.Entry(self.frame, textvariable=self.vemail)
        self.eidade = tk.Entry(self.frame, textvariable=self.vidade)
        self.epais = tk.Entry(self.frame, textvariable=self.vpais)
        self.btnRetornar = tk.Button(self.frame, text="Terminar") #Finaliza a operação de cadastro

        self.lnome.grid(row=0,column=0)
        self.enome.grid(row=0,column=1)
        self.lidade.grid(row=1,column=0)
        self.eidade.grid(row=1,column=1)
        self.lpais.grid(row=2,column=0)
        self.epais.grid(row=2,column=1)
        self.lemail.grid(row=3,column=0)
        self.eemail.grid(row=3,column=1)
        self.lusuario.grid(row=4,column=0)
        self.eusuario.grid(row=4,column=1)
        self.lsenha.grid(row=5,column=0)
        self.esenha.grid(row=5,column=1)
        self.btnRetornar.grid(row=6,column=0)

        self.btnRetornar.bind("<Button>", lambda e: self.retornarMainWindow())

    


        

        


#Minhatela = AppGUI(root, 0)
#root.mainloop()