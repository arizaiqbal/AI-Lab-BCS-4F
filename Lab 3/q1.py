class Environment:
    def __init__(self, traffic_control='Heavy Traffic'):
        self.traffic_control = traffic_control

    def get_percept(self):
        if self.traffic_control == 'Heavy Traffic':
            return 'Heavy Traffic'
        else:
            return 'Light Traffic'


class SimpleReflexAgent:
  def __init__(self):
    pass
  
  def act(self, percept):
    if percept == 'Heavy Traffic':
      return 'Extend Green Time'
    elif percept == 'Light Traffic':
      return 'Normal Green'
    else:
      return 'Default Green'
      
def run_agent(agent, environment):
    percept = environment.get_percept()
    action = agent.act(percept)
    print(f"Percept: {percept} -> Action: {action}")

agent = SimpleReflexAgent()
environment1 = Environment('Light Traffic')
environment2 = Environment('Heavy Traffic')

run_agent(agent, environment1)
run_agent(agent, environment2)
