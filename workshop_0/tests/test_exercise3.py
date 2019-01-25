import exercise3

def test_getAverage():
    result = exercise3.getAverage([80.4, 65.8, 92.3, 45.2])
    assert result == 70.925

def test_fizzBuzz():
    result = exercise3.fizzBuzz(16)
    assert result == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']

def test_hasDuplicates():
    result = exercise3.hasDuplicates([])
    assert result == False
    result = exercise3.hasDuplicates([3,4,3,2])
    assert result == True
    result = exercise3.hasDuplicates([3,4,6,2])
    assert result == False

def test_reverseText():
    result = exercise3.reverseText("mohamed")
    assert result == "demahom"
    result = exercise3.reverseText("")
    assert result == ""
