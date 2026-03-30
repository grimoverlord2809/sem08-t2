# Escreva um programa que leia a altura e o sexo de uma pessoa, considere 1 para homens e 2 para mulheres.
# Usando duas casas decimais, calcule e mostre o peso ideal utilizando as seguintes formulas:
# para homens: (72.7 * altura) - 58
# para mulheres: (62.1 * altura) - 44.7

# funcao que calcula o peso ideal com base na altura e no sexo
def calcular_peso_ideal(altura, sexo):
    if sexo == 1:                              # verifica se o sexo informado e masculino (1)
        peso_ideal = (72.7 * altura) - 58      # aplica a formula para homens
    elif sexo == 2:                            # verifica se o sexo informado e feminino (2)
        peso_ideal = (62.1 * altura) - 44.7    # aplica a formula para mulheres
    else:
        raise ValueError()                     # lanca excecao se o sexo nao for 1 ou 2
    return round(peso_ideal, 2)                # arredonda o resultado para 2 casas decimais e retorna

# funcao principal que coordena a leitura dos dados e exibicao do resultado
def main():
    try:
        altura = float(input())                # le a altura e converte para numero decimal
        sexo = int(input())                    # le o sexo e converte para inteiro (1 ou 2)
        peso_ideal = calcular_peso_ideal(altura, sexo)   # calcula o peso ideal
        print(f"{peso_ideal:.2f}")             # exibe o peso ideal com 2 casas decimais
    except ValueError as e:                    # captura erro de entrada invalida ou sexo invalido
        print(e)                               # exibe a mensagem de erro

# ponto de entrada: executa apenas quando rodado diretamente
if __name__ == "__main__":
    main()    # chama a funcao principal