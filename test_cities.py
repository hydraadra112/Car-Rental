import unittest
from city_functions import func

class TestCase(unittest.TestCase):
    def test_city_country(self):
        city_country = func('Santiago', 'Chile')
        self.assertEqual(city_country, 'Santiago, Chile')
        
    def test_city_country_population(self):
        population = 284358
        city_country = func('Santiago', 'Chile', population)
        self.assertEqual(city_country, f'Santiago, Chile - Population: {population}')
        
unittest.main()