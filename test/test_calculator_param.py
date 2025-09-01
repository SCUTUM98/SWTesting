import pytest

from test.conftest import calculator_instance
from test.test_calculator_csv import load_csv, trans

add_test_cases = [(749.12, 597, 1346.12), (70.97, -325.29, -254.32000000000002), (54.4, -464, -409.6), (-163.63, 626.56, 462.92999999999995),
    (-161.46, -177, -338.46000000000004), (0, 50.12, 50.12), (535.1, 794.7, 1329.8000000000002), (-29.7, 0, -29.7), (274.67, 108.97, 383.64),
    (96.79, -526.49, -429.7), (290.76, -725.66, -434.9), (673.23, -297.74, 375.49), (-231.84, -425.23, -657.07), (402.13, 882.68, 1284.81),
    (-712.18, 119.34, -592.8399999999999), (312.56, -738.9, -426.34), (-875, -840.12, -1715.12), (-976.24, -557, -1533.24), (541, 107.89, 648.89),
    (0, 0, 0), (-490.5, 169.2, -321.3), (72, -951, -879), (-319.8, -961.3, -1281.1), (542.7, 608.1, 1150.8000000000002),
    (-523.4, -220.7, -744.0999999999999), (-840, 770, -70), (-389, -29, -418), (-712, 119, -593), (-935.6, 342.1, -593.5),
    (812, 868, 1680), (-34, -485, -519), (875, 597, 1472), (668, 869, 1537), (78, 62, 140),
    (-871, 114, -757), (569, -270, 299), (240, 153, 393), (-965, -825, -1790), (-657, 14, -643),
    (605, 517, 1122), (-475, -596, -1071), (-488, -263, -751), (-135, -781, -916), (70, -289, -219),
    (37, -979, -942), (-570, -298, -868), (-601, 235, -366), (110, -567, -457), (-386, 755, 369),
    (-889, 584, -305), (-691, -972, -1663), (226, 843, 1069), (791, 574, 1365), (567, -277, 290),
    (-309, 298, -11), (-36, -918, -954), (873, -834, 39), (81, -505, -424), (185, -812, -627),
    (440, 831, 1271), (124, 762, 886), (-60, 482, 422), (-682, -871, -1553), (540, 946, 1486),
    (-837, -817, -1654), (897, -762, 135), (-363, 203, -160), (-29, -962, -991), (-193, 225, 32),
    (-217, 988, 771), (534, -406, 128), (419, -60, 359), (960, 936, 1896), (-715, -675, -1390),
    (-976, -838, -1814), (-996, 786, -210), (561, 483, 1044), (793, 761, 1554), (-826, 83, -743),
    (450, 480, 930), (-564, 403, -161), (673, 560, 1233), (546, -110, 436), (446, 324, 770),
    (675, 939, 1614), (976, 563, 1539), (-801, 410, -391), (168, -253, -85), (240, 786, 1026),
    (-102, -87, -189), (465, -177, 288), (-342, 638, 296), (843, -998, -155), (-260, 203, -57),
    (656, 303, 959), (115, -690, -575), (384, -987, -603), (240, -781, -541), (-214, 219, 5),
    (0.1, 0.2, pytest.approx(0.3)), (pytest.param(1000000000, 2000000000, 3000000000, id='bigValue'))]

# Exception Test
div_test_cases = [(10, 0, ZeroDivisionError), ('10', 2, TypeError), (10, '2', TypeError), (None, 2, TypeError)]

csv_add_cases = load_csv('data/add.csv')

@pytest.mark.parametrize('x, y, expected_value', add_test_cases)
def test_add_cases(calculator_instance, x, y, expected_value):
    assert calculator_instance.add(x, y) == expected_value

@pytest.mark.parametrize('x, y, expected_value', div_test_cases)
def test_div_exceptions(calculator_instance, x, y, expected_value):
    with pytest.raises(expected_value):
        calculator_instance.div(x,y)
        # 정상테스트 파라미터화

@pytest.mark.parametrize('x', [1,2])
@pytest.mark.parametrize('y', [10,100])
def test_multiparam_cases(x, y):
    # val type check
    assert isinstance(x, int)
    assert isinstance(y, int)
    
# ================================================================== test session starts ===================================================================
# platform darwin -- Python 3.11.5, pytest-8.4.1, pluggy-1.6.0 -- /Users/bongeungu/miniforge3/envs/swtest/bin/python3.11
# cachedir: .pytest_cache
# collected 4 items                                                                                                                                        

# test_calculator_param.py::test_multiparam_cases[10-1] PASSED                                                                                       [ 25%]
# test_calculator_param.py::test_multiparam_cases[10-2] PASSED                                                                                       [ 50%]
# test_calculator_param.py::test_multiparam_cases[100-1] PASSED                                                                                      [ 75%]
# test_calculator_param.py::test_multiparam_cases[100-2] PASSED  

@pytest.mark.parametrize('x, y, expected', csv_add_cases)
def test_csv_add(calculator_instance, x, y, expected):
    if expected == 'TypeError':
        with pytest.raises(TypeError):
            calculator_instance.add(trans(x),trans(y))
    else:
        assert calculator_instance.add(trans(x),trans(y)) == trans(expected)