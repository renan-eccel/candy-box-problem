from __future__ import division
import pyomo.environ as poe

model = poe.AbstractModel()

# partitions
model.I = poe.RangeSet(1, 2)
# items
model.J = poe.Set()

# items cost
model.c = poe.Param(model.J, within=poe.NonNegativeReals)

# decision variable: 1, if item j is in partition i
#                    0, otherwise
model.x = poe.Var(model.I, model.J, within=poe.NonNegativeIntegers)

# auxiliar variable
model.z = poe.Var(within=poe.NonNegativeReals)


def objective_expression(model):
    return model.z


model.OBJ = poe.Objective(rule=objective_expression)


def covering_constraint_rule(model, j):
    '''
    return the expression for the constraint of j
    '''
    return sum(model.x[i, j] for i in model.I) == 1


def auxiliar_positive_constraint_rule(model):
    '''
    return the expression for the auxiliar constraint
    '''
    return (sum(model.c[j] * model.x[1, j] for j in model.J)
            - sum(model.c[j] * model.x[2, j] for j in model.J) <= model.z)


def auxiliar_negative_constraint_rule(model):
    '''
    return the expression for the auxiliar constraint
    '''
    return (- sum(model.c[j] * model.x[1, j] for j in model.J)
            + sum(model.c[j] * model.x[2, j] for j in model.J) <= model.z)


# the next line creates one constraint for each member of the set model.J
model.coverConstraint = poe.Constraint(model.J, rule=covering_constraint_rule)

# the next line creates the positive auxiliar constraint
model.auxiliarPositiveConstraint = poe.Constraint(
    rule=auxiliar_positive_constraint_rule
)

# the next line creates the negative auxiliar constraint
model.auxiliarNegativeConstraint = poe.Constraint(
    rule=auxiliar_negative_constraint_rule
)
