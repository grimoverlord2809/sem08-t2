# Documentacao — sem-08-02

Documentacao completa de todas as questoes do seminario 08-02.

---

## Q1 — Par ou Impar: Soma Condicional

### Enunciado
Leia um numero inteiro. Some 5 se for par ou some 8 se for impar. Mostre o resultado.

### Logica
- Se `numero % 2 == 0` → numero e par → resultado = numero + 5
- Caso contrario → numero e impar → resultado = numero + 8

### Exemplo

| Entrada | Saida |
|---------|-------|
| 4       | 9     |
| 7       | 15    |

### Codigo Comentado

```python
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
```

---

## Q2 — Soma dos Digitos

### Enunciado
Leia um numero inteiro. Mostre a soma dos digitos se estiver entre 0 e 100000, ou -1 caso contrario.

### Logica
- Se `0 <= numero <= 100000` → converte para string → soma cada digito
- Caso contrario → retorna -1

### Exemplo

| Entrada | Calculo              | Saida |
|---------|----------------------|-------|
| 16759   | 1+6+7+5+9            | 28    |
| 136759  | fora do intervalo    | -1    |
| -100    | negativo             | -1    |
| 100000  | 1+0+0+0+0+0          | 1     |

### Funcoes

| Funcao            | Descricao                                              |
|-------------------|--------------------------------------------------------|
| `numero_entrada()` | Le e converte a entrada para inteiro; retorna None se invalido |
| `soma_digitos(n)`  | Calcula a soma dos digitos ou retorna -1               |
| `main()`           | Coordena leitura e exibicao do resultado               |

### Codigo Comentado

```python
def numero_entrada():
    try:
        numero = int(input())    # le a entrada e converte para inteiro
        return numero            # retorna o numero lido
    except ValueError:           # captura erro se a entrada nao for numerica
        print("Valor invalido. Por favor, digite um numero inteiro.")
        return None              # retorna None em caso de erro

def soma_digitos(numero):
    if 0 <= numero <= 100000:                                  # verifica se o numero esta entre 0 e 100000
        soma = sum(int(digito) for digito in str(numero))      # converte para string, percorre cada digito e soma
        return soma                                            # retorna a soma dos digitos
    else:
        return -1                                              # retorna -1 se fora do intervalo

def main():
    numero = numero_entrada()        # le o numero da entrada
    if numero is not None:           # verifica se a leitura foi bem-sucedida
        resultado = soma_digitos(numero)   # calcula a soma dos digitos
        print(resultado)                   # exibe o resultado

if __name__ == "__main__":
    main()    # chama a funcao principal
```

---

## Q3 — FizzBuzz

### Enunciado
Leia um numero inteiro positivo e escreva:
- `FIZZBUZZ` se divisivel por 3 e por 5
- `FIZZ` se divisivel apenas por 3
- `BUZZ` se divisivel apenas por 5
- O proprio numero nos demais casos

### Regras de Divisibilidade

| Condicao                   | Saida    |
|----------------------------|----------|
| divisivel por 3 e por 5    | FIZZBUZZ |
| divisivel apenas por 3     | FIZZ     |
| divisivel apenas por 5     | BUZZ     |
| nenhuma das anteriores     | numero   |

### Exemplo

| Entrada | Saida    |
|---------|----------|
| 15      | FIZZBUZZ |
| 9       | FIZZ     |
| 10      | BUZZ     |
| 7       | 7        |

### Funcoes

| Funcao                  | Descricao                                              |
|-------------------------|--------------------------------------------------------|
| `ler_numero_inteiro()`  | Le, converte e valida (positivo); retorna None se invalido |
| `fizz_buzz(numero)`     | Aplica as regras e retorna a string correta            |
| `main()`                | Coordena leitura e exibicao                           |

### Codigo Comentado

```python
def ler_numero_inteiro():
    try:
        numero = int(input())       # le a entrada e converte para inteiro
        if numero < 0:              # verifica se o numero e negativo
            print("Valor invalido. Por favor, digite um numero inteiro positivo.")
            return None             # retorna None se negativo
        return numero               # retorna o numero se valido
    except ValueError:              # captura erro se entrada nao for numerica
        print("Valor invalido. Por favor, digite um numero inteiro.")
        return None                 # retorna None em caso de erro

def fizz_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:   # divisivel por 3 E 5
        return "FIZZBUZZ"
    elif numero % 3 == 0:                       # divisivel apenas por 3
        return "FIZZ"
    elif numero % 5 == 0:                       # divisivel apenas por 5
        return "BUZZ"
    else:
        return str(numero)                      # retorna o proprio numero

def main():
    numero = ler_numero_inteiro()     # le o numero
    if numero is not None:            # verifica validade
        resultado = fizz_buzz(numero) # aplica as regras
        print(resultado)              # exibe o resultado

if __name__ == "__main__":
    main()
```

---

## Q4 — Peso Ideal

### Enunciado
Leia a altura e o sexo de uma pessoa (1 = homem, 2 = mulher) e calcule o peso ideal com 2 casas decimais.

**Formulas:**
- Homem: `(72.7 * altura) - 58`
- Mulher: `(62.1 * altura) - 44.7`

### Exemplo

| Altura | Sexo | Saida  |
|--------|------|--------|
| 1.75   | 1    | 69.23  |
| 1.65   | 2    | 57.77  |

### Funcoes

