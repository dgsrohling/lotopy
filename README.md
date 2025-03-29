# 🎲 Gerador Estratégico de Jogos - Lotofácil e Mega-Sena

Este projeto contém dois scripts Python que geram jogos estratégicos para as loterias **Lotofácil** e **Mega-Sena** com base em análise de frequência dos números sorteados. Os jogos seguem regras inteligentes que evitam combinações improváveis, como números repetidos, todos pares ou ímpares, ou muitos números consecutivos.

## 📂 Estrutura do Projeto

```
.
├── Mega_Sena.py
├── Loto_Facil.py
└── data/
    ├── mega_sena_numeros_sorteados.csv
    └── lotofacil_numeros_sorteados.csv
```

---

## 📥 Atualizando os Arquivos CSV com Resultados Oficiais

Antes de rodar os scripts, baixe os arquivos `.xlsx` com os resultados atualizados das loterias e converta-os para `.csv`:

### 🔹 Lotofácil
- Acesse: [https://asloterias.com.br/download-todos-resultados-lotofacil](https://asloterias.com.br/download-todos-resultados-lotofacil)
- Clique em **Baixar Resultados**
- Edite o arquivo .xlsx deixando apenas as colunas com os números
- Salve o arquivo como `lotofacil_numeros_sorteados.csv`
- Mova o arquivo para a pasta `data/`

### 🔹 Mega-Sena
- Acesse: [https://asloterias.com.br/download-todos-resultados-mega-sena](https://asloterias.com.br/download-todos-resultados-mega-sena)
- Clique em **Baixar Resultados**
- Edite o arquivo .xlsx deixando apenas as colunas com os números
- Salve o arquivo como `mega_sena_numeros_sorteados.csv`
- Mova o arquivo para a pasta `data/`

---

## 🚀 Como Executar os Scripts

### Pré-requisitos

- Python 3.6 ou superior
- Pandas instalado:
```bash
pip install pandas
```

---

### 🎰 Gerando Jogos para a Lotofácil

Execute no terminal:

```bash
python3 Loto_Facil.py
```

Você será perguntado:

```text
Quantos jogos você deseja gerar?
Como deseja gerar os jogos?
1 - Mais sorteados
2 - Menos sorteados
3 - Aleatórios
4 - Surpresa (estratégico)
```

Cada jogo terá 15 números, validados com as seguintes regras:

- Sem 3 ou mais números consecutivos
- Não permite todos pares ou ímpares
- Deve ter números da faixa 1–13 e 14–25
- Não repete combinações anteriores do histórico
- Todos os números são únicos

---

### 💰 Gerando Jogos para a Mega-Sena

Execute no terminal:

```bash
python3 Mega_Sena.py
```

Você verá opções semelhantes:

```text
Quantos jogos você deseja gerar?
Como deseja gerar os jogos?
1 - Mais sorteados
2 - Menos sorteados
3 - Aleatórios
4 - Surpresa (estratégico)
```

Cada jogo terá 6 números, validados com:

- Sem 3 ou mais números consecutivos
- Não permite todos pares ou ímpares
- Deve conter pelo menos 2 números ≤30 e 2 >30
- Sem repetições entre top, bottom e middle
- Todos os números são únicos

---

## 💾 Saída dos Jogos

Os jogos gerados serão:

- Exibidos no terminal
- Salvos em arquivos `.txt` com timestamp, por exemplo:  
  `loto_facil_resultados_2025-03-28_14-30-22.txt`  
  `mega_sena_resultados_2025-03-28_14-31-10.txt`

---

## 💡 Estratégias Inteligentes

Os modos estratégicos (opção 4) utilizam análise de frequência para equilibrar:

- Números mais sorteados
- Números menos sorteados
- Números aleatórios do meio da distribuição
- Evitando repetições e combinações ruins

---

## 🤝 Contribuições

Sinta-se à vontade para contribuir com melhorias, sugestões de novas estratégias ou visualizações estatísticas.

---

## ⚠️ Aviso Legal

Este projeto é apenas para fins de estudo, aprendizado e entretenimento. Não garante qualquer tipo de ganho financeiro. Jogue com responsabilidade!
