def how_much_i_love_you(petals):
    phrases = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return phrases[(petals - 1) % 6]
import codewars_test as test
from solution import how_much_i_love_you

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(how_much_i_love_you(7), "I love you")
        test.assert_equals(how_much_i_love_you(3), "a lot")
        test.assert_equals(how_much_i_love_you(6), "not at all")
