import exercise2

def test_getFullName():
    name = exercise2.getFullName("mohamed", "ibrahim")
    assert name == "mohamed ibrahim"

def test_canVote():
    result = exercise2.canVote(18)
    assert result == "you can vote !" 
    result = exercise2.canVote(17)
    assert result == "you can't vote !"

def test_isEven():
    result = exercise2.isEven(10)
    assert result == True
    result = exercise2.isEven(9)
    assert result == False
    result = exercise2.isEven(0)
    assert result == True

def test_cheapChatbot():
    result = exercise2.cheapChatbot("good morning")
    assert result == "would you like some coffee?"
    result = exercise2.cheapChatbot("good afternoon")
    assert result == "good afternoon to you too"
    result = exercise2.cheapChatbot("whatever")
    assert result == "I don't know what you're saying"




    