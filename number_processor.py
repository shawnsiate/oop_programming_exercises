class IntegerFileProcessor:
    def __init__(self, source_file="integers.txt", even_file="double.txt", odd_file="triple.txt"):
        self.source_file = source_file
        self.even_file = even_file
        self.odd_file = odd_file

    def process_numbers(self):
        print("--- Initializing Integer File Processor ---")

        try:
            with open(self.source_file, "r") as file:
                raw_content = file.read().split()

            numbers_list = []
            for item in raw_content:
                numbers_list.append(int(item))

            even_squares = []
            odd_cubes = []

            for num in numbers_list:
                if num % 2 == 0:
                    squared_result = num ** 2
                    even_squares.append(squared_result)
                else:
                    cubed_result = num ** 3
                    odd_cubes.append(cubed_result)

            with open(self.even_file, "w") as even_output:
                for square_value in even_squares:
                    even_output.write(str(square_value) + "\n")

            with open(self.odd_file, "w") as odd_output:
                for cube_value in odd_cubes:
                    odd_output.write(str(cube_value) + "\n")

            print("\n[Success] Processing completed efficiently!")
            print(f" -> Found and squared {len(even_squares)} even numbers.")
            print(f" -> Found and cubed {len(odd_cubes)} odd numbers.")
            print(f" -> Results written to '{self.even_file}' and '{self.odd_file}'.")

        except FileNotFoundError:
            print(f"\n[Error] The input file '{self.source_file}' does not exist.")
            print("Please make sure the file is in the same folder as this script.")
        except ValueError:
            print("\n[Error] Failed to convert data. Make sure 'integers.txt' contains only numbers.")
        except IOError:
            print("\n[Error] A critical file system read/write error occurred.")

if __name__ == "__main__":
    processor = IntegerFileProcessor()
    processor.process_numbers()