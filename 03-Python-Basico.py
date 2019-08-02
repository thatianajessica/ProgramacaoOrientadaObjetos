#!/usr/bin/env python
# coding: utf-8

# # Python Básico I
# 
# ## Objetivos 
# 
# O objetivo da aula é introduzir comandos básicos em Python:
#  - Terminal interativo de comandos
#  - Variáveis e tipos
#  - Operadores e expressões
#  - Entrada e saída
#  Controle de fluxo (`if`, `while`, `for`)
# 
# ## A Linguagem de Programação Python
# 
# - Linguagem criada no início dos anos 90 (Guido van Rossum)
#     - Versão 3: lançada em 2008
# - Utilizada em diferentes tipos de aplicações:
#     - Linguagem de script (auxiliar)
#     - Aplicações das grandes indústrias de software (Google, Dropbox, Intel, Netflix, etc.)
#     - Aplicações científicas (NASA, Robot Operating System, etc.)
#     - Bibliotecas de IA: Deep learning (PyTorch, TensorFlow)
# - Crescimento de uso considerável na década atual
# 
# ## A Linguagem de Programação Python
# 
# Por que Python?
# 
# - Simplicidade
# - Facilidade de aprendizado e de correção de erros
# - Código limpo
# - Código multiplataforma (Linux/Mac/Windows)
# - **Suporta o paradigma de programação orientada a objetos**
# 
# ## A Linguagem de Programação Python
# 
# - É uma linguagem interpretada
#     - Código fonte:
#         - Terminação do arquivo: .py
#         - É interpretado pelo interpretador Python
#     - Após interpretado:
#         - Código fonte se torna uma representação
#           intermediária chamada *bytecode*
#         - Representação independente de hardware
#         - Terminação do arquivo: .pyc
#     - Último passo no processo de interpretação
#         - *Bytecode* é executado, instrução por instrução,
#           pela máquina virtual Python (PVM)
#     - Todo o processo é realizado sem intervenção do programador
# 
# ## Terminal de Comandos Interativo
# - A linguagem Python suporta um terminal de comandos interativo
# - Qualquer comando da linguagem pode ser executado
#     - Agiliza a programação
#     - Facilita a depuração de erros
#     - Ajuda nas funções/classes declaradas
# - **Importante**: confira se a versão do Python é a 3.X
# 
# ```
# $> python
# Python 3.7.3 (default, Mar 30 2019, 03:37:43) 
# [Clang 10.0.0 (clang-1000.11.45.5)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# ```
# 
# ## Terminal Python como Calculadora ( e o Zen do Python)
# 
# Segue alguns comandos simples que podem ser executados no terminal de comandos interativos 
# 

# In[ ]:


3 + 2


# In[ ]:


print("alo mundo!")


# In[ ]:





# In[ ]:


import math
math.sqrt(2)


# In[1]:


# O Zen do Python
import this


# ---
# ## Comandos Básicos em Python
# 
# ### Comentários
# Comentários de linha em Python: linhas que começam com ```#```
# 
# Também, strings podem ser utilizadas para documentar código:

# In[4]:


def soma(x, y):
  '''Função para calcular a soma de x e y'''
  return x + y

soma(3,2)
#Podemos ler a documentação da função!
soma.__doc__


# In[5]:


def soma(x, y):
  '''Função para calcular a soma de x e y'''
  return x + y

soma(3,2)


# In[6]:


# Alternativamente, podemos utilizar a função help
help(soma)


# Strings podem ser também utilizadas para comentários de várias linhas

# In[7]:


def mult(x,y):
    '''
    Retorna x * y.
    Nesta implementação vamos a utilizar
    o operator * de Python e depois retornar o valor. 
    '''
    return x * y

print(mult(3,5))
help(mult)
    


# ## Separador
# Note que não há necessidade de utilizar ```;```
# 

# In[8]:


x = 4 ; # Com ;
y = 5   # some  ;
print(x+y)


# --- 
# 
# ## Variáveis e tipos
# - Declarar variável:
#     - Tipo da variável é determinado automaticamente pelo valor atribuído
#     - Usar operador de atribuição ```=```
#     - Ex.: ```a = 5```, a variável ```a``` é do tipo ```int```
# - Como saber o tipo de uma variável: ```type(variavel)```

# In[11]:


i = 3
type(i)


# In[12]:


s = "alo"
type(s)


# In[13]:


f = 3.2
type(f)


# In[ ]:


b = True
type(b)


# ### Tipos básicos em Python
# - Número inteiro: ```int```
# - Número real: ```float```
# - Booleano: ```bool``` (valor ```True``` ou ```False```)
# - String: ```str``` (tanto faz aspas simples ``` `ECT' ``` ou duplas ```"ECT"```)
#     - Também usado para caracteres

# In[14]:


print('uma string')
print("outra string")
print("mais uma string")


# ### Conversão explícita entre tipos
# É possível converter uma variável de um tipo em outro utilizando funções cujo nome é igual ao tipo para o qual a expressão deve ser convertida:
# 
# - ```int(expr)```, ```float(expr)```, etc.
# - Similar ao operador de *typecast* em C++
# 
# Alguns exemplos:

