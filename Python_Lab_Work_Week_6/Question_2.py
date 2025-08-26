# Program to print words longer than 20 characters from words.txt

# Step 1: Open the file
with open("words.txt", "r") as file:
    # Step 2: Read each line
    for line in file:
        # Step 3: Split line into words
        words = line.split()
        # Step 4: Check length of each word
        for word in words:
            if len(word) > 20:
                print(word)
              
