class GoalBasedAgent:
  def __init__(self):
    self.goal = 'Complete all subjects'

  def formulate_goal(self, percept):
    if percept:
      self.goal = 'Complete Studying'
    else:
      self.goal = 'Goal Achieved '

  def act(self, percept):
    self.formulate_goal(percept)
    if self.goal == 'Complete Studying':
      return f"Studying {percept[0]}"
    else:
      return "Goal Achieved: All subjects completed"


class Environment:
  def __init__(self):
    self.subjects = ['AI','Math', 'Physics']

  def get_percept(self):
    return self.subjects

  def study_subject(self):
    if self.subjects:
      self.subjects.pop(0)


def run_agent(agent, environment):
  while True:
    percept = environment.get_percept()
    action = agent.act(percept)
    print(action)

    if not percept:
      break

    environment.study_subject()

 
agent = GoalBasedAgent()
environment = Environment()

run_agent(agent, environment)
