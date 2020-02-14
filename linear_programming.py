from pulp import *
from fractions import Fraction

prob = LpProblem("Example of standard maximum problem", LpMaximize)

# nonnegativity constraints
x1 = LpVariable("x1", 0)
x2 = LpVariable("x2", 0)
x3 = LpVariable("x3", 0)
x4 = LpVariable("x4", 0)
x5 = LpVariable("x5", 0)
x6 = LpVariable("x6", 0)
x7 = LpVariable("x7", 0)
x8 = LpVariable("x8", 0)
x9 = LpVariable("x9", 0)

# objective function
prob += 0.08 * x1 + 0.12 * x2 + 0.13 * x3 + 0.25 * x4 + 0.45 * x5 + 0.13 * x6 + 0.13 * x7 + 0.13 * x8 + 0.14 * x9


prob += 6.8 * x1 + 7.16 * x2 + 7.22 * x3 + 7.75 * x4 + 8.2 * x5 + 7.22 * x6 + 7.29 * x7 + 7.08 * x8 + 7.19 * x9 <= 3610
prob += 0.3332 * x1 + 0.01432 * x2 - 0.0361 * x3 - 0.496 * x4 - 0.8938 * x5 - 0.02888 * x6 - 0.10206 * x7 + 0.08496 * x8 - 0.00719 * x9 == 0
prob += 0.77 * x1 + 0.67 * x2 + 0.61 * x3 + 0.38 * x4 + 0.59 * x6 + 0.57 * x7 + 0.7 * x8 + 0.62 * x9 <= 292
prob += -17 * x1 - 14 * x2 - 2 * x3 - 12 * x4 - 30 * x5 - 11 * x6 - 10 * x7 - 16 * x8 + 63 * x9 <= 0
prob += 1.1 * x1 + 0.1 * x2 - 0.35 * x3 - 1.64 * x4 - 1.877 * x5 + 0.64 * x6 - 1.7 * x7 + 0.78 * x8 - 0.3 * x9 <= 0
prob += -x1 - 8.3 * x2 - 4 * x3 - 3 * x4 - 6 * x5 - 2 * x6 + 2 * x7 - 3 * x8 + x9 <= 0
prob += -01.28 * x1 - 2.08 * x2 - 0.4 * x3 - 0.18 * x4 + 1.2 * x5 - 3.2 * x6 + 1.5 * x7 - x8 - 0.3 * x9 <= 0
prob += 0.554 * x1 + 0.011 * x2 - 0.129 * x3 - 0.148 * x4 - 1.276 * x5 - 0.112 * x6 + 0.04 * x7 + 0.022 * x8 - 0.002 * x9 <= 0
prob += 1.383 * x1 - 0.69 * x2 - 0.854 * x3 - 3.927 * x4 - 1.4 * x5 - 1.569 * x6 + 0.1735 * x7 - 1.626 * x8 - 1.785 * x9 <= 0
prob += 0.499 * x1 - 1.507 * x2 + 0.322 * x3 - 1.213 * x4 + 32.85 * x5 - 3.115 * x6 - 26.441 * x7 - 1.871 * x8 + 7.01 * x9 <= 0
prob += x1 <= 111
prob += x2 <= 113
prob += x3 <= 339
prob += x4 <= 94
prob += x5 <= 39
prob += x6 <= 96
prob += x7 <= 112
prob += x8 <= 69
prob += x9 <= 32
prob += 7.16 * x1 + 7.22 * x2 + 7.22 * x3 <= 1545

# The problem is solved using PuLP's choice of Solver
prob.solve()

# status of the solution
print("Status: {}".format(LpStatus[prob.status]))
for v in prob.variables():
    print("{} = {}".format(v.name, str(Fraction(v.varValue).limit_denominator())))
# maximum value of the objective function
print("Max of objective function is {}".format(str(Fraction(value(prob.objective)).limit_denominator())))
