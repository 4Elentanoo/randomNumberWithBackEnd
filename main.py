from flask import Flask, session
from flask import render_template, render_template_string, make_response, request, redirect, url_for
import random as rnd
import math
import os


app = Flask(__name__)
app.secret_key = os.urandom(30).hex()

# Константы диапазона
START_RANGE = 1
END_RANGE = 200


def initialize_session():
    session['count'] = math.ceil(math.log2(END_RANGE - START_RANGE + 1))
    session['max_count'] = session['count']
    session['rnd_num'] = rnd.randint(START_RANGE, END_RANGE)
    session['history_numbers'] = []
    session['error'] = ""
    session['message'] = ""
    print(session['rnd_num'])


@app.route("/", methods=["GET", "POST"])
def main():
    if 'rnd_num' not in session:
        initialize_session()

    if request.method == "POST":
        if 'enter__number' in request.form:
            number = request.form['enter__number']
            if number == '':
                session['error'] = "Отсутствует число"
            else:
                if number.isdigit():
                    number = int(number)
                    if END_RANGE < number or START_RANGE > number:
                        session['error'] = "Число вне диапазона"
                    else:
                        session['history_numbers'].append(number)
                        session['count'] -= 1
                        session['error'] = ""

                        if number == session['rnd_num']:
                            session['message'] = "Поздравляем! Вы угадали число!"
                            # Перенаправляем на страницу результата
                            return redirect(url_for('status_game'))
                        elif number < session['rnd_num']:
                            session['message'] = f"Загаданное число больше {number}"
                        else:
                            session['message'] = f"Загаданное число меньше {number}"

                        if session['count'] <= 0:
                            session['message'] = "К сожалению, попытки закончились!"
                            return redirect(url_for('status_game'))
                else:
                    session['error'] = "Число должно быть положительным"

            session.modified = True
            return redirect(url_for('main'))

        if 'new__game' in request.form:
            return redirect(url_for('new_game'))

    # GET запрос - просто отображаем страницу
    return render_template(
        "start_game.html",
        start_range=START_RANGE,
        end_range=END_RANGE,
        count=session['count'],
        history_numbers=session['history_numbers'],
        maxCount=session['max_count'],
        rnd_num=session['rnd_num'],
        error=session['error'],
        message=session.get('message', '')
    )


@app.route("/new_game")
def new_game():
    initialize_session()
    return redirect(url_for('main'))


@app.route("/status_game")
def status_game():
    if 'rnd_num' not in session:
        return redirect(url_for('main'))

    rnd_num = session['rnd_num']
    # Количество использованных попыток
    count = session['max_count'] - session['count']
    message = session.get('message', '')

    session_data = {
        'rnd_num': rnd_num,
        'used_attempts': count,
        'message': message
    }
    session.clear()

    return render_template("status_game.html", **session_data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template_string("""{% extends 'base.html' %} {% block body %}
<main>
  <h1 class="main__title">Вы сбились с пути</h1>
  <div class="table end__game__btn">
  <a href="{{url_for("main")}}">
  <button type="submit" class="btn btn-primary restart__btn">
        Вернуться назад
      </button>
  </a>
    
  </div>
</main>
{% endblock %}
"""), 404


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
