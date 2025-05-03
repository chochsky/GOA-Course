def who_is_paying(name):
    if len(name) > 2:
        return [name, name[:2]]
    return [name]
from solution import who_is_paying
import codewars_test as test

@test.describe("Basic tests")
def basic_tests():
    
    @test.it("Examples")
    def examples():
        test.assert_equals(who_is_paying("Mexico"), ["Mexico", "Me"])
        test.assert_equals(who_is_paying("Melania"), ["Melania", "Me"])
        test.assert_equals(who_is_paying("Melissa"), ["Melissa", "Me"])
        test.assert_equals(who_is_paying("Me"), ["Me"])
        test.assert_equals(who_is_paying(""), [""])
        test.assert_equals(who_is_paying("I"), ["I"])
