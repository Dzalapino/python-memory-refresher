# some usefull methods

someText = "Pokaz mi jak odbijasz strzaly wiedzminie"

print(someText.upper())

print(someText.replace('wiedzminie', 'morswinie'))
print(someText.replace('a', '44'))

print("length: " + str(len(someText)))

print(someText == "Pokaz mi jak odbijasz strzaly wiedzminie")

print("Pokaz" not in someText)

# multiline

comment = "la da da di da da da da" \
"la da da di da da da da" \
"la da da di da" \
"la da di da da da" \
"la da di da da da da da"

betterComment = """
chcialbym byc...
... marynarzem

chcialbym miec...
...tatuaze
"""

print(comment)
print(betterComment)

# formatting

# first approach
name = "Eustachy Motyka"
email = """
hello {},
how are you?
It is nice talking to you
"""

print(email.format(name))

# second approach
name = "Eustachy Motyka"
email = f"""
hello {name},
how are you?
It is nice talking to you
age: {4 + 4}
"""

print(email)