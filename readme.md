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
1. Run the hangman answers image
```
cd hangman_answers
docker build -t hangman-answers:1.0.0 .
```
`docker run --rm -it -p 5000:5000 hangman-answers:1.0.0`
# Building and running the hangman-client image
1. Build the hangman_client image
1. Run the hangman_client image
```
cd hangman_client
docker build -t hangman-client:1.0.0 .
```
```
docker run --rm -it -p 5000:5000 hangman-client:1.0.0
docker exec -it hangman-game_hangman-client_1 sh 
```

## Running Tests
1. Ensure that hangman_answers and hangman_client is not running
```
docker-compose build
pytest --docker-compose=./docker-compose.yaml
```
