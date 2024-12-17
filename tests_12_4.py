import unittest
import logging

logging.basicConfig(level=logging.INFO,
                    filename='runner_tests.log',
                    filemode='w',
                    encoding='utf-8',
                    format='%(levelname)s: %(message)s')

class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self.name = name
        self.speed = speed

    def __eq__(self, other):
        if isinstance(other, Runner):
            return self.name == other.name
        return False

    def run(self, distance):
        time = distance / self.speed
        return time

    def walk(self, distance):
        time = distance / (self.speed / 2)
        return time

class Tournament:
    def __init__(self, distance, participants):
        self.distance = distance
        self.participants = participants

    def start(self):
        results = {}
        for runner in self.participants:
            time_taken = runner.run(self.distance)
            results[time_taken] = runner.name
        return dict(sorted(results.items()))

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_walk(self):
        try:
            Runner("Test", -5)  
        except ValueError:
            logging.warning("Неверная скорость для Runner")
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            Runner(123, 10) 
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")
        else:
            logging.info('"test_run" выполнен успешно')

if __name__ == '__main__':
    unittest.main()
