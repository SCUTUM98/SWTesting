# 파라미터화 parametrize        
# @pytest.mark.parametrize
# - 하나의 테스트 함수에 여러 다른 데이터 세트를 적용
# - @pytest.mark.parametrize(argnames, argvalues):
#   - argnames: 기대 인자
#   - argvalues: list 형태로 테스트 데이터 전달
# - 여러 테스트 함수를 생성하는 것이 아니라 하나의 함수로 다수의 테스트를 수행할 수 있음

import pytest

def add(a, b):
    return a+b

@pytest.mark.parametrize('a, b, expected', [(1,1,2), (2,3,5), (-1,2,1)])
# a = 1, b = 1, expected = 2
def test_add(a, b, expected):
    assert add(a,b) == expected

test_tuple = [(1,1,2), (2,3,5), (-1,2,1), (4,4,8), (10,-2,8)]

@pytest.mark.parametrize('a, b, expected', test_tuple)
def test_add_tuple(a, b, expected):
    assert add(a,b) == expected