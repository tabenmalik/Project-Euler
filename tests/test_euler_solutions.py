"""
Acceptance test of all Euler Problem solutions

All euler solvers must have a correct solution and must generate the solution in under 60sec.
"""
import importlib
import operator
import pkgutil
from importlib.metadata import entry_points
from importlib.util import find_spec
from importlib.util import module_from_spec

import pytest


def iter_euler_problems():
    """Find and yield all euler problem modules."""
    problem_packages = entry_points(group="pe.problems")
    for problem_package_info in problem_packages:
        problem_package = problem_package_info.load()
        for problem_module_info in pkgutil.iter_modules(problem_package.__path__):
            spec = find_spec(f".{problem_module_info.name}", problem_package_info.value)
            yield pytest.param(spec, id=problem_module_info.name)


@pytest.mark.parametrize("problem_module_spec", iter_euler_problems())
@pytest.mark.timeout(120)
def test(problem_module_spec):
    """Test an euler solver. Must generate the correct solution and solve it in less than 60s"""
    problem = module_from_spec(problem_module_spec)
    problem_module_spec.loader.exec_module(problem)
    if getattr(problem, "SOLUTION", None) is None:
        pytest.fail("No solution")
    assert problem.SOLUTION == problem.solve()
