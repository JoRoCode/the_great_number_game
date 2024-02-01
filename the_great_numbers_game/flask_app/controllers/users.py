from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user 


import random


@app.route('/')
def index():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1,100)
    print(session['random_num'])
    return render_template('index.html')


@app.post('/play')
def play_game():
    if 'guess_count'not in session:
        session['guess_count'] = 0
    session['guess_count'] += 1
    session['guess'] = int(request.form['guess'])
    print(session)
    return redirect('/')

@app.route('/play_again')
def play_again():
    session.clear()
    return redirect('/')


# @app.route('/play', methods=['GET', 'POST'])
# def play_game():
#     if request.method == 'POST':
#         session['guess'] = int(request.form['guess'])
#         random_num = int(request.form['random_num'])
#         if guess == random_num:
#             results = "Congratulations!! Your guess was correct!!!"
#         elif guess < random_num:
#             results = "I'm sorry, your guess is too low. Try again."
#         elif guess > random_num:
#             results = "I'm sorry, your guess is too high. Try again."
#         else:
#             results = None
#         session['results']=results
#         print(session['random_num'])
#         print(guess)
#         return redirect('/')
#     render_template('index')







# def get_results(guess, random_num):

#     if guess == random_num:
#         result = "Congratulations!! Your guess was correct!!!"
#     elif guess < random_num:
#         result = "I'm sorry, your guess is too low. Try again."
#     elif guess > random_num:
#         result = "I'm sorry, your guess is too high. Try again."
#     else:
#         result = "none"


# @app.route('/play', methods=['GET', 'POST'])
# def play_game():
#     if request.method == 'POST':
#         session['guess'] = int(request.form['guess'])
#         results=get_results(session['guess'], session['random_num'])
#         session['results']=results
#         print(session['random_num'])
#         print(results)
#     return redirect ('/')

# # def paly_game():
# #     results = " "
# #     if request.method == 'POST':
# #         random_num=random.randint(1,100)
# #         guess = int(request.form['guess'])
# #         results= get_results(guess, random_num)
# #         print(random_num)
# #         print(results)
# #         return redirect ('/'), random_num, results
    
    
# # def get_random_num():
# #     random_num=int(random.randint(1,100))
# #     print(random_num, "lets go!!")
# #     return random_num


    

    