# Escreva um programa que leia um numero inteiro.
# Mostre a soma dos digitos para os numeros entre
# 0 (zero) e 100 mil ou -1 para outros valores.
# Por exemplo: Em 16759 a soma dos digitos e 1 + 6 + 7 + 5 + 9 = 28
# e o valor retornado; Em 136759 o valor lido e maior que 100 mil e deve retornar -1; Em -100 o valor lido e negativo e deve retornar -1.

# funcao que le e converte a entrada para inteiro
def numero_entrada():
    try:
        numero = int(input())    # le a entrada e converte para inteiro
        return numero            # retorna o numero lido
    except ValueError:           # captura erro se a entrada nao for numerica
        print("Valor invalido. Por favor, digite um numero inteiro.")
        return None              # retorna None em caso de erro

# funcao que calcula a soma dos digitos ou retorna -1 se fora do intervalo
def soma_digitos(numero):
    if 0 <= numero <= 100000:                                  # verifica se o numero esta entre 0 e 100000
        soma = sum(int(digito) for digito in str(numero))      # converte o numero em string, percorre cada digito, converte para int e soma
        return soma                                            # retorna a soma dos digitos
    else:
        return -1                                              # retorna -1 se o numero estiver fora do intervalo

# funcao principal que coordena a leitura e o calculo
def main():
    numero = numero_entrada()        # le o numero da entrada
    if numero is not None:           # verifica se a leitura foi bem-sucedida
        resultado = soma_digitos(numero)   # calcula a soma dos digitos
        print(resultado)                   # exibe o resultado

# ponto de entrada: executa apenas quando rodado diretamente
if __name__ == "__main__":
    main()    # chama a funcao principal