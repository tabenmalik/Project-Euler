from collections import defaultdict
from importlib import import_module, resources
from pkgutil import iter_modules

import pe
from pe import euler_problems

class Problem:
    solutions = None

    def __init__(self, n):
        self.n = n
    
    @property
    def solution(self):
        self.load_solutions()
        return self.solutions[self.n]

    def run(self):
        euler_module = import_module(f'.euler_{self.n:03}', package='pe.euler_problems')
        return euler_module.solve()

    @staticmethod
    def all():
        # TODO: find importlib replacement to pkgutil.iter_modules
        for module_info in iter_modules(path=euler_problems.__path__):
            yield Problem(int(module_info.name[-3:]))

    @classmethod
    def load_solutions(cls, force=False):
        if cls.solutions is None or force:
            solution_text = resources.files(pe).joinpath('solutions.txt').read_text()
            cls.solutions = defaultdict(lambda: None)
            for line in solution_text.splitlines():
                num, solution = line.split(':')
                cls.solutions[int(num)] = solution.strip()

    def __repr__(self):
        return f'Problem(n={self.n:03})'

    def __str__(self):
        return self.__repr__()
