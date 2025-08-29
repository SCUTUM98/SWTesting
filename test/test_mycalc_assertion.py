import pytest
import warnings

from apps.mycalc import add, sub, div

def test_various_assertion():
    # 참거짓 검증
    assert True
    assert 0 == False
    assert 1 == True
    assert not ""
    
    # 
    
def test_div_float():
    # 순환소수일 경우
    result = div(1,3) 
    assert result == pytest.approx(1/3)
    
    # 일반적인 나누기
    assert div(10,2) == pytest.approx(5.0)
    assert div(20.34, 4.3) == pytest.approx(20.34/4.3)
    
def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        div(3,0)
        # ZeroDivisionError 가 발생하면 테스트 성공
        # 다른 결과가 나오거나 다른 에러 발생시 테스트 실패

def test_type_error():
    with pytest.raises(TypeError):
        div('4',3)
        # TypeError 가 발생하면 테스트 성공
        # 다른 결과가 나오거나 다른 에러 발생시 테스트 실패
    # with pytest.raises(ValueError):
    #     div('4',3)
    #     # ValueError 가 발생하면 테스트 성공

def function_that_warns():
    warnings.warn("이 함수는 곧 제거될 예정입니다.", DeprecationWarning)
    return True
        
def test_warning():
    with pytest.warns(DeprecationWarning):
        assert function_that_warns()