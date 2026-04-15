cpd_P = TabularCPD(
    variable='P', variable_card=2,
    values=[
        [0.95, 0.80, 0.50],
        [0.05, 0.20, 0.50]
    ],
    evidence=['G'],
    evidence_card=[3]
)

model.add_cpds(cpd_I, cpd_S, cpd_D, cpd_G, cpd_P)

print("Model valid:", model.check_model())

inference = VariableElimination(model)

q1 = inference.query(variables=['P'], evidence={'S': 0, 'D': 1})
print("\nP(Pass | Sufficient, Hard):")
print(q1)

q2 = inference.query(variables=['I'], evidence={'P': 0})
print("\nP(Intelligence | Pass=Yes):")
print(q2)
