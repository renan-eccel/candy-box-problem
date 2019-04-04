import pyomo.environ as poe

modelo = poe.AbstractModel()

# criancas
modelo.P = poe.RangeSet(1, 2)
# bombons
modelo.B = poe.Set()

# nivel de gostosura dos bombons
modelo.c = poe.Param(modelo.B, within=poe.Binary)

# variavel de decisao: 1, se o bombom i for para a crianca j
#                      0, caso contrario
modelo.x = poe.Var(modelo.B, modelo.P, within=poe.NonNegativeIntegers)


def funcao_objetivo(modelo):
    return ((sum(modelo.c[i] * modelo.x[i, 1] for i in modelo.B)
             - sum(modelo.c[i] * modelo.x[i, 2] for i in modelo.B))**2)


modelo.OBJ = poe.Objective(rule=funcao_objetivo)


def funcao_restricao_de_cobertura(modelo, i):
    return modelo.x[i, 1] + modelo.x[i, 2] == 1


# cria uma restricao de cobertura para cada bombom
modelo.restricao_de_cobertura = \
    poe.Constraint(modelo.B, rule=funcao_restricao_de_cobertura)
