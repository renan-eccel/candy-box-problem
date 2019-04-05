import pyomo.environ as poe

modelo = poe.AbstractModel()

# criancas
modelo.P = poe.RangeSet(1, 2)
# bombons
modelo.B = poe.Set()

# gostosura dos bonbons
modelo.c = poe.Param(modelo.B, within=poe.NonNegativeReals)

# variavel de decisao: 1, se o bombom i for para a crianca j
#                      0, caso contrario
modelo.x = poe.Var(modelo.B, modelo.P, within=poe.Binary)

# variavel auxiliar
modelo.z = poe.Var(within=poe.NonNegativeReals)


def funcao_objetivo(modelo):
    return modelo.z


modelo.OBJ = poe.Objective(rule=funcao_objetivo)


def funcao_restricao_de_particionamento(modelo, i):
    return sum(modelo.x[i, j] for j in modelo.P) == 1


def funcao_restricao_auxiliar_positiva(modelo):
    return (sum(modelo.c[i] * modelo.x[i, 1] for i in modelo.B)
            - sum(modelo.c[i] * modelo.x[i, 2] for i in modelo.B) <= modelo.z)


def funcao_restricao_auxiliar_negativa(modelo):
    return (- sum(modelo.c[i] * modelo.x[i, 1] for i in modelo.B)
            + sum(modelo.c[i] * modelo.x[i, 2] for i in modelo.B) <= modelo.z)


# cria uma restricao de particionamento para cada bombom
modelo.restricaoDeParticionamento = poe.Constraint(
    modelo.B, rule=funcao_restricao_de_particionamento
)

modelo.restricaoAuxiliarPositiva = poe.Constraint(
    rule=funcao_restricao_auxiliar_positiva
)

modelo.restricaoAuxiliarNegativa = poe.Constraint(
    rule=funcao_restricao_auxiliar_negativa
)
