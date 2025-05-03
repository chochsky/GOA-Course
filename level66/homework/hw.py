def move_zeros(arr):
    # Filter out all non-zero elements
    non_zeros = [x for x in arr if x != 0]
    # Count the number of zeros
    zeros = arr.count(0)
    # Return the list of non-zeros followed by the zeros
    return non_zeros + [0] * zeros
import codewars_test as test
from solution import move_zeros

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        test.assert_equals(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]), [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        test.assert_equals(move_zeros([0, 0]), [0, 0])
        test.assert_equals(move_zeros([0]), [0])
        test.assert_equals(move_zeros([]), [])