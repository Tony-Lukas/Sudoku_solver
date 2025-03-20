from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from img2puzzle import img2puzzle

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://sudoku.com")
    try:
        banner_close = driver.find_element(By.ID, "banner-close")
        banner_close.click()
    except:
        print("Banner close")

    game = driver.find_element(By.ID, "game")
    game.click()
    game.screenshot("puzzle.png")
    print("Screen shot saved")
    board = img2puzzle('puzzle.png')
    for i in range(9):
        for j in range(9):
            print(board[i*9+j], end= ' ')
        print()
finally:
    driver.quit()
