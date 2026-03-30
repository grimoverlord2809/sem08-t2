# Escreva um programa que leia um numero inteiro e some 5 caso o valor lido seja par ou some 8 caso o valor lido seja impar. Mostre na tela o resultado da operacao.

# funcao que le um numero inteiro da entrada padrao
def ler_numero_inteiro():
    numero = int(input())    # le a entrada e converte para inteiro
    return numero            # retorna o numero lido

# bloco principal com tratamento de excecao
try:
    numero = ler_numero_inteiro()    # chama a funcao para ler o numero
    if numero % 2 == 0:              # verifica se o numero e par (resto da divisao por 2 igual a 0)
        resultado = numero + 5       # se par, soma 5 ao numero
    else:                            # caso contrario, o numero e impar
        resultado = numero + 8       # se impar, soma 8 ao numero
    print(resultado)                 # exibe o resultado na tela
except ValueError:                   # captura erro caso a entrada nao seja um numero inteiro
    print("Valor invalido. Por favor, digite um numero inteiro.")