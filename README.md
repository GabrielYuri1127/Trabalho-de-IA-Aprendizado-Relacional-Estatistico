# Arquitetura Híbrida SRL – Prolog + Python

## Informações da Disciplina

- **Disciplina:** Inteligência Artificial
- **Professor:** Edjard Mota
- **Aluno:** Gabriel Yuri Cavalcante de Castro
- **Matrícula:** 22350996
- **Curso:** Engenharia da Computação – UFAM

---

## Objetivo

Desenvolver um sistema capaz de estimar o risco de inadimplência de clientes a partir de:

- atributos financeiros tradicionais, como renda mensal e score de crédito;
- informações relacionais obtidas de uma rede de transações financeiras.

A hipótese considerada é que clientes próximos de pessoas inadimplentes tendem a apresentar maior risco.

---

## Estrutura do Repositório

```text
arquitetura-hibrida-srl-python/
├── README.md
├── rede_social.pl
├── dados_financeiros.csv
├── main.py
└── requirements.txt
```

---

## Descrição dos Arquivos

### `rede_social.pl`

Contém a base relacional em Prolog, incluindo:

- transações financeiras entre clientes;
- clientes com histórico de inadimplência;
- regras de conectividade;
- cálculo recursivo do grau de proximidade.

### `dados_financeiros.csv`

Arquivo com os atributos financeiros tradicionais utilizados no modelo.

### `main.py`

Script principal responsável por:

1. carregar a base Prolog;
2. consultar o grau de risco de cada cliente;
3. enriquecer o conjunto de dados;
4. treinar uma Regressão Logística;
5. exibir probabilidades e regras probabilísticas.

### `requirements.txt`

Lista as bibliotecas necessárias para a execução do projeto.

---

## Implementação

### Base Relacional em Prolog

As relações entre clientes são representadas por fatos do tipo:

```prolog
transacao_entre(joao, ana, 1500).
```

Clientes inadimplentes são registrados por:

```prolog
inadimplente(daniel).
```

A regra `risco_conexao/3` calcula o número de conexões entre dois clientes, enquanto `grau_risco_inadimplente/2` determina a menor distância entre um cliente e qualquer inadimplente.

### Integração com Python

A biblioteca `pyswip` permite que o Python consulte o Prolog. Para cada cliente do arquivo CSV, é executada uma consulta para obter o valor de `grau_risco_rede`.

### Regressão Logística

O modelo utiliza três atributos:

- `renda_mensal`
- `score_classico`
- `grau_risco_rede`

Com base nesses valores, a Regressão Logística estima a probabilidade de inadimplência.

### Saída Probabilística

Após o treinamento, o sistema produz uma representação no estilo ProbLog, por exemplo:

```text
0.82 :: risco(joao) :- conectado_a_inadimplente(joao, 2).
```

---

## Etapas de Desenvolvimento

1. Definição da rede de transações em Prolog.
2. Modelagem dos clientes inadimplentes.
3. Implementação da regra recursiva de conectividade.
4. Criação do arquivo CSV com os dados financeiros.
5. Integração entre Python e Prolog.
6. Geração do atributo relacional `grau_risco_rede`.
7. Treinamento do modelo estatístico.
8. Geração das probabilidades e regras probabilísticas.

---

## Como Executar

### Instalação das Dependências

```bash
pip install -r requirements.txt
```

### Execução do Programa

```bash
python main.py
```

---

## Resultado Esperado

A execução do programa deve apresentar:

1. o conjunto de dados com a coluna `grau_risco_rede`;
2. os coeficientes aprendidos pela Regressão Logística;
3. as probabilidades estimadas de inadimplência;
4. regras probabilísticas no estilo ProbLog.

---

## Fundamentação Teórica

O projeto aplica conceitos de **Statistical Relational Learning (SRL)**, abordagem que combina:

- Lógica de Primeira Ordem (Prolog);
- Métodos estatísticos (Regressão Logística).

Essa integração permite representar relações complexas e produzir resultados probabilísticos interpretáveis.

---

## Observações

- O valor `999` indica que não foi encontrada conexão com clientes inadimplentes.
- Os valores de probabilidade podem variar de acordo com o treinamento.
- A saída final é explicável, pois associa probabilidades a regras lógicas.

---

## Referências

BRATKO, Ivan. *Prolog Programming for Artificial Intelligence*. 4th Edition.

Material da disciplina de Inteligência Artificial – Prof. Edjard Mota.
