import pytest

from apps.mycalc import add, sub

# 참/거짓 검증: assert, assert not
# 비교 검증
# 멤버십 검증: in, not in
# 동일성 검증: is, is not

def test_add_positive_num():
    # 준비
    a = 3
    b = 4
    expected_reuslt = 7
    
    # 실행
    actual_result = add(3,4)
    
    # 검증
    assert actual_result == expected_reuslt
    #assert add(4,5) == 9
    
    
def test_add_negative_num():
    # 준비
    a = -3
    b = -4
    expected_result = -7
    
    # 실행
    actual_result = add(a,b)
    
    # 검증
    assert actual_result == expected_result

def test_add_zero_num():
    # 준비
    a = 0
    b = 0
    expected_result = 0
    
    # 실행
    actual_result = add(a,b)
    
    # 검증
    assert actual_result == expected_result
    
def test_sub_positive_num():
    # 준비
    a = 3
    b = 2
    expected_result = 1
    
    # 실행
    actual_result = sub(a,b)
    
    # 검증
    assert actual_result == expected_result
    
def test_sub_negative_num():
    # 준비
    a = -3
    b = -4
    expected_result = 1
    
    # 실행
    actual_result = sub(a,b)
    
    # 검증
    assert actual_result == expected_result
    
def test_sub_zero_num():
    # 준비
    a = 0
    b = 0
    expected_result = 0
    
    # 실행
    actual_result = sub(a,b)
    
    # 검증
    assert actual_result == expected_result