% Base relacional da rede de transacoes financeiras

transacao_entre(joao, ana, 1500).
transacao_entre(ana, carlos, 800).
transacao_entre(carlos, daniel, 50).
transacao_entre(maria, joao, 600).
transacao_entre(lucas, maria, 400).
transacao_entre(beatriz, fernando, 900).
transacao_entre(fernando, daniel, 300).

inadimplente(daniel).
inadimplente(carlos).

conectado(X, Y) :-
    transacao_entre(X, Y, _).

conectado(X, Y) :-
    transacao_entre(Y, X, _).

risco_conexao(X, Y, Grau) :-
    risco_conexao(X, Y, [X], Grau).

risco_conexao(X, Y, _, 1) :-
    conectado(X, Y).

risco_conexao(X, Y, Visitados, Grau) :-
    conectado(X, Z),
    Z \== Y,
    \+ member(Z, Visitados),
    risco_conexao(Z, Y, [Z|Visitados], GrauAnterior),
    Grau is GrauAnterior + 1.

grau_risco_inadimplente(Cliente, GrauMinimo) :-
    findall(
        Grau,
        (
            inadimplente(Pessoa),
            Cliente \== Pessoa,
            risco_conexao(Cliente, Pessoa, Grau)
        ),
        Graus
    ),
    Graus \== [],
    min_list(Graus, GrauMinimo).
