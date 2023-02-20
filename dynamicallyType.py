# python is dynamically typed language
# datatype of any variable is checked at runtime

# if we want to specifically show that some value is of specific type
name: str = "James"

# but still you can assign other data type than specified (?)
isAdult: bool = "dd"
print(type(isAdult))

# here with methods:
def hello():
    return "hello"

def altHello() -> int:
    return 1

"""
    btw
        this is a nice way to do multi line comment
    # :)
"""