class LifeTextWriter:
    def __init__(self, filename="mylife.txt"):
        self.filename = filename

    def write_user_lines(self):
        print("--- Welcome to the Life Text Writer ---")

        try:
            with open(self.filename, "w") as file:
                keep_going = True

                while keep_going:
                    user_line = input("Enter line: ")
                    file.write(user_line + "\n")
                    choice = input("Are there more lines y/n? ").strip().lower()
                    if choice == 'n':
                        keep_going = False
                    elif choice != 'y':
                        print("Invalid input detected, but assuming you want to stop.")
                        keep_going = False

            print(f"\n[Success] All lines have been saved perfectly to '{self.filename}'!")

        except IOError:
            print("[Error] Could not write to the file. Please check system permissions.")

if __name__ == "__main__":
    writer = LifeTextWriter()
    writer.write_user_lines()
