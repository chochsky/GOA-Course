def double_integer(n):
    return n * 2
import codewars_test as test

@test.describe('Tests')
def tests():
    @test.it('Sample Test Case')
    def sample_test_case():
        test.assert_equals(double_integer(2), 4)
        test.assert_equals(double_integer(4), 8)
        test.assert_equals(double_integer(-10), -20)
        test.assert_equals(double_integer(0), 0)
        test.assert_equals(double_integer(100), 200)
