def printGrid(grid):
	printOut = ""
	for row in grid:
		for num in row:
			if num == "":
				printOut += "_ "
			else:
				printOut += str(num) + " "
		printOut += "\n"
	print(printOut)

def is_legal(curr_pos, new_pos, grid, grid_size):
	# out of bounds
	if new_pos[0] not in range(0, grid_size):
		return False
	if new_pos[1] not in range(0, grid_size):
		return False
	# wrong direction
	if new_pos[0] < curr_pos[0]:
		return False
	if new_pos[1] < curr_pos[1]:
		return False
	# illegal path
	illegal_move = grid[curr_pos[1]][curr_pos[0]]
	if move_south(curr_pos,"")[0] == new_pos:
		if illegal_move == "S":
			return False
	if move_east(curr_pos,"")[0] == new_pos:
		if illegal_move == "E":
			return False
	return True

def move_south(curr_pos, my_path):
	new_pos = [curr_pos[0], curr_pos[1]+1]
	new_path = my_path + "S"
	return [new_pos, new_path]

def move_east(curr_pos, my_path):
	new_pos = [curr_pos[0]+1, curr_pos[1]]
	new_path = my_path + "E"
	return [new_pos, new_path]

def reached_finish(pos, grid_size):
	if pos == [grid_size-1, grid_size-1]:
		return True
	return False

def create_grid(path, grid_size):
	grid = [[""] * grid_size for i in range(grid_size)]
	x = 0
	y = 0
	for move in path:
		if move == "S":
			grid[y][x] = "S"
			y += 1
		elif move == "E":
			grid[y][x] = "E"
			x += 1
		else:
			print("SOMETHING WENT WRONG")
			return
	return grid

cases = int(input())
for case in range(1, cases + 1):
    grid_size = int(input())
    illegal_path = str(input())
    grid = create_grid(illegal_path, grid_size)
    my_path = ""
    my_curr_pos = [0,0]

    while not reached_finish(my_curr_pos, grid_size):
        if is_legal(my_curr_pos, move_south(my_curr_pos, my_path)[0], grid, grid_size):
            my_curr_pos, my_path = move_south(my_curr_pos, my_path)
        if is_legal(my_curr_pos, move_east(my_curr_pos, my_path)[0], grid, grid_size):
            my_curr_pos, my_path = move_east(my_curr_pos, my_path)

    print("Case #{}: {}".format(case, my_path))
	
