file_path = "notes.txt"

def show_notes():
    try:
        with open(file_path, "r") as file:
            notes = file.read()

            print("------Your Notes--------")

            print(notes)

    except FileNotFoundError:
        print("Nothing shows up in your notes.........")

def add_notes():
    note = input("Write your note: ")

    with open(file_path, "a") as file:
        file.write(note + "\n")

        print("Note saved successfully......")

        

def main():
    while True:
        print("\n ============= NOTES APP =============")
        print("1. Add note")
        print("2. Show notes")
        print("3. Exit")

        choice = input("Enter a choice: ")

        if choice == "1":
            add_notes()

        elif choice == "2":
            show_notes()

        elif choice == "3":
            print("Goodbye......")
            break

        else:
            print("Invalid choice....")
            continue



if __name__ == "__main__":
    main()