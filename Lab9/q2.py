!pip install pgmpy
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Step 1: Define structure
model = DiscreteBayesianNetwork([
    ('I', 'G'),
    ('S', 'G'),
    ('D', 'G'),
    ('G', 'P')
])

# Step 2: Define CPDs

cpd_I = TabularCPD('I', 2, [[0.7], [0.3]])
cpd_S = TabularCPD('S', 2, [[0.6], [0.4]])
cpd_D = TabularCPD('D', 2, [[0.6], [0.4]])

cpd_G = TabularCPD(
    variable='G', variable_card=3,
    values=[
        [0.7, 0.5, 0.4, 0.2, 0.3, 0.2, 0.1, 0.05],
        [0.2, 0.3, 0.4, 0.5, 0.4, 0.3, 0.3, 0.25],
        [0.1, 0.2, 0.2, 0.3, 0.3, 0.5, 0.6, 0.7]
    ],
    evidence=['I', 'S', 'D'],
    evidence_card=[2, 2, 2]
)

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
