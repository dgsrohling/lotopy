import pandas as pd
import random
from datetime import datetime

# Carrega histórico da Mega-Sena
df = pd.read_csv("data/mega_sena_numeros_sorteados.csv", header=None)
sorted_existing = set(tuple(sorted(row)) for row in df.values)

# Frequência dos números
all_numbers = df.values.flatten()
frequency = pd.Series(all_numbers).value_counts().sort_values(ascending=False)

# Define grupos
top_numbers = frequency.head(20).index.tolist()
bottom_numbers = frequency.tail(20).index.tolist()
todos_numeros = list(range(1, 61))

# Regras de validação da Mega-Sena
def is_valid_sequence(sequence):
    sequence = sorted(sequence)

    # Evita 3 ou mais números consecutivos
    for i in range(len(sequence) - 2):
        if sequence[i] + 1 == sequence[i + 1] and sequence[i + 1] + 1 == sequence[i + 2]:
            return False

    # Evita todos pares ou todos ímpares
    even = sum(1 for n in sequence if n % 2 == 0)
    if even == 0 or even == 6:
        return False

    # Garante pelo menos 2 números abaixo de 30 e 2 acima
    low = sum(1 for n in sequence if n <= 30)
    high = 6 - low
    if low < 2 or high < 2:
        return False

    return True

# Geração de sequência com proteção contra loops
def generate_sequence(tipo):
    tentativas = 0
    max_tentativas = 1000

    while tentativas < max_tentativas:
        tentativas += 1

        if tipo == 1:
            top_sample = random.sample(top_numbers, 4)
            restante = list(set(todos_numeros) - set(top_sample))
            extra = random.sample(restante, 2)
            sequence = sorted(top_sample + extra)

        elif tipo == 2:
            bottom_sample = random.sample(bottom_numbers, 4)
            restante = list(set(todos_numeros) - set(bottom_sample))
            extra = random.sample(restante, 2)
            sequence = sorted(bottom_sample + extra)

        elif tipo == 3:
            sequence = sorted(random.sample(todos_numeros, 6))

        elif tipo == 4:
            base_set = set()
            top = random.sample(top_numbers, 2)
            base_set.update(top)

            bottom = random.sample([n for n in bottom_numbers if n not in base_set], 2)
            base_set.update(bottom)

            middle_pool = list(set(todos_numeros) - base_set)
            if len(middle_pool) < 2:
                continue  # pula tentativa inválida

            middle = random.sample(middle_pool, 2)
            sequence = sorted(top + bottom + middle)

        else:
            sequence = sorted(random.sample(todos_numeros, 6))

        if is_valid_sequence(sequence):
            return sequence

    print("⚠️ Aviso: não foi possível gerar uma sequência válida após 1000 tentativas.")
    return None

# Interação com o usuário
try:
    qtd = int(input("Quantos jogos você deseja gerar? "))
except ValueError:
    print("Entrada inválida. Serão gerados 4 jogos por padrão.")
    qtd = 4

print("\nComo deseja gerar os jogos?")
print("1 - Mais sorteados")
print("2 - Menos sorteados")
print("3 - Aleatórios")
print("4 - Surpresa (estratégico)")
try:
    tipo = int(input("Escolha o modo (1-4): "))
    if tipo not in [1, 2, 3, 4]:
        raise ValueError
except ValueError:
    print("Opção inválida. Usando modo surpresa.")
    tipo = 4

# Geração dos jogos
jogos = []
for _ in range(qtd):
    seq = generate_sequence(tipo)
    if seq is None:
        jogos.append((["ERRO"], "(erro ao gerar sequência)"))
    else:
        ja_sorteado = " (já foi sorteado)" if tuple(seq) in sorted_existing else " (inédito)"
        jogos.append((seq, ja_sorteado))

# Exibe os jogos no terminal
print("\nJogos gerados:")
for i, (seq, status) in enumerate(jogos, start=1):
    print(f"Jogo {i}: {','.join(map(str, seq))}{status}")

# Salva os jogos em .txt com data e hora
agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"mega_sena_resultados_{agora}.txt"
with open(filename, "w") as file:
    for seq, _ in jogos:
        file.write(",".join(map(str, seq)) + "\n")

print(f"\nAs {qtd} sequências foram salvas em '{filename}'.")
