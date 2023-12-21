# new function called convert()
def convert(smiley):
  new_string = smiley.replace(":)","🙂").replace(":(","🙁")
  return new_string

# getting the user's input
old_string = input()

# calling on convert(), but passing 'old_string' in as the argument.
conversion = convert(old_string)
print(conversion)

# def greet(name="Guest"):
#   print("Hello, " + name + "!")

# greet()
# hey = input("What is your name? ")
# yo = greet(hey)
