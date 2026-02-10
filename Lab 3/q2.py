import random

class Environment:
    def __init__(self, student_presence='No', light_status='OFF'):
        self.student_presence = student_presence
        self.light_status = light_status

    def get_percept(self):
        return {'student_presence': self.student_presence, 'light_status': self.light_status}

    def turn_lights_off(self):
        if self.light_status == 'ON':
            self.light_status = 'OFF'

    def turn_lights_on(self):
        if self.light_status == 'OFF':
            self.light_status = 'ON'


class ModelBasedAgent:
    def __init__(self):
        self.model = {'student_presence': 'No', 'light_status': 'OFF'}

    def act(self, percept):
        self.model.update(percept)

        if self.model['student_presence'] == 'Yes' and self.model['light_status'] == 'OFF':
            return 'Turn lights ON'
        elif self.model['student_presence'] == 'No' and self.model['light_status'] == 'ON':
            return 'Turn lights OFF'
        else:
            return 'No Action'


def run_agent(agent, environment, steps):
    for step in range(steps):
        environment.student_presence = random.choice(['Yes', 'No'])  
        percept = environment.get_percept()
        action = agent.act(percept)

        if action == 'Turn lights ON':
            environment.turn_lights_on()
        elif action == 'Turn lights OFF':
            environment.turn_lights_off()

        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")
        print(f"Internal Model: {agent.model}")


agent = ModelBasedAgent()
environment = Environment(student_presence='No', light_status='OFF')

run_agent(agent, environment, 8)
