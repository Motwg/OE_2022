import pytest
from optimization_functions import OptimizationFunction


def test_f1(opt_funct):
    f = opt_funct('f1')
    assert isinstance(f, OptimizationFunction)
    assert callable(f.opt_function)
    assert callable(f)
    assert len(f.dimension_constraints) == 2
    assert len(f.x_range) == 2
    assert isinstance(f.accuracy, (int, float))
    assert f.accuracy > 0


def test_f1_call(opt_funct):
    f = opt_funct('f1')
    assert f([5, 4, 3]) == 50
    assert f([1.2, 2.4, 3.4]) == pytest.approx(18.76, 0.1)
    assert f([]) == 0
    with pytest.raises(TypeError):
        f(3)
    with pytest.raises(TypeError):
        f('ok')
    with pytest.raises(TypeError):
        f(None)
        

def test_f2(opt_funct):
    f = opt_funct('f2')
    assert isinstance(f, OptimizationFunction)
    assert callable(f.opt_function)
    assert callable(f)
    assert len(f.dimension_constraints) == 2
    assert len(f.x_range) == 2
    assert isinstance(f.accuracy, (int, float))
    assert f.accuracy > 0


def test_f2_call(opt_funct):
    f = opt_funct('f2')
    assert f([5, 4, 3]) == 35
    assert f([1.2, 2.4, 3.4]) == pytest.approx(5.36, 0.1)
    assert f([]) == 0
    with pytest.raises(TypeError):
        f(3)
    with pytest.raises(TypeError):
        f('ok')
    with pytest.raises(TypeError):
        f(None)
