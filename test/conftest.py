# Decoration Function 집합

import pytest

from apps.calculator import Calculator

# 픽스쳐(fixture)
@pytest.fixture
def calculator_instance(scope='module'):
    print('\n===Create Calculator Instance===')
    cal = Calculator()
    return cal
# Decoration Function
# 테스트 함수에 전달 목적