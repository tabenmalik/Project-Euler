"""
Acceptance test of all Euler Problem solutions

All euler solvers must have a correct solution
and must generate the solution in under 60sec.
"""
from __future__ import annotations

import pkgutil
from _frozen_importlib import ModuleSpec
from collections.abc import Generator
from importlib.metadata import entry_points
from importlib.util import find_spec
from importlib.util import module_from_spec

import pytest
from _pytest.mark.structures import ParameterSet


def iter_euler_problems() -> Generator[ParameterSet]:
    """Find and yield all euler problem modules."""
    pkg_infos = entry_points(group="pe.problems")
    for pkg_info in pkg_infos:
        pkg = pkg_info.load()
        for module_info in pkgutil.iter_modules(pkg.__path__):
            spec = find_spec(
                f".{module_info.name}",
                pkg_info.value,
            )
            yield pytest.param(spec, id=module_info.name)


@pytest.mark.parametrize("problem_module_spec", iter_euler_problems())
@pytest.mark.timeout(60)
def test(problem_module_spec: ModuleSpec) -> None:
    """
    Test an euler solver.

    Must generate the correct solution and solve it in less than 60s
    """
    problem = module_from_spec(problem_module_spec)
    assert problem is not None
    assert problem_module_spec.loader is not None
    problem_module_spec.loader.exec_module(problem)
    if getattr(problem, "SOLUTION", None) is None:
        pytest.fail("No solution")
    assert problem.SOLUTION == problem.solve()
