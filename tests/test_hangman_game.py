import io
import unittest
import responses

from unittest.mock import patch
from hangman_client import start_hangman_game


class HangmanClientTests(unittest.TestCase):

    def test_is_puzzle_solved_with_solved_puzzle(self):
        self.assertTrue(start_hangman_game.is_puzzle_solved(['t', 'a', 'c', 'o'], 'taco'))

    def test_is_puzzle_solved_with_unsolved_puzzle(self):
        self.assertFalse(start_hangman_game.is_puzzle_solved(['t'], 'taco'))

    @patch('builtins.input')
    def test_get_guess_from_user_with_multiple_characters(self, mock_input):
        mock_input.return_value = 'Taco'
        self.assertIsNone(start_hangman_game.get_guess_from_user([]))

    @patch('builtins.input', return_value="t")
    def test_get_guess_from_user_with_valid_input(self, mock_input):
        result = start_hangman_game.get_guess_from_user([])
        self.assertEqual(result, "t")

    @patch('builtins.input', return_value="T")
    def test_get_guess_from_user_is_case_insensitive(self, mock_input):
        result = start_hangman_game.get_guess_from_user([])
        self.assertEqual(result, "t")

    @patch('builtins.input', return_value="t")
    def test_get_guess_from_user_with_duplicated_character(self, mock_input):
        guessed_chars = ['t']
        self.assertIsNone(start_hangman_game.get_guess_from_user(guessed_chars))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_word_progress_full_word(self, mock_stdout):
        expected_result = 'T a c o\n'
        start_hangman_game.display_word_progress(['t', 'a', 'c', 'o'], 'Taco')
        self.assertEqual(mock_stdout.getvalue(), expected_result)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_word_progress_partial_word(self, mock_stdout):
        expected_result = 'T a _ _\n'
        start_hangman_game.display_word_progress(['t', 'a'], 'Taco')
        self.assertEqual(mock_stdout.getvalue(), expected_result)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_display_word_progress_all_blank(self, mock_stdout):
        expected_result = '_ _ _ _\n'
        start_hangman_game.display_word_progress(['b'], 'Taco')
        self.assertEqual(mock_stdout.getvalue(), expected_result)

    @responses.activate
    def test_get_answer_from_hangman_answers_consumes_from_answer_key(self):
        expected_result = 'Taco'
        responses.add(responses.GET, 'http://0.0.0.0:5000/v1/get-hangman-answer',
                      json={'answer': expected_result})
        result = start_hangman_game.get_answer_from_hangman_answers()
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
