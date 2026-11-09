from Decrypt import Rotating_CC

def tests():
    rcc = Rotating_CC()

    # Test 1 - empty string
    assert rcc.RCC_encrypt("", 2) == "", "Test 1 - empty string - failed"

    # Test 2 - single letter
    assert rcc.RCC_encrypt("A", 1) == "B", "Test 2 - single letter - failed"

    # Test 3 - multiple letters
    assert rcc.RCC_encrypt("AA", 1) == "BC", "Test 3 - multiple letters - failed"

    # Test 4 - non-alphabetic character
    assert rcc.RCC_encrypt("A A", 1) == "B C", "Test 4 - non-alphabetic characters - failed"

    # Test 5 - Case sensitive
    assert rcc.RCC_encrypt("Aa", 1) == "Bc", "Test 5 - case sensitive letters - failed"

    # Test 6 - Alphabet wrapping 
    assert rcc.RCC_encrypt("Z", 1) == "A", "Test 6 - alphabet wrapping - failed"

    # Decryption
    # Test 7: Case Retention ("Hello" = "Jirty")
    encrypted_CS = rcc.RCC_encrypt("Hello", 2)
    assert rcc.RCC_decrypt(encrypted_CS) == "Hello", "Test 7 - Decryption (Case Retention) - failed"

    # Test 8: Upper Case Retention ("HELLO" = "JIRTY")
    encrypted_upper = rcc.RCC_encrypt("HELLO", 2)
    assert rcc.RCC_decrypt(encrypted_upper) == "HELLO", "Test 8 - Decryption (Upper Case) - failed"

    # Test 9: Mixed Case Sentence Retention ("Hello World" = "Jirty Ygtnf")
    encrypted_sentence1 = rcc.RCC_encrypt("Hello World", 2)
    assert rcc.RCC_decrypt(encrypted_sentence1) == "Hello World", "Test 9 - Decryption (Mixed sentence casing) - failed"

    # Test 10: Commas and Inner Punctuation
    encrypted_sentence2 = rcc.RCC_encrypt("Hello, World!", 2)
    assert rcc.RCC_decrypt(encrypted_sentence2) == "Hello, World!", "Test 10 - Decryption (Commas and Inner Punctuation) - failed"

    # Test 11: Numbers
    encrypted_sentence3 = rcc.RCC_encrypt("Top 3 Artists", 2)
    assert rcc.RCC_decrypt(encrypted_sentence3) == "Top 3 Artists", "Test 11 - Decryption (Numbers) - failed"
    
    print("All tests passed!")

if __name__ == "__main__":
    tests()