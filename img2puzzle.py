import cv2
import numpy as np
import pytesseract
import os


def img2puzzle(img_path):
    gray = cv2.imread(img_path)
    blur = cv2.GaussianBlur(gray, (5,5),0)

    ret,thresh = cv2.threshold(blur,150,255, cv2.THRESH_BINARY)
    
    resize_img = cv2.resize(thresh,(450,450))
    row_split = np.array_split(resize_img, 9, axis = 0)
    img_split = []

    for i in range(9):
        img_split.extend(np.hsplit(row_split[i],9))
    n = 5
    img_split = np.array([img[n:-n, n:-n] for img in img_split])

    board = []
    for m in img_split:
        if np.all(m==255):
            board.append(0)
        else:
            text = pytesseract.image_to_string(m, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=123456789')
            if text.strip().isdigit():
                board.append(int(text))
            else:
                board.append(0)
    return board

def check(board,puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] != board[i][j]:
                print(f"({i}, {j}) {puzzle[i][j]} vs {board[i][j]}")
if __name__ == '__main__':
    img_path = 'puzzle.png'
    predict_board = img2puzzle(img_path)
    for i in range(9):
        print(predict_board[i*9:i*9+9],end=',\n')
