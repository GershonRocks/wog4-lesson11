from selenium.webdriver.common.by import By
from detect_arch import detect_arch_webdriver

TEST_URL = 'http://127.0.0.1:30000/score_server'


def test_scores_service(url):
    driver = detect_arch_webdriver()
    driver.get(url)
    score = driver.find_element(By.ID, 'score').text
    if score.isdigit() and 0 <= int(score) <= 1000:
        print("Test Successful")
        return True
    else:
        print("Test failed")
        return False


def main_function():
    result = test_scores_service(TEST_URL)
    if result:
        exit(0)
    else:
        exit(-1)


if __name__ == '__main__':
    main_function()
    input("Press Enter to exit")

