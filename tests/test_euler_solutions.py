import pkgutil
import importlib
import pytest

from project_euler import euler_problems

def euler_modules():
    for module_info in pkgutil.iter_modules(path=euler_problems.__path__):
        yield module_info.name


@pytest.mark.parametrize('module_name', euler_modules())
@pytest.mark.timeout(60)
def test(module_name):
    euler_module = importlib.import_module('.' + module_name, package='project_euler.euler_problems')
    exp_solution = euler_module.SOLUTION
    act_solution = euler_module.solve()
    assert exp_solution == act_solution
