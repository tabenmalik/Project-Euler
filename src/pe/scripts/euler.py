#!/usr/bin/env python

import argparse
import importlib
import logging
import sys
import time
import importlib
from importlib.metadata import entry_points

LOGGER = logging.getLogger(__name__)


def configure_logger(verbosity):
    trace_level_num = 5
    logging.addLevelName(trace_level_num, 'TRACE')

    def _trace(self, message, *args, **kwargs):
        if self.isEnabledFor(trace_level_num):
            self._log(trace_level_num, message, args, **kwargs)

    logging.Logger.trace = _trace

    level = logging.WARNING
    if verbosity == 1:
        level = logging.INFO
    elif verbosity == 2:
        level = logging.DEBUG
    elif verbosity == 3:
        level = trace_level_num
    logging.basicConfig(level=level)

def get_latest_solution(euler_module):
    attrs = dir(euler_module)
    solution_funcs = filter(lambda s: 'solution' in s, attrs)
    solution_funcs = list(reversed(sorted(solution_funcs)))
    
    return solution_funcs[0]


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--solution', type=int, default=None)
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('number', type=int)
    
    args = parser.parse_args()
    configure_logger(args.verbose)

    return args.number, args.solution

def iter_euler_problems():
    import pkgutil
    problem_groups = entry_points(group = "pe.problems")
    for problem_group in problem_groups:
        module = problem_group.load()
        for submodule in pkgutil.iter_modules(module.__path__):
            yield submodule

def main():
    number, solution_num = get_args()

    for problem in iter_euler_problems():
        if str(number) in problem.name:
            break
    else:
        print(f"Problem {number} not found")
        return 0
    module = problem.module_finder.find_module(problem.name).load_module()
    
    tstart = time.time()
    solution = module.solve()
    tend = time.time()

    LOGGER.info('Solution took {} seconds'.format(tend - tstart))
    print(str(solution))

if __name__ == '__main__':
    sys.exit(main())
