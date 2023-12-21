# request a name in camel case
camel = input("camelCase: ")

snake = camel[0].lower()
for output in camel[1:]:
  if output.isupper():
    snake += '_'
  snake += output.lower()

print("snake_case: " + snake)
