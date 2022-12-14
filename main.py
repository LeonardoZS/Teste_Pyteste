#Leonardo Zaniboni Silva 11801049
import pytest      
#Definindo a função fibonacci
def fibonacci(x):
    if x<3:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)
#Definindo a função fatorial
def fatorial(x):
    if x<2:
        return 1
    else:
        return x*fatorial(x-1)

#Definindo a função que irá checar se o resultado bate com o arquivo certo
def test_certo():
    linha = [] ; erro = False ; count = 1
    with open('output_certo.txt') as output:
        dados = output.read()
    for i in range(len(dados)):
        if dados[i] == "\n":
            count = count + 1
        if dados[i] == saida[i]: pass
        else:
            linha.append(count)
            erro = True
    assert erro == False, print(f"As linhas ondem contém os erros seguem dispostas a seguir : {linha}. Lembrar de considerar as LINHAS VAZIAS do arquivo na contagem.")

#Definindo a função que irá checar se o resultado apresenta erros quando comparado com arquivo errado
def test_errado():
    linha = [] ; erro = False ; count = 1
    with open('output_errado.txt') as output:
        dados = output.read()
    for i in range(len(dados)):
        if dados[i] == "\n":
            count = count + 1
        if dados[i] == saida[i]: pass
        else:
            linha.append(count)
            erro = True
    assert erro == False, print(f"As linhas ondem contém os erros seguem dispostas a seguir : {linha}. Lembrar de considerar as LINHAS VAZIAS do arquivo na contagem.")

input = [1,2,4,9,7]     #dados de entrada
fibo = [] ; fact = []   #inicializando os vetores
saida = f"# fact Fib\n"
for i in range(len(input)):
    fibo.append(fibonacci(int(input[i])))
    fact.append(fatorial(int(input[i])))
    saida = saida + f"\n{input[i]} {fact[i]} {fibo[i]}\n"