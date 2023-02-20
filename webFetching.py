from urllib import request
import json

url = "http://official-joke-api.appspot.com/random_ten"
r = request.urlopen(url)
print(r.getcode())
data = r.read()
jsonData = json.loads(data)

class Joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

    def __str__(self) -> str:
        return f"? {self.setup}\n! {self.punchline}\n"

jokes = []

for data in jsonData:
    jokes.append(Joke(data["setup"], data["punchline"]))

for joke in jokes:
    print(joke)