import pytest

from apps.calculator import Calculator
from test.conftest import calculator_instance

def test_add(calculator_instance):
        
    assert calculator_instance.add(3,4) == 7
    assert calculator_instance.add(-1,1) == 0
    assert calculator_instance.add(-1, -98) == -99
    
def test_sub(calculator_instance):
    
    assert calculator_instance.sub(5,2) == 3
    assert calculator_instance.sub(10, -2) == 12
    assert calculator_instance.sub(-2, 3) == -5
    
def test_div(calculator_instance):
    
    assert calculator_instance.div(5, 3) == pytest.approx(5/3)
    assert calculator_instance.div(1, 3) == pytest.approx(1/3)
    with pytest.raises(ZeroDivisionError):
        calculator_instance.div(3,0)
        # ZeroDivisionError 가 발생하면 테스트 성공
        # 다른 결과가 나오거나 다른 에러 발생시 테스트 실패

def test_multi(calculator_instance):
    
    assert calculator_instance.multi(3,2) == 6
    assert calculator_instance.multi(4, -4) == -16
    assert calculator_instance.multi(6, 0) == 0