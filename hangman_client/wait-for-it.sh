#!/bin/sh

set -e

until $(curl --output /dev/null --silent --head --fail http://$HANGMAN_ANSWERS_HOST:5000); do
    printf "hangman-answers is unavailable"
    sleep 5
done
python start_hangman_game.py
