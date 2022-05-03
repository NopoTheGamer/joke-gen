import random

from guizero import *
joke1 = ["What do you call a fake noodle?", "what is deez", "why did the crab go to jail", "why did the chicken cross the road", "why did the zak go to the dentist", "what do you call a deer with no eye",
         "a man walks into a bar and says ouch", "no", ""]
joke2 = ["An Impasta!", "deez nuts", "crimes", "darcy keeys", "Your mother was a hamster and your father smelt of elderberries", "!", "blind", "bottom text",
         "vodka", "because it didnt", "after that it went to jail"]

app = App(title="Joke Generator")

def joke_generator():
    x = random.randint(0, len(joke1) - 1)
    y = random.randint(0, len(joke2) - 1)
    Text(app, text=joke1[x])
    Text(app, text=joke2[y])
    Text(app, text="")

title = Text(app, text="Welcome to the joke generator!")
button = PushButton(app, command=joke_generator, text="Generate a joke!")
app.display()
