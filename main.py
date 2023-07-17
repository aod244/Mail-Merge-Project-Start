names = open("Input/Names/invited_names.txt", "r")
names_list = names.read().split("\n")

for name in names_list:
    invite = open("Input/Letters/starting_letter.txt", "r")
    with open(f"Output/ReadyToSend/invited_{name}.txt", "w") as output:
        for line in invite:
            output.write(line)
    with open(f"Output/ReadyToSend/invited_{name}.txt", "r") as name_replace:
        data = name_replace.read()
        data = data.replace("[name]", f"{name}")

    with open(f"Output/ReadyToSend/invited_{name}.txt", "w") as name_replace:
        name_replace.write(data)
