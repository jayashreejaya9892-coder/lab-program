from palindrome import check

def test_palindrome():
    assert check("madam") == True

def test_not_palindrome():
    assert check("hello") == False