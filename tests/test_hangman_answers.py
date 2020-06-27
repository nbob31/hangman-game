import pytest
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

pytest_plugins = ["docker_compose"]


# Invoking this fixture: 'function_scoped_container_getter' starts all services
@pytest.fixture(scope="function")
def wait_for_hangman_answers(function_scoped_container_getter):
    """Wait for the api from my_api_service to become responsive"""
    request_session = requests.Session()
    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[500, 502, 503, 504])
    request_session.mount('http://', HTTPAdapter(max_retries=retries))
    service = function_scoped_container_getter.get("hangman-answers").network_info[0]
    api_url = f"http://{service.hostname}:{service.host_port}"
    return request_session, api_url


def test_hangman_answers_returns_answer(wait_for_hangman_answers):
    """The Api is now verified good to go and tests can interact with it"""
    request_session, api_url = wait_for_hangman_answers
    answer_response = request_session.get(f'{api_url}/v1/get-hangman-answer')
    answer_response.raise_for_status()
    answer = answer_response.json()['answer']
    assert isinstance(answer, str)
    assert len(answer) > 1

