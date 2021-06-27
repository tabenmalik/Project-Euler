"""Acceptance test of all Euler Problem solutions

All euler solvers must have a correct solution and must generate the solution in under 60sec.
"""
import pkgutil
import importlib
import pytest

from project_euler import euler_problems


def euler_modules():
    """Yields all euler problem modules."""
    for module_info in pkgutil.iter_modules(path=euler_problems.__path__):
        yield module_info.name


@pytest.mark.parametrize('module_name', euler_modules())
@pytest.mark.timeout(60)
def test(module_name):
    """Test an euler solver. Must generate the correct solution and solve it in less than 60s"""
    euler_module = importlib.import_module('.' + module_name, package='project_euler.euler_problems')
    exp_solution = euler_module.SOLUTION
    act_solution = euler_module.solve()
    assert exp_solution == act_solution
