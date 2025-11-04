from flask import Flask
from flask import render_template, session, make_response, request
import random as rnd
import math

app = Flask(__name__)
# Сделать хранение данных в сессии

start_range = 1
end_range = 120
count = math.ceil(math.log2(end_range - start_range + 1))
maxCount = count
rnd_num = rnd.randint(start_range, end_range)
history_numbers = []


@app.route("/")
def main():
    global count, start_range, end_range, rnd_num, history_numbers, maxCount
    return render_template("start_game.html", start_range=start_range, end_range=end_range, count=count, history_numbers=history_numbers, rnd_num=rnd_num, maxCount=maxCount, error="")


@app.route("/check", methods=['POST'])
def check():
    # брать переменную из сессии
    global count, rnd_num, history_numbers
    count -= 1
    number = request.form['enter__number']
    if count == 0:
        history_numbers = []
        return end_game()
    try:
        if number != "":
            history_numbers.append(int(number))
            if int(number) == rnd_num:
                history_numbers = []
                return win_game()
        elif request.form['new_game'] == "" and number == "":
            return new_game()
    except:
        return main()
    return main()


@app.route("/end_game", methods=['GET'])
def end_game():
    global rnd_num
    return render_template("end_game.html", rnd_num=rnd_num)


@app.route("/new_game", methods=['GET'])
def new_game():
    global count, start_range, end_range, rnd_num, history_numbers
    count = math.ceil(math.log2(end_range - start_range + 1))
    rnd_num = rnd.randint(start_range, end_range)
    history_numbers = []
    print(rnd_num)
    return main()


@app.route("/win_game",)
def win_game():
    global rnd_num
    return render_template("win_game.html", rnd_num=rnd_num)


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
