#Write code to assign the string "You can apply to SI!" to output if the string "SI 106" is in the list courses. If it is not in courses, assign the value "Take SI 106!" to the variable output.
courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]
if "SI 106" in courses:
    output = "You can apply to SI!"
    print(output)
else:
    output = "Take SI 106"
    print(output)
