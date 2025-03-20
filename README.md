# Tasks
- [x] Get Sudoku puzzle from https://sudoku.com/
- [x] Change 2D array
- [x] Solve the puzzle
- [x] Put solution back to https://sudoku.com/
- [ ] Run Task Daily (https://sudoku.com/challenges/daily-sudoku)
# Key Take away
1. Interactive with web using (`selenium`)
2. Image processing with (`cv2`)
3. OCR with (`pytestrest`)
4. Solve Sudoku puzzle with `recursive` function

# Challenges
1. Firstly I think Sudoku puzzle are store in table and I can easily get using `request` and `beautifulsoup`. But It store in canvas and I only get image of it.
2. Split the image  cell is quite easy task using `numpy.hsplit` and `numpy.vsplit` 
3. Change each cell to number array is challenging. I test various methods.
	1. Using image image similarity
	2. Using MNIST dataset and train a CNN model
	3. Using `pytesseract` 
	among them `pytesseract` give highest accuracy and less error. If he can detect a number, he return a blank, that is very useful to handle the error.
4. When Interactive with the web, `TimeoutError` due to the connection.
# Todo
- [ ] Run Task daily using `corntab`
- [ ] Change to one script file and clean code
