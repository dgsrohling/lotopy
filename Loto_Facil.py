import pandas as pd
import random
from datetime import datetime

# Carrega o histórico da Lotofácil
df = pd.read_csv("data/lotofacil_numeros_sorteados.csv", header=None)
sorted_existing = set(tuple(sorted(row)) for row in df.values)

# Frequência dos números sorteados
all_numbers = df.values.flatten()
frequency = pd.Series(all_numbers).value_counts().sort_values(ascending=False)

# Define os grupos estratégicos
top_numbers = frequency.head(20).index.tolist()
bottom_numbers = frequency.tail(20).index.tolist()
todos_numeros = list(range(1, 26))

# Valida se uma sequência segue os critérios estratégicos
def is_valid_sequence(sequence):
    sequence = sorted(sequence)

    # Evita 3 ou mais números consecutivos
    for i in range(len(sequence) - 2):
        if sequence[i] + 1 == sequence[i + 1] and sequence[i + 1] + 1 == sequence[i + 2]:
            return False

    # Evita todos pares ou todos ímpares
    even_count = sum(1 for num in sequence if num % 2 == 0)
    if even_count == 0 or even_count == 15:
        return False

    # Garante distribuição entre 1–13 e 14–25
    low_count = sum(1 for num in sequence if num <= 13)
    high_count = 15 - low_count
    if low_count == 0 or high_count == 0:
        return False

    return True

# Geração de sequência com estratégia + proteção contra loops
def generate_sequence(tipo):
    tentativas = 0
    max_tentativas = 1000

    while tentativas < max_tentativas:
        tentativas += 1

        if tipo == 1:
            top_sample = random.sample(top_numbers, 10)
            restante = list(set(todos_numeros) - set(top_sample))
            aleatorios = random.sample(restante, 5)
            sequence = sorted(top_sample + aleatorios)

        elif tipo == 2:
            bottom_sample = random.sample(bottom_numbers, 8)
            restante = list(set(todos_numeros) - set(bottom_sample))
            aleatorios = random.sample(restante, 7)
            sequence = sorted(bottom_sample + aleatorios)

        elif tipo == 3:
            sequence = sorted(random.sample(todos_numeros, 15))

        elif tipo == 4:
            top_sample = random.sample(top_numbers, 5)
            bottom_sample = random.sample(bottom_numbers, 5)

            # Garante que todos os números da sequência sejam únicos
            base_set = set()
            top_sample = random.sample(top_numbers, 5)
            base_set.update(top_sample)

            bottom_sample = random.sample([n for n in bottom_numbers if n not in base_set], 5)
            base_set.update(bottom_sample)

            restante = list(set(todos_numeros) - base_set)
            if len(restante) < 5:
                continue  # pula essa tentativa, pois não é possível formar uma sequência válida

            restante_sample = random.sample(restante, 5)
            sequence = sorted(top_sample + bottom_sample + restante_sample)

        else:
            sequence = sorted(random.sample(todos_numeros, 15))

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

# Gera os jogos
jogos = []
for _ in range(qtd):
    seq = generate_sequence(tipo)
    if seq is None:
        jogos.append((["ERRO"], "(erro ao gerar sequência)"))
    else:
        ja_sorteado = " (já foi sorteado)" if tuple(seq) in sorted_existing else " (inédito)"
        jogos.append((seq, ja_sorteado))

# Exibe no terminal
print("\nJogos gerados:")
for i, (seq, status) in enumerate(jogos, start=1):
    print(f"Jogo {i}: {','.join(map(str, seq))}{status}")

# Salva em arquivo TXT com timestamp
agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"loto_facil_resultados_{agora}.txt"
with open(filename, "w") as file:
    for seq, _ in jogos:
        file.write(",".join(map(str, seq)) + "\n")

print(f"\nAs {qtd} sequências foram salvas em '{filename}'.")
