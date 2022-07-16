from random import seed, getrandbits, choice, randrange


class City:
    """Class for the city. This will be called later to define individual cities"""

    def __init__(self, name: str = None, size: [None, tuple[int]] = None, initial_seed: int = None):
        # Initializes random generator
        self.random_start = initial_seed or getrandbits(100)
        seed(self.random_start)

        self.name = name
        self.size = size

        # Randomly generated items
        self.child_pop = None
        self.child_percent = None
        self.pop_density = None
        self.population = None
        self.area = None

    def calc_population(self):
        """
        Generates city population.
        :return: None
        """
        city_types = ['Thorp',
                      'Hamlet',
                      'Village',
                      'Small Town',
                      'Large Town',
                      'Small City',
                      'Large City',
                      'Metropolis'
                      ]

        if not self.size:
            self.size = (choice(city_types))

        city_pop_range = {'Thorp': (1, 20),
                          'Hamlet': (21, 60),
                          'Village': (61, 200),
                          'Small Town': (201, 2000),
                          'Large Town': (2001, 5000),
                          'Small City': (5001, 10000),
                          'Large City': (10001, 25000),
                          'Metropolis': (25000, 50000)
                          }
        city_area_range = {'Thorp': (1, 20),
                           'Hamlet': (1, 40),
                           'Village': (5, 60),
                           'Small Town': (100, 1000),
                           'Large Town': (200, 2000),
                           'Small City': (30, 80),
                           'Large City': (80, 200),
                           'Metropolis': (12000, 20000)
                           }
        self.population = (randrange(city_pop_range[self.size][0], city_pop_range[self.size][1]))
        self.area = (randrange(city_area_range[self.size][0], city_area_range[self.size][1]))

    def calc_density(self):
        self.pop_density = self.population / self.area
        if self.pop_density < 1:
            self.pop_density = 1

    def calc_children(self):
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

        self.calc_population()
        self.calc_density()
        self.calc_children()
