# Hangman Game

## Overview
Hangman Game Utility with two services `hangman-answers` and `hangman-client`

## Prerequisites
- Pyenv
- Pyenv-virtualenv

## Setup
```
pyenv install 3.8.2
pyenv virtualenv 3.8.2 hangman-game
pyenv activate hangman-game
pip install pytest
pip install pytest-docker-compose
```

## Running Locally 
In the console run the following:
`python hangman_answers/app.py`
In a new console tab role the following:
`python hangman_client/start_hangman_game.py`

# Building and running the hangman-answers image
1. Build the hangman_answers image
```
docker-compose up
docker exec -it hangman-game_hangman-client_1 sh
python start_hangman_game.py 
```

## Running Tests
1. Ensure that hangman_answers and hangman_client is not running
```
docker-compose build
pytest --docker-compose=./docker-compose.yaml
```
