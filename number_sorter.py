import os


class NumberSorter:
    def __init__(self, input_file):
        self.input_file = input_file

    def process_numbers(self):
        if not os.path.exists(self.input_file):
            print(f"Error: {self.input_file} not found!")
            return

        try:
            with open(self.input_file, 'r') as file:
                with open('even.txt', 'w') as even_file, open('odd.txt', 'w') as odd_file:
                    for line in file:
                        if line.strip():
                            num = int(line.strip())
                            if num % 2 == 0:
                                even_file.write(f"{num}\n")
                            else:
                                odd_file.write(f"{num}\n")

            print("Sorting complete!")

        except ValueError:
            print("Error: May alien(not a number) sa text file!")

sorter = NumberSorter("ten_integer_numbers.txt")
sorter.process_numbers()