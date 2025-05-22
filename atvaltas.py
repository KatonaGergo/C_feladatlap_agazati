selection_input_field = input("Írd ide, hogy milyen mértékegységben szeretnél átváltani: ")
number_input_field = float(input("Írd ide a számot, amit át szeretnél váltani: "))

if selection_input_field == "MB":
    result = number_input_field / 1024
    print(f"{number_input_field} MB = {result} GB")

elif selection_input_field == "GB":
    result = number_input_field * 1024
    print(f"{number_input_field} GB = {result} MB")
