# Added .lower() to make the search case insensitive
name = input("What's your name? ").lower()

# If / else version
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# Match Statement
# Added .lower() to make the search case insensitive
match name.lower():
    case "harry" | "hermione" | "ron":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("Who?")

