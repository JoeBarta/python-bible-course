from random import choice

questions = ["Why is the Earth Round?", "Where are all the dinosaurs?","Why is the sky blue?:"]

question = (choice(questions))
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?:").strip().lower()

print("oh.. okay")
