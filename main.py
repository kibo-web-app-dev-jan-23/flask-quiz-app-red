# from flask import Flask, render_template, request

# app = Flask(__name__)


# questions = {1:"what is my name", }
# options ={1:["Samuel","Mercy","Ayo","Blessing"]}
# correct_answers={1: "Samuel"} 

# @app.get("/")
# def index():
#   return render_template("index.html")
  
# @app.get("/quiz/<numbers>")
# def quiz_game(number):
#   return render_template("quiz.html", questions = questions, number= number, options=options)

# @app.get("/quiz/results")
# def results():
#   return render_template("results.html", score = score)

# def correct_answers(score):
#   if match():
#     score+=1

# def match(user_answer,correct_answer):
#   if user_answer == correct_answer:
#     return True 
#   else:  
#     return False 

