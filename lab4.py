from pyomo.environ import *

# Create a concrete model
model = ConcreteModel()

# Decision Variables
model.x = Var(within=NonNegativeReals, bounds=(0, 60), doc='Quantity of Keyboards to manufacture')
model.y = Var(within=NonNegativeReals, bounds=(0, 40), doc='Quantity of Mice to manufacture')

# Objective Function
model.profit = Objective(
    expr=80 * model.x + 160 * model.y,
    sense=maximize,
    doc='Total Profit'
)

# Constraints
model.time_constraint = Constraint(
    expr=4 * model.x + 6 * model.y <= 210,
    doc='Manufacturing time constraint'
)

# Create the solver
solver = SolverFactory('glpk')

# Solve the model
solver.solve(model)

# Display the results
print(f"Optimal Quantity of Keyboards to Manufacture: {model.x()} units")
print(f"Optimal Quantity of Mice to Manufacture: {model.y()} units")
print(f"Total Profit: Rs. {model.profit()}")