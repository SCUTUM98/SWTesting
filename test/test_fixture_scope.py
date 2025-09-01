import pytest

@pytest.fixture(scope='class')
def sample_data():
    print("\n===Create Data===")
    return {'id':1, 'name':'henry'}

class TestSample:
    def test_id(self, sample_data):
        print(('\n=== ID ==='))
        assert sample_data['id'] == 1
        
    def test_name(self, sample_data):
        print('\n=== Name ===')
        assert sample_data['name'] == 'henry'
        
# pytest test_fixture_scope.py::TestSample -s
# ================================================================== test session starts ===================================================================
# platform darwin -- Python 3.11.5, pytest-8.4.1, pluggy-1.6.0
# collected 2 items                                                                                                                                        

# test_fixture_scope.py 
# ===Create Data===

# === ID ===
# .
# === Name ===
# .

class TestSampleInstance:
    def test_id(self, calculator_instance):
        print(('\n=== ID ==='))
        assert calculator_instance.add['id'] == 1
        
    def test_name(self, calculator_instance):
        print('\n=== Name ===')
        assert calculator_instance.add['name'] == 'henry'
# TestSample Class == TestSampleInstance Class

# 무의미        
class TestGuest:
    def test_id(self, sample_data):
        assert sample_data['id'] == 1