import datetime

# Se a soma for diferente de 4 o assert vai dizer que tem erro

assert 2 + 2 == 4 

if not 2 + 2 == 5: raise senhaerrada(Exception)

def senhaerrada(Exception):
    print("senha errada")
    a = 1


class Ser:

    def move(self):
        print("Com os pés")
        pass


class movimento(Ser):

    def move(self):
        print("Andando")

class movimentol(Ser):

    def move(self):
        super().move()
        print("Andando")

# A = movimento()
# A.move()

B = movimentol()
B.move()

t = issubclass(movimento, Ser)
t1 = isinstance(movimento(), Ser)

class Test(object):

    # Inicia toda vez que a classe é instanciada
    # Não retorna nada
    def __init__(self, texto):
        self.texto = texto
    
    # Executa somente uma vez quando a classe é instanciada
    # Retorna valores
    def __new__(cls):
        return print("Creating instance") # super(A, cls).__new__(cls)

    # retorna alguma coisa de inicio
    def __repr__(self):
        return self.texto

    # Adiciona valor ao metodo
    def __add__(self, outro):
        return self.texto + outro




BANANA: str         # str é Anotation
BANANA = 'fruta'    # Variavel normal


# Lambda Function!

double = lambda x: x * 2
multi = lambda x,y: x * y
# BANANA <= multi(2,10)

BANANA

print(double(4))
print(multi(2,10))

# Recursão
def fatorial(x) -> int:
    if x == 1:
        return 1
    else:
        return (x * fatorial(x-1))



# Argumentos variaveis
def ola(nome, mensagem="Bom dia"):
    print(mensagem, nome,',Tudo bem?')

ola('magnolia')
ola('felisberto','Boa tarde')


# Arbitrary arguments --> *args  --> Lista
def cumprimentos(*nomes):
    for nome in nomes:
        print("Hello", nome)

def despedidas(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" %(key, value))

despedidas(first='Até', mid='a', last='noite')