# In[17]:


x = int('1234')
y = float('5.1435')
type(y)
i = int (3.2)
print(i)


# In[19]:


i = 4
s = str(i)
print(s)
type(s)


# ### Conversão implícita
# Em Python, há também a conversão implícita:

# In[20]:


a = 10
b = 1.33
c = a + b
type(c)


# ---
# ## Comandos Básicos em Python
# ### Operadores aritméticos
# - Adição: ```+```
# - Subtração: ```-```
# - Multiplicação: ```*```
# - Divisão: ```/```
# - Divisão inteira: ```//``` (divide e aplica a função ```floor(expr)```)
# - Resto da divisão: ```%```
# - Exponenciação: ```**```
# - Radiciação: função ```sqrt``` (módulo ```math```)
# - Atribuição junto com operação: ```+=```, ```-=```, etc.
# 
# Alguns exemplos:

# In[21]:


print(3 / 2) # Divisão
print(3 // 2) # Divisão inteira
print (6 % 2) #Resto da divisão
print( 3 ** 2) #Exponenciação 
x = 5
x += 3
print(x)


# ### Comparação com C++
# - Operadores para divisão e divisão inteira separados
# - Operador para potência
# - Não existe o operador de incremento/decremento (```++```/```--```)
# 
# ### Operadores relacionais
# - Igual: ```==```
# - Diferente: ```!=```
# - Maior: ```>```
# - Maior ou igual: ```>=```
# - Menor: ```<```
# - Menor ou igual: ```<=```
# 
# O que imprimiria o código a seguir em C++ ?
# ```
# cout<< (3 < 5 < 2 ) ;
# ```
# 

# In[22]:


# Em Python... funciona!
print ( 3 < 5 < 2 )


# ### Operadores lógicos e valores lógicos
# - ```False```, ```0```, ```None```, ``` '' ``` (string vazia) e sequências vazias têm o valor lógico igual a falso
# - Qualquer outra coisa: valor lógico igual a verdadeiro
# - Negação: ```not```
# - Conjunção (e): ```and```
# - Disjunção (ou): ```or```

# In[23]:


x = True and (False or True)
print(x)
print(not True)


# ### Precedência de operadores
# 1. Operadores aritméticos
# 2. Operadores relacionais
# 3. Operadores lógicos
# 
# Na dúvida, utilizar parênteses ```()```

# In[24]:


not  1 + 2  < 5


# In[25]:


(not  1 + 2)  < 5


# In[26]:


not  1 + (2  < 5)


# In[27]:


(not  1) + 2   < 5


# --- 
# 
# ## Impressão de dados na tela
# - Função ```print(mensagem)```
# - Alternativas:
#     - ```print(mensagem, expr)```
#     - Com saída formatada tipo ```printf``` do C: ```print("x eh %i, y eh %i" % (x, y))```
#     - Com saída formatada tipo Python: ```print("x e {0}, y e {1}".format(x, y))```
#     - Ainda mais simples ```print(f"x e {x}, y e {y}")```
# - Python também possui caracteres especiais como ``` `\n' ``` e ``` `\t' ```
#     - Comando ```print``` já possui o ``` `\n' ```
#     - Caso não queria utilizá-lo, altere o parâmetro ```end```:
#       ```print("o resultado eh {0}".format(x), end='')```

# In[32]:


x = 3
s = "alo"
#print(f'x = {x}, x + 4 = {x+4}. String = {s}') #valor da expressao entre chaves
print('Alo', end='...')
print('Mundo')
print('alo{0}'.format(4))


# In[33]:


x=3
y=5

print('{0}+{1} = {2}'.format(x,y,x+y))


# ## Leitura de dados do teclado
# - Função ```input(mensagem)```
# - A função retorna os dados lidos como uma única variável do tipo ```str```
# - Ou seja, para ler um número inteiro, por exemplo, é necessário utilizar a função de conversão
#     - Ex.: ```x = int(input("Insira um numero inteiro: "))```

# In[34]:


i = int(input("Número inteiro? "))
i += 1
print(i)


# ---
# ## Executando Arquivos .py
# - O terminal interativo Python é útil, mas se torna inviável para códigos com tamanhos grandes
# - Portanto, vale a pena escrever o código dos programas em arquivos ```.py```
# - Para executar o programa:
#     - Usando o terminal, vá até a pasta do arquivo e digite ```python3 arquivo.py``` ou
#     - Utilize a opção de executar um arquivo na IDE de sua preferência
#     
#     

# ---
# 
# ## Controle de Fluxo em Python
# ### Código indentado é obrigatório
# - Em Python, não há ```{``` e ```}``` como em C++ para delimitar blocos
# - Blocos são delimitados pelos espaços em branco
# - Começar novo bloco: adicionar quatro espaços em branco
# - Finalizar bloco: remover quatro espaços em branco
# - Dica: configurar editor de texto para trocar tabulação por quatro espaços
#     - Sublime Text do laboratório está configurado assim
#     - Caso contrário: o interpretador irá dizer que o programa contém erros
# - Isto é necessário para os comandos de controle de fluxo, mostrados a seguir
# 
# ### Comando condicional ```if```
# - Sintaxe:
# 
# ```
# if condicao:
#         bloco de comandos
# ```
# - ```else:``` é opcional
# 
# ### Comparação com C++
# - Não existe ```else if```, deve-se usar ```elif```
# - Não existe ```switch..case```, deve-se usar ```if... elif... else```
# 

# In[38]:


x = int(input("Insira um numero inteiro: "))
if x % 2 == 0:
    print('{0} e par'.format(x))
    #print(f'{x} e par')
else:
    print('{0} e impar'.format(x))
    #print(f'{x} e impar')


# In[ ]:


x = int(input("Insira um numero inteiro: "))
if x < 10:
    print("menor 10")
elif x < 20:
    print("entre 10 e 20")
else:
    print("maior que 20")
    


# ## Comando de repetição ```while```:
# 
# - Funciona como em C++:
#     - Enquanto uma determinada condição for verdadeira, o laço é executado
#     - É necessário:
#         - Fazer com que a condição seja verdadeira pelo menos uma vez (antes do laço)
#         - Fazer com que a condição se torne falsa, em algum momento (dentro do laço)
# - Sintaxe:
# 
# ```
# while condicao:
#     bloco de comandos
# ```
# 
# ### Comparação com C++
# - Não existe ```do..while```
# - O comando ```while``` suporta o ```else```, que é executado quando a condição é/se torna falsa
#     - Ou seja, não é executado caso o laço seja finalizado com ```break```
# 

# In[40]:


x = 0
while x < 10:
    print(x)
    x += 1
#else:
print("Fim do laco")


# # Comando de repetição ```for```:
# 
# - Funciona de forma diferente do ```for``` tradicional em C++:
#     - Uma variável local deve iterar sobre todos os elementos de uma sequência
#     - Sequências serão vistas na próxima aula
#     - Por enquanto, devemos usar a função ```range```, para gerar uma sequência em um intervalo
#         - ```range(inicio, fim)```: gera sequência no intervalo
#           $[inicio,fim[$ com incremento igual a 1
#         - ```range(inicio, fim, inc)```: gera sequência no intervalo
#           $[inicio,fim[$ com incremento igual a ```incr```
#     - O intervalo gerado faz com que o ```for``` tenha o mesmo comportamento de C++
# 
# - Sintaxe:
# 
# ```
# for var in sequencia:
#     bloco de comandos
# ```
# 
# ### Comparação com C++
# - O comando ```for``` suporta o ```else```,
#   que é executado quando a condição é/se torna falsa
#     - Ou seja, não é executado caso o laço seja finalizado com ```break```
# 

# In[41]:


for i in range(0,10):
   print(i)

print('***')
for i in range(10,0,-1):
   print(i)

print('***')   
for i in range(0,10,2):
   print(i)
 


# ### Comandos ```break``` e ```continue```
# - Suportados em Python, assim como em C++
# - ```break```: encerra o laço (o ```else``` associado ao laço não é executado)
# - ```continue```: força a próxima iteração do laço
# 
# ## Importante
# 
# - O interpretador somente irá reportar erro em uma linha sintaticamente
#   correta caso esta linha seja executada
#     - Por exemplo, caso a linha possua uma variável não declarada, o interpretador
#       somente irá reportar este tipo de erro se a linha for executada
#       
# ---
# 
# ## Exercícios
# 1. Implemente um programa que leia três números inteiros denotando os lados de um triangulo.
#    Três números formam um triângulo se cada um deles for menor do que a soma dos outros dois.
#    O programa deve informar se eles formam um triângulo e em caso positivo,
#    qual é o triângulo formado (equilátero, isósceles ou escaleno).
# 2. Implemente um programa para o usuário adivinhar qual o valor de um
#    número inteiro armazenado.
#    O programa deve ler a entrada do usuário repetidas vezes e informar se o número
#    digitado foi menor, maior ou se o usuário conseguiu adivinhar o número secreto,
#    que é igual a 23.
# 3. Implemente um programa que leia do usuário um total ```N``` de números reais
#    e imprima na tela qual foi o maior número digitado
# 4. Implemente um programa que leia do usuário um número inteiro e informa na tela
#    quantos dos seus dígitos são pares
# 

# In[50]:


lado1 = int(input("Tamanho do primeiro lado: "))
lado2 = int(input("Tamanho do segundo lado "))
lado3 = int(input("Tamanho do terceiro lado "))

if (lado1 < lado2+lado3) and (lado2 < lado1+lado3) and (lado3 < lado1+lado2):
    if lado1 == lado2 == lado3:
        print('Triangulo equilatero')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Triangulo isosceles')
    elif lado1 != lado2 != lado3:
        print('Triangulo escaleno')
else:
    print('Nao eh um triangulo')


# In[ ]:




