import pytest

from apps.calculator import Calculator

# 픽스쳐(fixture)
@pytest.fixture
def calcurator_instance():
    cal = Calculator()
    return cal
# Decoration Function
# 테스트 함수에 전달 목적

def test_add(calcurator_instance):
        
    assert calcurator_instance.add(3,4) == 7
    assert calcurator_instance.add(-1,1) == 0
    assert calcurator_instance.add(-1, -98) == -99
    
def test_sub(calcurator_instance):
    
    assert calcurator_instance.sub(5,2) == 3
    assert calcurator_instance.sub(10, -2) == 12
    assert calcurator_instance.sub(-2, 3) == -5
    
def test_div(calcurator_instance):
    
    assert calcurator_instance.div(5, 3) == pytest.approx(5/3)
    assert calcurator_instance.div(1, 3) == pytest.approx(1/3)
    with pytest.raises(ZeroDivisionError):
        calcurator_instance.div(3,0)
        # ZeroDivisionError 가 발생하면 테스트 성공
        # 다른 결과가 나오거나 다른 에러 발생시 테스트 실패

def test_multi(calcurator_instance):
    
    assert calcurator_instance.multi(3,2) == 6
    assert calcurator_instance.multi(4, -4) == -16
    assert calcurator_instance.multi(6, 0) == 0