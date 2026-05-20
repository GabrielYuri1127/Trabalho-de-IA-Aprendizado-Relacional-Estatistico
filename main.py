from pyswip import Prolog
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def obter_grau_risco(prolog, cliente):
    consulta = f"grau_risco_inadimplente({cliente}, Grau)"
    resultado = list(prolog.query(consulta))

    if resultado:
        return resultado[0]["Grau"]

    return 999


def main():
    prolog = Prolog()
    prolog.consult("rede_social.pl")

    df = pd.read_csv("dados_financeiros.csv")

    df["grau_risco_rede"] = df["cliente_id"].apply(
        lambda cliente: obter_grau_risco(prolog, cliente)
    )

    print("\nDados com atributo relacional:")
    print(df)

    X = df[["renda_mensal", "score_classico", "grau_risco_rede"]]
    y = df["inadimplente_historico"]

    modelo = Pipeline([
        ("padronizacao", StandardScaler()),
        ("regressao", LogisticRegression())
    ])

    modelo.fit(X, y)

    coeficientes = modelo.named_steps["regressao"].coef_[0]

    print("\nCoeficientes aprendidos:")
    for atributo, valor in zip(X.columns, coeficientes):
        print(f"{atributo}: {valor:.4f}")

    df["probabilidade_risco"] = modelo.predict_proba(X)[:, 1]

    print("\nProbabilidades estimadas:")
    print(df[["cliente_id", "grau_risco_rede", "probabilidade_risco"]])

    print("\nSaida no estilo ProbLog:")
    for _, linha in df.iterrows():
        cliente = linha["cliente_id"]
        grau = linha["grau_risco_rede"]
        prob = linha["probabilidade_risco"]

        if grau == 999:
            print(f"{prob:.2f} :: risco({cliente}) :- sem_conexao_com_inadimplente({cliente}).")
        else:
            print(f"{prob:.2f} :: risco({cliente}) :- conectado_a_inadimplente({cliente}, {grau}).")


if __name__ == "__main__":
    main()
