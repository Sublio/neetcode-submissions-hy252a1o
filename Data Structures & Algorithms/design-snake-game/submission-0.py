from collections import deque

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.score = 0
        self.snake = deque([(0, 0)])
        self.snake_set = {(0, 0)}
        self.directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }
        
    def move(self, direction: str) -> int:
        dr, dc = self.directions[direction]
        head_r, head_c = self.snake[0]
        new_r, new_c = head_r + dr, head_c + dc
        
        if new_r < 0 or new_r >= self.height or new_c < 0 or new_c >= self.width:
            return -1
        
        tail = self.snake.pop()
        self.snake_set.remove(tail)
        
        if (new_r, new_c) in self.snake_set:
            return -1
        
        self.snake.appendleft((new_r, new_c))
        self.snake_set.add((new_r, new_c))
        
        if self.food_index < len(self.food) and self.food[self.food_index] == [new_r, new_c]:
            self.score += 1
            self.food_index += 1
            self.snake.append(tail)
            self.snake_set.add(tail)
        
        return self.score