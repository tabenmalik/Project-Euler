"""
Acceptance test of all Euler Problem solutions

All euler solvers must have a correct solution and must generate the solution in under 60sec.
"""
import importlib
import operator
import pkgutil
from importlib.metadata import entry_points

import pe
import pytest
from pe.euler import Problem


def iter_euler_problems():
    """Find and yield all euler problem modules."""
    problem_groups = entry_points(group="pe.problems")
    for problem_group in problem_groups:
        module = problem_group.load()
        for submodule in pkgutil.iter_modules(module.__path__):
            yield submodule.module_finder.find_module(submodule.name).load_module()


@pytest.mark.parametrize("problem", iter_euler_problems())
@pytest.mark.timeout(120)
def test(problem):
    """Test an euler solver. Must generate the correct solution and solve it in less than 60s"""
    if getattr(problem, "SOLUTION", None) is None:
        pytest.xfail("No known solution.")
    assert problem.SOLUTION == problem.solve()
