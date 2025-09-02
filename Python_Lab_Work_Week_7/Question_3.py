class Palindrome:
    # Method to reverse a string
    def reverse(self, text):
        return text[::-1]   # slice method to reverse

    # Method to check if a string is a palindrome
    def isPalindrome(self, text):
        # Compare original with reversed (case-insensitive, ignoring spaces)
        cleaned = text.replace(" ", "").lower()
        return cleaned == self.reverse(cleaned)


# -------- Testing the Palindrome class --------
if __name__ == "__main__":
    p = Palindrome()

    # Test strings
    test_strings = ["madam", "racecar", "hello", "Level", "Was it a car or a cat I saw"]

    for word in test_strings:
        print(f"Word: {word}")
        print("Reversed:", p.reverse(word))
        print("Is Palindrome?", p.isPalindrome(word))
        print("-" * 40)
