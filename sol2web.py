from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

from snail import snail

ans = [[1, 4, 7, 6, 8, 5, 9, 2, 3],
[8, 3, 9, 2, 7, 4, 1, 5, 6],
[5, 6, 2, 3, 1, 9, 4, 7, 8],
[4, 7, 1, 9, 2, 8, 3, 6, 5],
[9, 8, 6, 5, 4, 3, 7, 1, 2],
[3, 2, 5, 7, 6, 1, 8, 4, 9],
[2, 1, 3, 4, 9, 6, 5, 8, 7],
[7, 5, 4, 8, 3, 2, 6, 9, 1],
[6, 9, 8, 1, 5, 7, 2, 3, 4]]

board = [[0, 4, 7, 6, 0, 5, 0, 0, 0],
[0, 0, 0, 0, 7, 4, 1, 5, 0],
[5, 0, 2, 0, 0, 0, 0, 7, 0],
[4, 7, 1, 9, 2, 8, 0, 0, 0],
[0, 8, 0, 0, 0, 0, 0, 0, 0],
[0, 2, 0, 0, 0, 0, 8, 0, 9],
[0, 0, 0, 0, 0, 6, 0, 8, 0],
[7, 5, 0, 8, 3, 0, 0, 0, 0],
[0, 0, 8, 1, 0, 7, 2, 0, 0]
]

try:
	driver.get("https://sudoku.com/challenges/daily-sudoku")
	game = driver.find_element(By.ID, "game")
	print("game found")
	for r,c,d in snail():
		#print(r,c,end= ' ')
		if board[r][c] == 0:
			#send ans number
			game.send_keys('{ans[r][c]}')
		if d == 0:
			#move Right
			game.send_keys(Keys.ARROW_RIGHT)
		elif d == 1:
			# move Down
			game.send_keys(Keys.ARROW_DOWN)
		elif d == 2:
			# move left
			game.send_keys(Keys.ARROW_LEFT)
		elif d == 3:
			#move Up
			game.send_keys(Keys.ARROW_UP)
except Exception:
	print(Exception)
finally:
	driver.quit()
