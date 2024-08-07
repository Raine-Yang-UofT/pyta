"""Tests for ExprWrapper in python_ta.transforms."""

import pytest
from astroid import extract_node

from python_ta.transforms import ExprWrapper


def test_expr_wrapper_invalid_node() -> None:
    with pytest.raises(ValueError):
        ExprWrapper("not a node")


def test_expr_wrapper_assignment() -> None:
    assignment = "n = 2 + 3"

    node = extract_node(assignment)
    expr = ExprWrapper(node)

    assert expr.node is node.value
    assert expr.reduce() == 5
