import requests


def get_answer_from_hangman_answers():
    response = requests.get('http://0.0.0.0:5000/v1/get-hangman-answer')
    response.raise_for_status()
    return response.json()['answer']


def display_word_progress(guessed_letters, answer):
    word_progress = []
    for letter in answer:
        if letter.lower() in guessed_letters or letter == ' ':
            word_progress.append(letter)
        else:
            word_progress.append('_')
    print(' '.join(word_progress))


def get_guess_from_user(guessed_letters):
    guess = input(f"Letters you have guessed {guessed_letters}.\nGuess a new letter: ")
    guess = guess.lower().strip()
    if guess not in guessed_letters and len(guess) == 1 and guess.isalpha():
        return guess


def is_puzzle_solved(guessed_letters, answer):
    for letter in answer.lower().replace(' ', '').strip():
        if letter not in guessed_letters:
            return False
    return True


def display_hangman(incorrect_guesses):
    if incorrect_guesses == 0:
        print("""
___________  
|         |  
|            
|            
|            
|            
|            
""")
    elif incorrect_guesses == 1:
        print("""
___________  
|         |  
|         0  
|            
|            
|            
|            
""")
    elif incorrect_guesses == 2:
        print("""
___________  
|         |  
|         0  
|         |  
|            
|            
|            
""")
    elif incorrect_guesses == 3:
        print("""
___________  
|         |  
|         0  
|        /|  
|            
|            
|            
""")
    elif incorrect_guesses == 4:
        print("""
___________  
|         |  
|         0  
|        /|\ 
|            
|            
|            
""")
    elif incorrect_guesses == 5:
        print("""
___________  
|         |  
|         0  
|        /|\ 
|        /   
|            
|            
""")
    elif incorrect_guesses == 6:
        print("""
___________  
|         |  
|         0  
|        /|\ 
|        / \ 
|            
|            
""")


def create_new_game():
    incorrect_guesses = 0
    max_guesses = 6
    guessed_letters = []
    game_is_over = False
    answer = get_answer_from_hangman_answers()
    while not game_is_over:
        guess = None
        while guess is None:
            guess = get_guess_from_user(guessed_letters)
        guessed_letters.append(guess)
        if guess not in answer.lower():
            incorrect_guesses += 1
        display_hangman(incorrect_guesses)
        display_word_progress(guessed_letters, answer)
        if is_puzzle_solved(guessed_letters, answer):
            print("You win!")
            return True
        if incorrect_guesses >= max_guesses:
            print("You lose!")
            print(f"The answer was '{answer}'")
            print(f"The letters you guessed were: {' '.join(guessed_letters)}")
            return False


def start_hangman_game_loop():
    wins = 0
    losses = 0
    play_again = True
    while play_again:
        game_result = create_new_game()
        if game_result is True:
            wins += 1
        else:
            losses += 1
        print(f"Wins: {wins}\nLosses: {losses}")
        valid_input_received = False
        while not valid_input_received:
            play_again_input = input("Would you like to play again? Y/N ")
            if play_again_input.lower() == "yes" or play_again_input.lower() == "y":
                play_again = True
                valid_input_received = True
            elif play_again_input.lower() == "no" or play_again_input.lower() == "n":
                play_again = False
                valid_input_received = True
            else:
                print("please enter yes/no or y/n")


if __name__ == '__main__':
    start_hangman_game_loop()
