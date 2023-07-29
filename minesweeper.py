# creating a minesweep game

# input_grid: grid where hash(#) represents a mine and each dash (-) represents a mine-free spot
input_grid = [["-", "-", "#", "-", "#"],
              ["-", "-", "-", "-", "#"],
              ["#", "-", "-", "-", "-"],
              ["-", "-", "#", "-", "#"],
              ["#", "#", "-", "-", "-"]]

print(f'This is the input grid:\n {input_grid}')

#expected_grid: grid where dash is replaced by a digit that indicates the number of mines immediately adjacent
expected_grid = [["0", "1", "#", "3", "#"], 
                 ["1", "2", "1", "3", "#"],
                 ["#", "2", "1", "3", "2"],
                 ["3", "4", "#", "2", "#"],
                 ["#", "#", "2", "2", "1"]]

print(f'This is the expected grid:\n {expected_grid}')

# calculated_grid: create a function to produce a grid
def calculated_grid(grid):
    puzzle = []
    row = len(grid)
    column = len(grid[0])

    for row in range(len(grid)):
        puzzle.append(grid[row][:])
        for column in range(len(grid[row])):
            if grid[row][column] == '#':
                continue
            count = 0
            for direction in [(1,0),(-1,0), (0,1), (0,-1),(1,1),(-1,-1),(1,-1), (-1,1)]:
                direction_row, direction_column = row + direction[0], column + direction[1]
                try:
                    if direction_row >= 0 and direction_column >= 0 and grid[direction_row][direction_column] == '#':
                        count += 1
                except IndexError:
                    pass
            puzzle[row][column] = count
    return puzzle

print(f'This is the calculated grid: \n {calculated_grid(input_grid)}')