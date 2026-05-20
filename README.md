# Aprendizado Relacional Estatistico
# Arquitetura Híbrida SRL – Prolog + Python

## Informações

- **Disciplina:** Inteligência Artificial
- **Professor:** Edjard Mota
- **Aluno:** Gabriel Yuri Cavalcante de Castro
- **Matrícula:** 22350996
- **Curso:** Engenharia da Computação – UFAM

---

## Descrição

Este projeto implementa uma arquitetura híbrida usando Prolog e Python para análise de risco de crédito em uma rede de transações.

A ideia principal é combinar dados financeiros tradicionais, como renda mensal e score clássico, com uma informação relacional calculada em Prolog: o grau de conexão de cada cliente com pessoas inadimplentes.

O Prolog é usado para representar a rede e calcular relações. O Python consulta essa base lógica com `pyswip`, monta a tabela com Pandas e treina um modelo de Regressão Logística com Scikit-Learn.

---

## Estrutura do Projeto

```text
arquitetura-hibrida-srl-python/
├── README.md
├── rede_social.pl
├── dados_financeiros.csv
├── main.py
└── requirements.txt
