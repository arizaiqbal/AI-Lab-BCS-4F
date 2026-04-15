from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills')
])

cpd_D = TabularCPD(variable='Disease', variable_card=2,
                   values=[[0.3], [0.7]])

# Fever
cpd_Fever = TabularCPD(
    variable='Fever', variable_card=2,
    values=[[0.9, 0.5], [0.1, 0.5]],
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_Cough = TabularCPD(
    variable='Cough', variable_card=2,
    values=[[0.8, 0.6], [0.2, 0.4]],
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_Fatigue = TabularCPD(
    variable='Fatigue', variable_card=2,
    values=[[0.7, 0.3], [0.3, 0.7]],
    evidence=['Disease'],
    evidence_card=[2]
)

cpd_Chills = TabularCPD(
    variable='Chills', variable_card=2,
    values=[[0.6, 0.4], [0.4, 0.6]],
    evidence=['Disease'],
    evidence_card=[2]
)

model.add_cpds(cpd_D, cpd_Fever, cpd_Cough, cpd_Fatigue, cpd_Chills)

print("Model valid:", model.check_model())

inference = VariableElimination(model)

q1 = inference.query(variables=['Disease'],
                     evidence={'Fever': 0, 'Cough': 0})
print("\nP(Disease | Fever, Cough):")
print(q1)

q2 = inference.query(variables=['Disease'],
                     evidence={'Fever': 0, 'Cough': 0, 'Chills': 0})
print("\nP(Disease | Fever, Cough, Chills):")
print(q2)

q3 = inference.query(variables=['Fatigue'],
                     evidence={'Disease': 0})
print("\nP(Fatigue | Flu):")

     
