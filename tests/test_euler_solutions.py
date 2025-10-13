"""
Acceptance test of all Euler Problem solutions

All euler solvers must have a correct solution and must generate the solution in under 60sec.
"""

from collections.abc import Generator
from typing import Any
from _frozen_importlib import ModuleSpec
import importlib
import operator
import pkgutil
from importlib.metadata import entry_points
from importlib.util import find_spec
from importlib.util import module_from_spec

import pytest
from _pytest.mark.structures import ParameterSet


def iter_euler_problems() -> Generator[ParameterSet, None, None]:
    """Find and yield all euler problem modules."""
    problem_packages = entry_points(group="pe.problems")
    for problem_package_info in problem_packages:
        problem_package = problem_package_info.load()
        for problem_module_info in pkgutil.iter_modules(problem_package.__path__):
            spec = find_spec(f".{problem_module_info.name}", problem_package_info.value)
            yield pytest.param(spec, id=problem_module_info.name)


@pytest.mark.parametrize("problem_module_spec", iter_euler_problems())
@pytest.mark.timeout(60)
def test(problem_module_spec: ModuleSpec) -> None:
    """Test an euler solver. Must generate the correct solution and solve it in less than 60s"""
    problem = module_from_spec(problem_module_spec)
    assert problem is not None
    assert problem_module_spec.loader is not None
    problem_module_spec.loader.exec_module(problem)
    if getattr(problem, "SOLUTION", None) is None:
        pytest.fail("No solution")
    assert problem.SOLUTION == problem.solve()
