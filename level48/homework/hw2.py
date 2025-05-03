def other_angle(a, b):
    return 180 - (a + b)
import codewars_test as test

try:
    from solution import other_angle as other_angle
except ImportError:
    from solution import other_angle

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(other_angle(30, 60), 90)
        test.assert_equals(other_angle(60, 60), 60)
        test.assert_equals(other_angle(43, 78), 59)
        test.assert_equals(other_angle(10, 20), 150)
