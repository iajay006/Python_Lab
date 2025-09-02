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
    print()

# Example run
display_books()
add_books("Python Programming", 5)
sell_books("Data Structures", 2)
sell_books("AI Fundamentals", 10)
add_books("Machine Learning", 8)
display_books()
