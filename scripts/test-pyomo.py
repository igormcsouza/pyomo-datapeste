'''
max l = 1000x + 1800y
20x + 30y <= 1200
x <= 40 
y <= 30
'''

from pyomo.environ import *

model = ConcreteModel()

model.x = Var(within=NonNegativeReals)
model.y = Var(within=NonNegativeReals)

model.const1 = Constraint(rule=lambda model: (20*model.x + 30*model.y <= 1200))
model.const2 = Constraint(rule=lambda model: (model.x <= 40))
model.const3 = Constraint(rule=lambda model: (model.y <= 30))

model.obj = Objective(rule=lambda model: 1000*model.x + 1800*model.y, sense=maximize)

opt = SolverFactory("glpk")
results = opt.solve(model)

print("Resultado:", value(model.x))
print("Resultado:", value(model.y))