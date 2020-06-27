import random
from flask import Flask

app = Flask(__name__)


def get_random_word():
    return random.choice(
       [
           'Awkward',
           'Bagpipes',
           'Banjo',
           'do',
           'you',
           'even',
           'smoke',
           'brisket',
           'beer',
           'intelligence',
           'pronunciation',
           'handkerchief',
       ]
    )


@app.route('/v1/get-hangman-answer', methods=["GET"])
def get_hangman_answer():
    return {'answer': get_random_word()}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
