"""
Acceptance test of all Euler Problem solutions

All euler solvers must have a correct solution and must generate the solution in under 60sec.
"""
import pkgutil
import importlib
import pytest
import operator

import pe
from pe import euler_problems
from pe.euler import Problem

@pytest.mark.parametrize('problem', Problem.all(), ids=operator.attrgetter("n"))
@pytest.mark.timeout(120)
def test(problem):
    """Test an euler solver. Must generate the correct solution and solve it in less than 60s"""
    if problem.solution is None:
        pytest.xfail("No known solution.")
    assert problem.solution == problem.run()
