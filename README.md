# 📚 sem-08-02 — Exercícios de Lógica em Python

Repositório com as soluções comentadas dos exercícios da semana 08, turma 02.
Cada questão utiliza funções e estruturas condicionais, **sem laços de repetição**.

---

## 🗂️ Índice

- [Q1 — Par ou Ímpar](#q1--par-ou-ímpar-soma-condicional)
- [Q2 — Soma dos Dígitos](#q2--soma-dos-dígitos)
- [Q3 — FizzBuzz](#q3--fizzbuzz)
- [Q4 — Peso Ideal](#q4--peso-ideal)
- [Q5 — Média Final e Conceito](#q5--média-final-e-conceito-do-aluno)

---

## Q1 — Par ou Ímpar: Soma Condicional

> Leia um número inteiro. Some **5** se for par ou **8** se for ímpar. Mostre o resultado.

### Lógica

| Condição          | Operação        |
|-------------------|-----------------|
| `numero % 2 == 0` | resultado = n + 5 |
| ímpar             | resultado = n + 8 |

### Exemplo

| Entrada | Saída |
|---------|-------|
| 4       | 9     |
| 7       | 15    |

### Código

```python
def ler_numero_inteiro():
    numero = int(input())    # lê a entrada e converte para inteiro
    return numero            # retorna o número lido

try:
    numero = ler_numero_inteiro()    # chama a função para ler o número
    if numero % 2 == 0:              # verifica se o número é par
        resultado = numero + 5       # se par, soma 5
    else:                            # caso contrário, é ímpar
        resultado = numero + 8       # se ímpar, soma 8
    print(resultado)                 # exibe o resultado
except ValueError:                   # captura erro se entrada não for inteiro
    print("Valor inválido. Por favor, digite um número inteiro.")
```

---

## Q2 — Soma dos Dígitos

> Leia um número inteiro. Mostre a **soma dos dígitos** se estiver entre 0 e 100 000, ou **-1** caso contrário.

### Lógica

- Se `0 <= numero <= 100000` → converte para string → soma cada dígito
- Caso contrário → retorna `-1`

### Exemplo

| Entrada | Cálculo       | Saída |
|---------|---------------|-------|
| 16759   | 1+6+7+5+9     | 28    |
| 136759  | > 100 000     | -1    |
| -100    | negativo      | -1    |
| 100000  | 1+0+0+0+0+0   | 1     |

### Funções

| Função             | Descrição                                                    |
|--------------------|--------------------------------------------------------------|
| `numero_entrada()` | Lê e converte para inteiro; retorna `None` se inválido       |
| `soma_digitos(n)`  | Calcula a soma dos dígitos ou retorna `-1`                   |
| `main()`           | Coordena leitura e exibição do resultado                     |

### Código

```python
def numero_entrada():
    try:
        numero = int(input())    # lê e converte para inteiro
        return numero
    except ValueError:
        return None              # retorna None em caso de erro

def soma_digitos(numero):
    if 0 <= numero <= 100000:                              # intervalo válido
        soma = sum(int(d) for d in str(numero))            # soma cada dígito
        return soma
    else:
        return -1                                          # fora do intervalo

def main():
    numero = numero_entrada()
    if numero is not None:
        print(soma_digitos(numero))

if __name__ == "__main__":
    main()
```

---

## Q3 — FizzBuzz

> Leia um número inteiro positivo e escreva:
> - `FIZZBUZZ` — divisível por 3 **e** por 5
> - `FIZZ` — divisível apenas por 3
> - `BUZZ` — divisível apenas por 5
> - O próprio número — demais casos

### Regras

| Condição                | Saída    |
|-------------------------|----------|
| `n % 3 == 0 and n % 5 == 0` | FIZZBUZZ |
| `n % 3 == 0`            | FIZZ     |
| `n % 5 == 0`            | BUZZ     |
| nenhuma das anteriores  | n        |

### Exemplo

| Entrada | Saída    |
|---------|----------|
| 15      | FIZZBUZZ |
| 9       | FIZZ     |
| 10      | BUZZ     |
| 7       | 7        |

### Funções

| Função                 | Descrição                                                  |
|------------------------|------------------------------------------------------------|
| `ler_numero_inteiro()` | Lê, converte e valida (positivo); retorna `None` se inválido |
| `fizz_buzz(numero)`    | Aplica as regras e retorna a string correta                |
| `main()`               | Coordena leitura e exibição                               |

### Código

```python
def ler_numero_inteiro():
    try:
        numero = int(input())        # lê e converte para inteiro
        if numero < 0:               # rejeita negativos
            return None
        return numero
    except ValueError:
        return None

def fizz_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:   # divisível por 3 e 5
        return "FIZZBUZZ"
    elif numero % 3 == 0:                       # divisível apenas por 3
        return "FIZZ"
    elif numero % 5 == 0:                       # divisível apenas por 5
        return "BUZZ"
    else:
        return str(numero)                      # retorna o próprio número

def main():
    numero = ler_numero_inteiro()
    if numero is not None:
        print(fizz_buzz(numero))

if __name__ == "__main__":
    main()
```

---

## Q4 — Peso Ideal

> Leia a **altura** e o **sexo** de uma pessoa (`1` = homem, `2` = mulher).
> Calcule e mostre o peso ideal com 2 casas decimais.

### Fórmulas

| Sexo   | Fórmula                        |
|--------|--------------------------------|
| Homem  | `(72.7 × altura) − 58`         |
| Mulher | `(62.1 × altura) − 44.7`       |

### Exemplo

| Altura | Sexo | Saída |
|--------|------|-------|
| 1.75   | 1    | 69.23 |
| 1.65   | 2    | 57.77 |

### Funções

| Função                              | Descrição                                          |
|-------------------------------------|----------------------------------------------------|
| `calcular_peso_ideal(altura, sexo)` | Aplica a fórmula e retorna o peso arredondado      |
| `main()`                            | Lê os dados, chama o cálculo e exibe o resultado   |

### Código

```python
def calcular_peso_ideal(altura, sexo):
    if sexo == 1:                              # homem
        peso_ideal = (72.7 * altura) - 58
    elif sexo == 2:                            # mulher
        peso_ideal = (62.1 * altura) - 44.7
    else:
        raise ValueError()                     # sexo inválido
    return round(peso_ideal, 2)                # arredonda para 2 casas

def main():
    try:
        altura = float(input())                # lê a altura
        sexo   = int(input())                  # lê o sexo (1 ou 2)
        print(f"{calcular_peso_ideal(altura, sexo):.2f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```

---

## Q5 — Média Final e Conceito do Aluno

> Leia a matrícula, notas de 3 provas e a média dos exercícios.
> Calcule a média final e exiba matrícula, média, conceito e situação.

### Fórmula

$$
\text{Média Final} = \frac{N_1 + N_2 \times 2 + N_3 \times 3 + \text{ME}}{7}
$$

### Tabela de Conceitos

| Conceito | Média Final        |
|----------|--------------------|
| A        | ≥ 9,0              |
| B        | ≥ 7,5 e < 9,0      |
| C        | ≥ 6,0 e < 7,5      |
| D        | ≥ 4,0 e < 6,0      |
| E        | < 4,0              |

### Tabela de Situação

| Situação  | Conceitos |
|-----------|-----------|
| Aprovado  | A, B ou C |
| Reprovado | D ou E    |

### Exemplo

**Entrada:**
```
2028211MTDS9877
9.86
10.00
6.15
8.50
```

**Saída:**
```
2028211MTDS9877
8.12
B
Aprovado
```

> **Cálculo:** (9,86 + 10,00×2 + 6,15×3 + 8,50) ÷ 7 = 56,81 ÷ 7 ≈ **8,12**

### Funções

| Função                               | Descrição                                          |
|--------------------------------------|----------------------------------------------------|
| `ler_matricula()`                    | Lê a matrícula como string (aceita alfanumérico)   |
| `ler_nota(prova_numero)`             | Lê e valida nota entre 0 e 10                      |
| `ler_media_exercicios()`             | Lê e valida média entre 0 e 10                     |
| `calcular_media_final(n1,n2,n3,me)`  | Aplica a fórmula ponderada                         |
| `atribuir_conceito(media_final)`     | Retorna o conceito (A–E)                           |
| `determinar_situacao(conceito)`      | Retorna Aprovado ou Reprovado                      |
| `main()`                             | Coordena todas as etapas                           |

### Código

```python
def ler_matricula():
    return input()              # lê como string (aceita letras e números)

def ler_nota(prova_numero):
    try:
        nota = float(input())   # lê e converte para decimal
        if 0 <= nota <= 10:
            return nota         # nota válida
        return None             # fora do intervalo
    except ValueError:
        return None

def ler_media_exercicios():
    try:
        me = float(input())     # lê e converte para decimal
        if 0 <= me <= 10:
            return me           # média válida
        return None
    except ValueError:
        return None

def calcular_media_final(nota1, nota2, nota3, me):
    return (nota1 + nota2 * 2 + nota3 * 3 + me) / 7   # fórmula ponderada

def atribuir_conceito(media):
    if media >= 9.0:   return "A"
    elif media >= 7.5: return "B"
    elif media >= 6.0: return "C"
    elif media >= 4.0: return "D"
    else:              return "E"

def determinar_situacao(conceito):
    return "Aprovado" if conceito in ["A", "B", "C"] else "Reprovado"

def main():
    matricula = ler_matricula()
    if matricula is not None:
        n1 = ler_nota(1)
        n2 = ler_nota(2)
        n3 = ler_nota(3)
        me = ler_media_exercicios()
        if None not in (n1, n2, n3, me):
            media   = calcular_media_final(n1, n2, n3, me)
            conceito = atribuir_conceito(media)
            print(matricula)
            print(f"{media:.2f}")
            print(conceito)
            print(determinar_situacao(conceito))

if __name__ == "__main__":
    main()
```

---

> **Repositório:** [grimoverlord2809/sem08-t2](https://github.com/grimoverlord2809/sem08-t2)