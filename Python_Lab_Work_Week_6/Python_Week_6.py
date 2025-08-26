def Question1():
    from collections import Counter

    # Step a: Create two new files f1 and f2
    with open("f1.txt", "w") as f1:
        f1.write("Hello this is file one.\nThis file contains some sample text.\nHello again hello.")

    with open("f2.txt", "w") as f2:
        f2.write("Welcome to file two.\nThis is another example file.\nFile two is simple and clear.")

    # Function to read, display, count lines and most common word
    def analyze_file(filename):
        with open(filename, "r") as f:
            content = f.read()
    
        print(f"\nContents of {filename}:")
        print(content)
    
        # Count lines
        with open(filename, "r") as f:
            lines = f.readlines()
        line_count = len(lines)
        print(f"Number of lines in {filename}: {line_count}")
    
        # Find most frequent word
        words = content.lower().split()
        word_counts = Counter(words)
        most_common_word, count = word_counts.most_common(1)[0]
        print(f"Most frequent word in {filename}: '{most_common_word}' (appears {count} times)")
    
        return content

    # Step b: Analyze f1 and f2
    content1 = analyze_file("f1.txt")
    content2 = analyze_file("f2.txt")

    # Step c: Combine f1 and f2 into f3
    with open("f3.txt", "w") as f3:
        f3.write(content1 + "\n" + content2)

    print("\nContents of combined file f3.txt:")
    with open("f3.txt", "r") as f3:
        print(f3.read())

        print("\n--------- Question 2 ---------\n")

def Question2():
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
    
Question1()
Question2()
