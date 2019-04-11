import pyomo.environ as poe

modelo = poe.AbstractModel()

modelo.criancas = poe.RangeSet(1, 2)
modelo.bombons = poe.Set()

# nivel de gostosura dos bombons
modelo.gostosura = poe.Param(modelo.bombons, within=poe.NonNegativeIntegers)

# variavel de decisao: 1, se o bombom i for para a crianca j
#                      0, caso contrario
modelo.x = poe.Var(modelo.bombons, modelo.criancas, within=poe.Binary)


def funcao_objetivo(modelo):
    return ((sum(modelo.gostosura[i] * modelo.x[i, 1]
                 for i in modelo.bombons)
             - sum(modelo.gostosura[i] * modelo.x[i, 2]
                   for i in modelo.bombons))**2)


modelo.OBJ = poe.Objective(rule=funcao_objetivo)


def funcao_restricao_de_particionamento(modelo, i):
    return modelo.x[i, 1] + modelo.x[i, 2] == 1


# cria uma restricao de cobertura para cada bombom
modelo.restricaoDeParticionamento = \
    poe.Constraint(modelo.bombons, rule=funcao_restricao_de_particionamento)
