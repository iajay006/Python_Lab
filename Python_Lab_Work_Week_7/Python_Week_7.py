def Question1():
    # Bookshop details stored in a dictionary
    # Key = Title of the book
    # Value = Number of copies

    bookshop = {
        "Python Programming": 10,
        "Data Structures": 5,
        "AI Fundamentals": 7
    }

    # Function to add books
    def add_books(title, copies):
        if title in bookshop:
            bookshop[title] += copies   # increase copies
        else:
            bookshop[title] = copies    # add new book
        print(f"Added {copies} copies of '{title}'. Now total: {bookshop[title]}")

    # Function to sell books
    def sell_books(title, copies):
        if title in bookshop:
            if bookshop[title] >= copies:
                bookshop[title] -= copies   # decrease copies
                print(f"Sold {copies} copies of '{title}'. Remaining: {bookshop[title]}")
            else:
                print(f"Only {bookshop[title]} copies available of '{title}'.")
        else:
            print(f"Book '{title}' not found in the shop.")

    # Function to show all books
    def display_books():
        print("\nBookshop Inventory:")
        for title, copies in bookshop.items():
            print(f"{title} : {copies} copies")

    # Example run
    display_books()
    add_books("Python Programming", 5)
    sell_books("Data Structures", 2)
    sell_books("AI Fundamentals", 10)
    add_books("Machine Learning", 8)
    display_books()
    print()


def Question2():
    class Time:
        def __init__(self, hours=0, minutes=0, seconds=0):
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds

        # Add two Time objects
        def add_time(self, other):
            total_seconds = self.to_seconds() + other.to_seconds()
            return Time.from_seconds(total_seconds)

        # Convert Time object to total seconds
        def to_seconds(self):
            return self.hours * 3600 + self.minutes * 60 + self.seconds

        # Convert seconds back into Time object
        @classmethod
        def from_seconds(cls, total_seconds):
            total_seconds = total_seconds % (24 * 3600)  # wrap around 24 hours
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            return cls(hours, minutes, seconds)

        # Print time in readable format
        def print_time(self):
            print(f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")


    # Example usage
    # Current time
    current_time = Time(14, 30, 0)   # 2:30:00 PM

    # Bread maker takes 3 hours 45 minutes
    bread_time = Time(3, 45, 0)

    # When will bread be ready?
    done_time = current_time.add_time(bread_time)

    print("Current Time: ", end="")
    current_time.print_time()

    print("Bread Time:   ", end="")
    bread_time.print_time()

    print("Done Time:    ", end="")
    done_time.print_time()
    print()



def Question3():
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

print("--------------- Question1 ---------------")
Question1()
print("--------------- Question2 ---------------")
print()
Question2()
print("--------------- Question3 ---------------")
print()
Question3()

