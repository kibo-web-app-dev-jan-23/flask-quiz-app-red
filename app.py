from flask import Flask, render_template, request

app = Flask(__name__)

score = 0
questions = {
  1: "what is my name",
  2: "What colour were the pills Neo had to choose from in The Matrix?",
  3: "Where did truck driver Jack Burton get into Big Trouble?",
  4:
  "What African country would you be in if you were with Marty, Melman & Gloria?",
  5: "What is the name of the actress who plays Abigail in The Favourite?",
  6: "Complete the film title starring John Candy: ‘Uncle…’?",
  7:
  "Which capital city appears in the title of the 3rd movie The Fast and Furious franchise?",
  8: "Arnold Schwarzenegger plays John Matrix in which 80s action movie?",
  9: "Who directed Eyes Wide Shut starring Tom Cruise?",
  10: "Who plays the taxi driver who escorts Cruise around in Collateral?",
  11: "What was the name of Michael B. Jordan’s character in Black Panther?",
  12: "Which actress starred in Bridget Jones’ Diary?"
}
options = {1: ["Samuel", "Mercy", "Ayo", "Blessing"]}
correct_answers = {
  1: "Samuel",
  2: "Red and blue",
  3: "Little China",
  4: "Madagascar",
  5: "Emma Stone",
  6: "Buck",
  7: "Tokyo",
  8: "Commando",
  9: "Stanley Kubrick",
  10: "Jamie Foxx",
  11: "Erik Killmonger",
  12: "Renee Zellweger"
}


@app.get("/")
def index():
  return render_template("index.html")


@app.get("/quiz/<numbers>")
def quiz_game(number):
  return render_template("quiz.html",
                         questions=questions,
                         number=number,
                         options=options)


@app.get("/quiz/results")
def results():
  return render_template("results.html", score=score)


def correct_answers(score):
  if match():
    score += 1


def match(user_answer, correct_answer):
  if user_answer == correct_answer:
    return True
  else:
    return False
