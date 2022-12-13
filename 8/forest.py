class Forest:
    
    @classmethod
    def parse(self, input_file: str) -> list[list[int]]:
        with open(input_file, 'r') as file:
            lines = [line.strip() for line in file]
            grid: list[list[int]] = []
            
            for x, line in enumerate(lines):
                grid.append([])
                
                for char in line:
                    grid[x].append(int(char))
            
            return grid
    
    # 1
    
    @classmethod
    def get_number_visible_trees(self, grid: list[list[int]]) -> int:
        length = len(grid)
        visible_grid = ([[self.__is_visible(grid, x, y) for y in range(length)] for x in range(length)])
        return sum(sum(visible_grid, []))
    
    @classmethod
    def __is_visible(self, grid: list[list[int]], x: int, y: int) -> bool:
        length = len(grid)
        return x == 0 or x == length or y == 0 or y == length or \
                    self.__look_up(grid, x, y) or self.__look_down(grid, x, y) or \
                    self.__look_left(grid, x, y) or self.__look_right(grid, x, y)
    
    @classmethod
    def __look_up(self, grid: list[list[int]], x: int, y: int) -> bool:
        return all(
            map(
                lambda xi: grid[xi][y] < grid[x][y],
                range(x)
            )
        )
    
    @classmethod    
    def __look_down(self, grid: list[list[int]], x: int, y: int) -> bool:
        return all(
            map(
                lambda xi: grid[xi][y] < grid[x][y],
                range(x+1, len(grid))
            )
        )
    
    @classmethod    
    def __look_left(self, grid: list[list[int]], x: int, y: int) -> bool:
        return all(
            map(
                lambda yi: grid[x][yi] < grid[x][y],
                range(y)
            )
        )
    
    @classmethod    
    def __look_right(self, grid: list[list[int]], x: int, y: int) -> bool:
        return all(
            map(
                lambda yi: grid[x][yi] < grid[x][y],
                range(y+1, len(grid))
            )
        )
    
    # 2
    
    @classmethod
    def get_best_scenic_score(self, grid: list[list[int]]) -> int:
        length = len(grid)
        scenic_score_grid = ([[self.__get_scenic_score(grid, x, y) for y in range(length)] for x in range(length)])
        return max(max(score) for score in scenic_score_grid)
    
    @classmethod
    def __get_scenic_score(self, grid: list[list[int]], x: int, y: int) -> int:
        return self.__count_up(grid, x, y) * self.__count_down(grid, x, y) * self.__count_left(grid, x, y) * self.__count_right(grid, x, y)
    
    @classmethod
    def __count_up(self, grid: list[list[int]], x: int, y: int) -> bool:
        visible = 0
        
        for xi in range(x-1, -1, -1):
            visible += 1
            
            if grid[xi][y] >= grid[x][y]:
                break
        
        return visible
    
    @classmethod
    def __count_down(self, grid: list[list[int]], x: int, y: int) -> bool:
        visible = 0
        
        for xi in range(x+1, len(grid)):
            visible += 1
            
            if grid[xi][y] >= grid[x][y]:
                break
        
        return visible
    
    @classmethod
    def __count_left(self, grid: list[list[int]], x: int, y: int) -> bool:
        visible = 0
        
        for yi in range(y-1, -1, -1):
            visible += 1
            
            if grid[x][yi] >= grid[x][y]:
                break
        
        return visible
    
    @classmethod
    def __count_right(self, grid: list[list[int]], x: int, y: int) -> bool:
        visible = 0
        
        for yi in range(y+1, len(grid)):
            visible += 1
            
            if grid[x][yi] >= grid[x][y]:
                break
        
        return visible