class environment_restaurant:
    def __init__(self, name, rating, distance):
        self.name = name
        self.rating = rating
        self.distance = distance


class agent:
    def calculate_utility(self, restaurant):
        return restaurant.rating - restaurant.distance

    def select_restaurant(self, restaurants):
        utilities = {}
        u=0
        selected=''
        for r in restaurants:
            utility = self.calculate_utility(r)
            if utility>u:
                u=utility
                selected=r.name
            utilities[r.name] = utility
            print(f"Restaurant {r.name} Utility = {utility}")

        print(f"Selected Restaurant: {selected}")


restaurant_A = environment_restaurant("A", 7, 3)
restaurant_B = environment_restaurant("B", 9, 5)
utility_agent = agent()
utility_agent.select_restaurant([restaurant_A, restaurant_B])
