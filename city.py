from random import seed, getrandbits, choice, randrange


city_types = ['Thorpe',
              'Hamlet',
              'Village',
              'Small Town',
              'Large Town',
              'Small City',
              'Large City',
              'Metropolis'
              ]


class City:
    """Class for the city. This will be called later to define individual cities"""

    def __init__(self,
                 name: str = None,
                 size=None,
                 initial_seed: int = None,
                 race_populations: dict[str, float] = None
                 ):
        # Initializes random generator
        self.race_populations = race_populations
        self.random_start = initial_seed or getrandbits(100)
        seed(self.random_start)

        self.name = name
        self.size = size

        # Randomly generated items
        self.child_pop = None
        self.child_percent = None
        self.pop_density = None
        self.population = None
        self.total_population = None
        self.area = None

    def get_total_population(self):
        """
        Generates city population.
        :return: None
        """

        if not self.size:
            self.size = (choice(city_types))

        # TODO optimize
        city_pop_range = {'Thorpe': (1, 20),
                          'Hamlet': (21, 60),
                          'Village': (61, 200),
                          'Small Town': (201, 2000),
                          'Large Town': (2001, 5000),
                          'Small City': (5001, 10000),
                          'Large City': (10001, 25000),
                          'Metropolis': (25000, 50000)
                          }

        population = (randrange(city_pop_range[self.size][0], city_pop_range[self.size][1]))
        return population

    def get_race_population(self, population):
        """Get total race population. This will be expanded to additional functionality."""
        total_race_population = {race: int(population*(population_percent/100))
                                 for race, population_percent in self.race_populations.items()}
        return total_race_population

    def density(self, population):
        city_area_range = {"Thorpe": (1, 20),
                           "Hamlet": (2, 40),
                           "Village": (5, 60),
                           "Small Town": (100, 1000),
                           "Large Town": (200, 2000),
                           "Small City": (30, 80),
                           "Large City": (80, 200),
                           "Metropolis": (12000, 20000)
                           }
        self.area = (randrange(city_area_range[self.size][0], city_area_range[self.size][1]))
        pop_density = population / self.area
        if pop_density < 1:
            pop_density = 1
        return pop_density

    def get_child_population(self):
        """
        Calculates percentage of city population that are children
        """

        self.child_percent = (round((randrange(0, 50) / 100.0), 2))
        self.child_pop = self.population * self.child_percent

    def generate(self):
        """
        Runs all the city generation items.
        :return:
        """

        self.total_population = self.get_total_population()
        self.pop_density = self.density(self.total_population)
        self.population = self.get_race_population(self.total_population)

