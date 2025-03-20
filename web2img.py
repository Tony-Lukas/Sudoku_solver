from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://sudoku.com/challenges/daily-sudoku")
    try:
        banner_close = driver.find_element(By.ID, "banner-close")
        banner_close.click()
    except:
        print("Banner close")

    game = driver.find_element(By.ID, "game")
    game.click()
    game.screenshot("puzzle.png")
    print("Screen shot saved")
finally:
    driver.quit()
