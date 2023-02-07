from flask import Flask, render_template, request , redirect

app = Flask(__name__)


questions = {
  1: "what is my name",
  2: "What colour were the pills Neo had to choose from in The Matrix?",
  3: "Where did truck driver Jack Burton get into Big Trouble?",
  # 4:
  # "What African country would you be in if you were with Marty, Melman & Gloria?",
  # 5: "What is the name of the actress who plays Abigail in The Favourite?",
  # 6: "Complete the film title starring John Candy: ‘Uncle…’?",
  # 7:
  # "Which capital city appears in the title of the 3rd movie The Fast and Furious franchise?",
  # 8: "Arnold Schwarzenegger plays John Matrix in which 80s action movie?",
  # 9: "Who directed Eyes Wide Shut starring Tom Cruise?",
  # 10: "Who plays the taxi driver who escorts Cruise around in Collateral?",
  # 11: "What was the name of Michael B. Jordan’s character in Black Panther?",
  # 12: "Which actress starred in Bridget Jones’ Diary?"
}
options = {
  1: ["Samuel", "Mercy", "Ayo", "Blessing"],
  2: ["Red and blue", "green and black", "white and blue", "red and white"],
  3: ["Little China", "Big China", "Little Tokyo", "Big Tokyo"],
  4: ["Madagascar","Seychelles","Algeria","Morocco"],
  5: ["Emma Stone","Megan Fox", "Jennifer Lawrence", "Jennifer Aniston"],
  6: ["Buck", "John", "Chris", "Don"],
  7: ["Tokyo","Beijing","Brusells","London"],
  8: ["Commando","The Matrix", "The God Father", "The Good, the Bad and the Ugly"],
  9: ["Stanley Kubrick",],

  10: ["Jamie Foxx", "Kevin Hart", "Eddie Murphy", "Will Smith"],
  11: ["N'Jadaka","T'Challa","M'Baku","Eric Steven" ],
  12: ["Renee Zellweger","Bridget Jones","Scarlett Johannson","Elizabeth Olsen"]
}
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

score = 0
answers=["0"]*len(questions)

@app.get("/")
def index():
  return render_template("index.html")


@app.route("/questions/<int:numbers>", methods = ["GET","POST"])
def quiz_game(numbers):
  
  if request.method == "POST" :
    user_answer = request.form["options"]
    answers[numbers-2] = user_answer
  
  return render_template("question.html",questions=questions,score = score ,numbers=numbers,options=options)
  
  
@app.post("/questions/results")
def results():
  user_answer = request.form["options"]
  answers[len(questions)-1] = user_answer
  user_score = match(correct_answers,answers,score)
  return render_template("result.html", user_score=user_score, answers= answers)

def match(correct_answer, answers, score):
  i = 1
  for answer in answers:
    if answer == correct_answer[i]:
      score += 1
      i+=1
    else:
      i+=1
  return score

@app.get("/reset")
def reset():
  global answers
  answers =[]
  return redirect("/")
