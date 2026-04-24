class GWAfinder:
    def __init__(self, filename):
        self.filename = filename

    def find_highest_gwa(self):
        highest_name = ''
        highest_gwa = 5.0

        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) < 2: continue

                    name = parts[0]
                    gwa = float(parts[1])

                    if gwa < highest_gwa:
                        highest_gwa = gwa
                        highest_name = name

            if highest_name:
                print(f"Top Student: {highest_name} with a GWA of {highest_gwa}")
            else:
                print("No data found in the file.")

        except FileNotFoundError:
            print("Student record file not found.")
        except ValueError:
            print("Error: May maling data format sa file.")


reviewer = GWAfinder("list_of_students.txt")
reviewer.find_highest_gwa()