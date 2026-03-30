# Escreva um programa que leia o numero de matricula de um aluno, suas notas em 3 provas e a media das notas obtidas nos exercicios que fazem parte da sua avaliacao. Calcule a media final usando a formula:

# Media Final = (Nota 1 + Nota 2 * 2 + Nota 3 * 3 + Media Exercicios) / 7

# A atribuicao dos conceitos obedece a tabela abaixo.

# Conceito  Media Final
# A  >= 9.0
# B  >= 7.5 e < 9.0
# C  >= 6.0 e < 7.5
# D  >= 4.0 e < 6.0
# E  < 4.0
# O programa deve escrever a matricula do aluno, a media final, o conceito correspondente e a mensagem "Aprovado" se o conceito for A, B ou C ou "Reprovado" se o conceito for D ou E.

# Mensagem  Conceitos
# Aprovado  A, B ou C
# Reprovado D ou E

# funcao que le a matricula do aluno como string (aceita letras e numeros)
def ler_matricula():
    matricula = input()    # le a matricula digitada pelo usuario
    return matricula       # retorna o valor lido sem conversao

# funcao que le e valida a nota de uma prova; recebe o numero da prova como parametro
def ler_nota(prova_numero):
    try:
        nota = float(input())        # le a nota e converte para numero decimal
        if 0 <= nota <= 10:          # verifica se a nota esta entre 0 e 10
            return nota              # retorna a nota se for valida
        else:
            print("Valor invalido. Por favor, digite uma nota entre 0 e 10.")
            return None              # retorna None se estiver fora do intervalo
    except ValueError:               # captura erro se a entrada nao for numerica
        print("Valor invalido. Por favor, digite um numero para a nota.")
        return None                  # retorna None em caso de erro

# funcao que le e valida a media dos exercicios
def ler_media_exercicios():
    try:
        media_exercicios = float(input())    # le a media e converte para decimal
        if 0 <= media_exercicios <= 10:      # verifica se esta no intervalo valido
            return media_exercicios          # retorna a media se for valida
        else:
            print("Valor invalido. Por favor, digite uma media entre 0 e 10.")
            return None                      # retorna None se fora do intervalo
    except ValueError:                       # captura erro se entrada nao for numerica
        print("Valor invalido. Por favor, digite um numero para a media dos exercicios.")
        return None                          # retorna None em caso de erro

# funcao que calcula a media final usando a formula ponderada do enunciado
def calcular_media_final(nota1, nota2, nota3, media_exercicios):
    media_final = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7  # aplica a formula: N1 + N2*2 + N3*3 + ME, dividido por 7
    return media_final    # retorna o resultado da media final

# funcao que atribui o conceito com base na media final
def atribuir_conceito(media_final):
    if media_final >= 9.0:       # media >= 9.0 recebe conceito A
        return "A"
    elif media_final >= 7.5:     # media entre 7.5 e 8.9 recebe conceito B
        return "B"
    elif media_final >= 6.0:     # media entre 6.0 e 7.4 recebe conceito C
        return "C"
    elif media_final >= 4.0:     # media entre 4.0 e 5.9 recebe conceito D
        return "D"
    else:                        # media abaixo de 4.0 recebe conceito E
        return "E"

# funcao que determina a situacao do aluno com base no conceito
def determinar_situacao(conceito):
    if conceito in ["A", "B", "C"]:  # conceitos A, B ou C resultam em aprovacao
        return "Aprovado"
    else:                             # conceitos D ou E resultam em reprovacao
        return "Reprovado"

# funcao principal que coordena todas as etapas do programa
def main():
    matricula = ler_matricula()      # le a matricula do aluno
    if matricula is not None:        # verifica se a matricula foi lida com sucesso
        nota1 = ler_nota(1)          # le a nota da prova 1
        nota2 = ler_nota(2)          # le a nota da prova 2
        nota3 = ler_nota(3)          # le a nota da prova 3
        media_exercicios = ler_media_exercicios()  # le a media dos exercicios

        if None not in (nota1, nota2, nota3, media_exercicios):  # verifica se todos os valores sao validos
            media_final = calcular_media_final(nota1, nota2, nota3, media_exercicios)  # calcula a media final
            conceito = atribuir_conceito(media_final)    # determina o conceito correspondente
            situacao = determinar_situacao(conceito)     # determina se esta aprovado ou reprovado

            print(matricula)              # imprime a matricula do aluno
            print(f"{media_final:.2f}")   # imprime a media final com 2 casas decimais
            print(conceito)               # imprime o conceito obtido
            print(situacao)               # imprime "Aprovado" ou "Reprovado"

# ponto de entrada: executa o programa apenas quando rodado diretamente
if __name__ == "__main__":
    main()  # chama a funcao principal