| Funcao                             | Descricao                                              |
|------------------------------------|--------------------------------------------------------|
| `calcular_peso_ideal(altura, sexo)` | Aplica a formula correta e retorna o peso arredondado |
| `main()`                           | Le altura e sexo, chama o calculo e exibe o resultado |

### Codigo Comentado

```python
def calcular_peso_ideal(altura, sexo):
    if sexo == 1:                              # sexo masculino
        peso_ideal = (72.7 * altura) - 58      # formula para homens
    elif sexo == 2:                            # sexo feminino
        peso_ideal = (62.1 * altura) - 44.7    # formula para mulheres
    else:
        raise ValueError()                     # lanca excecao se sexo invalido
    return round(peso_ideal, 2)                # arredonda para 2 casas decimais

def main():
    try:
        altura = float(input())                # le a altura
        sexo = int(input())                    # le o sexo (1 ou 2)
        peso_ideal = calcular_peso_ideal(altura, sexo)   # calcula
        print(f"{peso_ideal:.2f}")             # exibe com 2 casas decimais
    except ValueError as e:
        print(e)                               # exibe erro se entrada invalida

if __name__ == "__main__":
    main()
```

---

## Q5 — Media Final e Conceito do Aluno

### Enunciado
Leia a matricula do aluno, notas de 3 provas e a media dos exercicios. Calcule a media final e exiba matricula, media, conceito e situacao.

**Formula:**

```
Media Final = (Nota1 + Nota2 * 2 + Nota3 * 3 + Media Exercicios) / 7
```

### Tabela de Conceitos

| Conceito | Media Final       |
|----------|-------------------|
| A        | >= 9.0            |
| B        | >= 7.5 e < 9.0    |
| C        | >= 6.0 e < 7.5    |
| D        | >= 4.0 e < 6.0    |
| E        | < 4.0             |

### Tabela de Situacao

| Situacao  | Conceitos  |
|-----------|------------|
| Aprovado  | A, B ou C  |
| Reprovado | D ou E     |

### Exemplo

**Entrada:**
```
2028211MTDS9877
9.86
10.00
6.15
8.50
```

**Saida:**
```
2028211MTDS9877
8.12
B
Aprovado
```

**Calculo:** (9.86 + 10.00*2 + 6.15*3 + 8.50) / 7 = 56.81 / 7 = 8.12

### Funcoes

| Funcao                                           | Descricao                                              |
|--------------------------------------------------|--------------------------------------------------------|
| `ler_matricula()`                                | Le a matricula como string (aceita alfanumerico)       |
| `ler_nota(prova_numero)`                         | Le e valida nota entre 0 e 10                         |
| `ler_media_exercicios()`                         | Le e valida media entre 0 e 10                        |
| `calcular_media_final(n1, n2, n3, me)`           | Aplica a formula ponderada                            |
| `atribuir_conceito(media_final)`                 | Retorna o conceito A-E                                |
| `determinar_situacao(conceito)`                  | Retorna Aprovado ou Reprovado                         |
| `main()`                                         | Coordena todas as etapas                              |

### Codigo Comentado

```python
def ler_matricula():
    matricula = input()    # le a matricula como string
    return matricula       # retorna sem conversao

def ler_nota(prova_numero):
    try:
        nota = float(input())        # le e converte para decimal
        if 0 <= nota <= 10:          # valida intervalo
            return nota              # retorna nota valida
        else:
            print("Valor invalido. Por favor, digite uma nota entre 0 e 10.")
            return None              # retorna None se invalida
    except ValueError:
        print("Valor invalido. Por favor, digite um numero para a nota.")
        return None

def ler_media_exercicios():
    try:
        media_exercicios = float(input())    # le e converte para decimal
        if 0 <= media_exercicios <= 10:      # valida intervalo
            return media_exercicios          # retorna media valida
        else:
            print("Valor invalido. Por favor, digite uma media entre 0 e 10.")
            return None
    except ValueError:
        print("Valor invalido. Por favor, digite um numero para a media dos exercicios.")
        return None

def calcular_media_final(nota1, nota2, nota3, media_exercicios):
    media_final = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7  # formula ponderada
    return media_final    # retorna a media final

def atribuir_conceito(media_final):
    if media_final >= 9.0:       # conceito A
        return "A"
    elif media_final >= 7.5:     # conceito B
        return "B"
    elif media_final >= 6.0:     # conceito C
        return "C"
    elif media_final >= 4.0:     # conceito D
        return "D"
    else:                        # conceito E
        return "E"

def determinar_situacao(conceito):
    if conceito in ["A", "B", "C"]:  # aprovado
        return "Aprovado"
    else:                             # reprovado
        return "Reprovado"

def main():
    matricula = ler_matricula()      # le a matricula
    if matricula is not None:        # verifica validade
        nota1 = ler_nota(1)          # le nota 1
        nota2 = ler_nota(2)          # le nota 2
        nota3 = ler_nota(3)          # le nota 3
        media_exercicios = ler_media_exercicios()  # le media dos exercicios
        if None not in (nota1, nota2, nota3, media_exercicios):  # verifica se tudo e valido
            media_final = calcular_media_final(nota1, nota2, nota3, media_exercicios)
            conceito = atribuir_conceito(media_final)    # determina o conceito
            situacao = determinar_situacao(conceito)     # determina situacao
            print(matricula)              # exibe matricula
            print(f"{media_final:.2f}")   # exibe media com 2 casas
            print(conceito)               # exibe conceito
            print(situacao)               # exibe situacao

if __name__ == "__main__":
    main()
```#   s e m 0 8 - t 2  
 