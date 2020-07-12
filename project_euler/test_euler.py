import pkgutil
import importlib
import unittest

from project_euler import euler_problems

class EulerTest(unittest.TestCase):

    def test_euler_problem(self):
        for module_info in pkgutil.iter_modules(path=euler_problems.__path__):
            with self.subTest(problem=str(module_info.name)):
                module = importlib.import_module('.' + module_info.name, package=euler_problems.__name__)
                
                exp_solution = module.SOLUTION
                act_solution = module.solve()
                self.assertEqual(exp_solution, act_solution)
