# Dictionary of Words Mini Project

words = {}

while True:
    print("\n--- Dictionary of Words ---")
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # 1. Add a Word
    if choice == "1":
        word = input("Enter the word: ")
        meaning = input("Enter the meaning: ")

        words[word] = meaning

        print("Word added successfully!")

    # 2. Search for Meaning
    elif choice == "2":
        word = input("Enter the word to search: ")

        if word in words:
            print("Meaning:", words[word])
        else:
            print("Word not found!")

    # 3. Display All Words
    elif choice == "3":
        if words:
            print("\n--- All Words ---")

            for word, meaning in words.items():
                print(word, ":", meaning)
        else:
            print("Dictionary is empty!")

    # 4. Update Meaning
    elif choice == "4":
        word = input("Enter the word to update: ")

        if word in words:
            meaning = input("Enter the new meaning: ")

            words[word] = meaning

            print("Meaning updated successfully!")
            print("Updated Meaning:", words[word])
        else:
            print("Word not found!")

    # 5. Delete Word
    elif choice == "5":
        word = input("Enter the word to delete: ")

        if word in words:
            del words[word]

            print("Word deleted successfully!")
        else:
            print("Word not found!")

    # 6. Exit
    elif choice == "6":
        print("Thank you for using Dictionary of Words!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please enter a number from 1 to 6.")