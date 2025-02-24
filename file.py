import os, json, csv

# file_path = "test.txt"

# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandy", 27, "Scientist"]]

# if os.path.exists(file_path):
#     print(f"THe location '{file_path}' exists")

#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("That location doesnt exists")

# txt_data = "I like pizza!"

file_path_ou = "output.txt"
file_path_in = "input.txt"

try:
    with open(file=file_path_in, mode="r") as file:
        # content = file.read()
        # content = json.load(file)
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permisson to read that file")

try:
    with open(file=file_path_ou, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        # json.dump(employee, file, indent=4)
        print(f"csv file '{file_path_ou}' was created")
except FileExistsError:
    print("That file already exists")