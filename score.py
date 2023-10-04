from utils import SCORES_FILE_NAME
from os import path


def add_score(difficulty):
    score_file_result = load_score_file()
    score_file_result += (difficulty * 3) + 5
    score_file = open(SCORES_FILE_NAME, "w")
    score_file.write(f"{score_file_result}")
    score_file.close()


def load_score_file():
    if path.exists(SCORES_FILE_NAME):
        score_file = open(SCORES_FILE_NAME, "r")
        score_file_result = score_file.read()
        if score_file_result.isdigit():
            score_file_result = int(score_file_result)
        score_file.close()
    else:
        score_file_result = 0
    return score_file_result


