from flask import Flask, render_template, request , redirect
import random

app = Flask(__name__)


questions = {
  1: "what is my name",
  2: "What colour were the pills Neo had to choose from in The Matrix?",
  3: "Where did truck driver Jack Burton get into Big Trouble?",
  # 4: "What African country would you be in if you were with Marty, Melman & Gloria?",
  # 5: "What is the name of the actress who plays Abigail in The Favourite?",
  # 6: "Complete the film title starring John Candy: ‘Uncle…’?",
  # 7: "Which capital city appears in the title of the 3rd movie The Fast and Furious franchise?",
  # 8: "Arnold Schwarzenegger plays John Matrix in which 80s action movie?",
  # 9: "Who directed Eyes Wide Shut starring Tom Cruise?",
  # 10: "Who plays the taxi driver who escorts Cruise around in Collateral?",
  # 11: "What was the name of Michael B. Jordan’s character in Black Panther?",
  # 12: "Which actress starred in Bridget Jones’ Diary?",
  # 13: "What is the name of Quint’s shark-hunting boat in Jaws?",
  # 14: "In Mamma Mia! which character marries Sophie’s mother Donna at the end of the story?",
  # 15: "Who plays Jefferson ‘Seaplane’ McDonough in Jumanji: The Next Level?",
  # 16: "What is the name of the skyscraper in Die Hard?",
  # 17: "What fictitious island is Jurassic Park on?",
  # 18: "Who voices Lightning McQueen in Cars?",
  # 19: "Ryan Reynolds starred alongside Melissa George in which 2005 spine chiller?",
  # 20: "Who played the Prime Minister in Love Actually?"
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
  9: ["Stanley Kubrick", "William Heise", "Edwin S. Porter", "D.W. Griffith"],
  10: ["Jamie Foxx", "Kevin Hart", "Eddie Murphy", "Will Smith"],
  11: ["N'Jadaka","T'Challa","M'Baku","Eric Steven" ],
  12: ["Renee Zellweger","Bridget Jones","Scarlett Johannson","Elizabeth Olsen"],
  13: ["The Orca"],
14: ["Sam Carmichael", "Jacob Woods", "Theodore Thompson", "James Filler"],
15: ["Nick Jonas", "Joe Jonas", "Kevin Jonas", "Bill Jonas"],
16: ["Nakatomi Plaza","Burj Khalifa","Merdeka", "Shanghai Tower"],
17: ["Isla Nublar", "Danube Island", "Palm Jumeirah", "Rokko Island"],
18: ["Owen Wilson", "Owen Wilson",	"Kuno Becker",	"Hiroshi Tsuchida"],
19: ["The Amityville Horror", "Sin City", "Pride and Prejudice", "V for Vendetta"],
20: ["Hugh Grant", "David MacAdam", "Oswald Mosley", "Brad Pitt"]
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
  12: "Renee Zellweger",
  13: "The Orca",
  14: "Sam Carmichael",
  15: "Nick Jonas",
  16: "Nakatomi Plaza",
  17: "Isla Nublar",
  18: "Owen Wilson",
  19: "The Amityville Horror",
  20: "Hugh Grant"
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
  options_list = options[numbers]
  random.shuffle(options_list)
  
  return render_template("question.html",questions=questions,numbers=numbers,options_list=options_list)
  
  
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
  answers=["0"]*len(questions)
  return redirect("/")
