import random

class LearningAgent:
    def __init__(self):
        self.q_table = {"Play": 0, "Rest": 0}

    def choose_action(self):
        if self.q_table["Play"] >= self.q_table["Rest"]:
            return "Play"
        else:
            return "Rest"

    def update_q(self, action, reward):
        self.q_table[action] = self.q_table[action] + reward


class Environment:
    def get_reward(self, action):
        if action == "Play":
            return 5
        else:
            return 1


def run_agent(agent, environment, steps):
    for step in range(steps):
        action = agent.choose_action()
        reward = environment.get_reward(action)
        agent.update_q(action, reward)

        print(f"Step {step + 1}: Action {action} Reward {reward}")

    print("Q-table Updated")
    print(agent.q_table)


agent = LearningAgent()
environment = Environment()

run_agent(agent, environment, 10)
