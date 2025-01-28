from bottle import template, response, request
import os
import random

# Get the current directory path for template loading
current_dir = os.path.dirname(os.path.abspath(__file__))

# Game state
GRID_SIZE = 20
INITIAL_SNAKE = [210, 211, 212]  # Middle of grid, 3 cells long
DIRECTION = {
    "UP": -GRID_SIZE,
    "DOWN": GRID_SIZE,
    "LEFT": -1,
    "RIGHT": 1
}

def get_template():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Snake Game</title>
    <style>
        #game-grid {
            display: grid;
            grid-template-columns: repeat(20, 20px);
            grid-template-rows: repeat(20, 20px);
            gap: 1px;
            background-color: #333;
            border: 1px solid #444;
            width: fit-content;
            margin: 20px auto;
        }
        .grid-cell {
            width: 20px;
            height: 20px;
            background-color: #222;
        }
        .snake {
            background-color: #4CAF50;
            border-radius: 4px;
        }
        .snake-head {
            background-color: #45a049;
            border-radius: 6px;
        }
        .food {
            background-color: #ff4444;
            border-radius: 50%;
        }
        #score {
            text-align: center;
            font-size: 24px;
            color: #333;
            margin: 10px;
        }
        #game-info {
            text-align: center;
            margin: 20px;
            color: #333;
        }
    </style>
</head>
<body>
    <h1 style="text-align: center;">Snake Game</h1>
    <div id="score">Score: {{score}}</div>
    <div id="game-info">
        Use arrow keys to move
    </div>
    <div id="game-grid">
        % for i in range(400):
            % if i == snake[0]:
                <div class="grid-cell snake-head"></div>
            % elif i in snake[1:]:
                <div class="grid-cell snake"></div>
            % elif i == food:
                <div class="grid-cell food"></div>
            % else:
                <div class="grid-cell"></div>
            % end
        % end
    </div>
</body>
</html>
'''

# Route for the game page
def setup(app):
    @app.route('/game')
    def game():
        snake = INITIAL_SNAKE
        score = 0
        food_position = 55  # Random position for food
        return template(get_template(), 
            snake=snake,
            score=score,
            food=food_position
        )

    @app.post('/update_game')
    def update_game():
        data = request.json
        direction = data.get('direction')
        
        # Get current game state (you'll need to implement state management)
        snake = list(INITIAL_SNAKE)  # This should be stored in a session or database
        score = 0
        food_position = 55
        
        # Update snake position based on direction
        new_head = snake[0]
        if direction == 'UP':
            new_head -= GRID_SIZE
        elif direction == 'DOWN':
            new_head += GRID_SIZE
        elif direction == 'LEFT':
            new_head -= 1
        elif direction == 'RIGHT':
            new_head += 1
            
        # Check for collisions
        game_over = (
            new_head < 0 or 
            new_head >= 400 or
            new_head in snake[1:] or
            (direction in ['LEFT', 'RIGHT'] and new_head // GRID_SIZE != snake[0] // GRID_SIZE)
        )
        
        if game_over:
            response.content_type = 'application/json'
            return {'game_over': True, 'score': score}
            
        # Move snake
        snake.insert(0, new_head)
        
        # Check if food eaten
        if new_head == food_position:
            score += 10
            food_position = random.randint(0, 399)
            while food_position in snake:
                food_position = random.randint(0, 399)
        else:
            snake.pop()
            
        response.content_type = 'application/json'
        return {
            'game_over': False,
            'snake': snake,
            'food': food_position,
            'score': score
        }
