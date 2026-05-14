with open("Input/Letters/starting_letter.txt", mode="r") as file:
    contents = file.read()



total = open("Input/Names/invited_names.txt")
total = (total.readlines())


for item in total:
    clean_name = item.strip()
    new_letter = contents.replace("[name]", clean_name)
    with open(f"Output/ReadyToSend/{clean_name}.txt", mode="w") as file:
        file.write(new_letter)
