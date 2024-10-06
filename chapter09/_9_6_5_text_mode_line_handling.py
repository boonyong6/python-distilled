with open("filename.txt", "rt", newline="\r\n") as file:
    for i, line in enumerate(file):
        print(f"Line {i + 1}:\n{line}")
