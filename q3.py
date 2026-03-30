# Escreva um programa que leia um numero inteiro positivo e escreva na tela:

# FIZZ se o numero e divisivel por tres;
# BUZZ se o numero e divisivel por cinco;
# FIZZBUZZ se o numero e divisivel por tres e por cinco ao mesmo tempo.
# O proprio numero caso nao seja divisivel por tres ou por cinco.
# OBS: para cada numero lido apenas uma resposta deve ser impressa.

# funcao que le e valida um numero inteiro positivo
def ler_numero_inteiro():
    try:
        numero = int(input())       # le a entrada e converte para inteiro
        if numero < 0:              # verifica se o numero e negativo
            print("Valor invalido. Por favor, digite um numero inteiro positivo.")
            return None             # retorna None se o numero for negativo
        return numero               # retorna o numero se valido
    except ValueError:              # captura erro se a entrada nao for numerica
        print("Valor invalido. Por favor, digite um numero inteiro.")
        return None                 # retorna None em caso de erro

# funcao que aplica as regras do FizzBuzz
def fizz_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:   # verifica se e divisivel por 3 E por 5 ao mesmo tempo
        return "FIZZBUZZ"                       # retorna FIZZBUZZ se divisivel pelos dois
    elif numero % 3 == 0:                       # verifica se e divisivel apenas por 3
        return "FIZZ"                           # retorna FIZZ se divisivel por 3
    elif numero % 5 == 0:                       # verifica se e divisivel apenas por 5
        return "BUZZ"                           # retorna BUZZ se divisivel por 5
    else:
        return str(numero)                      # retorna o proprio numero convertido para string

# funcao principal que coordena leitura e exibicao do resultado
def main():
    numero = ler_numero_inteiro()     # le o numero da entrada
    if numero is not None:            # verifica se a leitura foi bem-sucedida
        resultado = fizz_buzz(numero) # aplica as regras do FizzBuzz
        print(resultado)              # exibe o resultado

# ponto de entrada: executa apenas quando rodado diretamente
if __name__ == "__main__":
    main()    # chama a funcao principal