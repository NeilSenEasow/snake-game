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
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            let currentDirection = 'RIGHT';
            let gameActive = true;
            
            // Handle keyboard controls
            document.addEventListener('keydown', (e) => {
                if (!gameActive) return;
                
                switch(e.key) {
                    case 'ArrowUp':
                        if (currentDirection !== 'DOWN') {
                            currentDirection = 'UP';
                            updateGame('UP');
                        }
                        break;
                    case 'ArrowDown':
                        if (currentDirection !== 'UP') {
                            currentDirection = 'DOWN';
                            updateGame('DOWN');
                        }
                        break;
                    case 'ArrowLeft':
                        if (currentDirection !== 'RIGHT') {
                            currentDirection = 'LEFT';
                            updateGame('LEFT');
                        }
                        break;
                    case 'ArrowRight':
                        if (currentDirection !== 'LEFT') {
                            currentDirection = 'RIGHT';
                            updateGame('RIGHT');
                        }
                        break;
                }
            });

            function updateGame(direction) {
                fetch('/update_game', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ direction: direction })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.game_over) {
                        gameActive = false;
                        alert('Game Over! Score: ' + data.score);
                        location.reload();
                        return;
                    }
                    updateSnake(data.snake);
                    updateFood(data.food);
                    updateScore(data.score);
                });
            }

            function updateSnake(snake) {
                // Clear all snake cells
                document.querySelectorAll('.snake, .snake-head').forEach(cell => {
                    cell.className = 'grid-cell';
                });
                
                // Update snake position
                snake.forEach((pos, index) => {
                    const cell = document.querySelector(`[data-index="${pos}"]`);
                    if (cell) {
                        cell.className = `grid-cell ${index === 0 ? 'snake-head' : 'snake'}`;
                    }
                });
            }

            function updateFood(foodPos) {
                document.querySelectorAll('.food').forEach(cell => {
                    cell.className = 'grid-cell';
                });
                const foodCell = document.querySelector(`[data-index="${foodPos}"]`);
                if (foodCell) {
                    foodCell.className = 'grid-cell food';
                }
            }

            function updateScore(score) {
                document.getElementById('score').textContent = 'Score: ' + score;
            }

            // Auto-movement
            setInterval(() => {
                if (gameActive) {
                    updateGame(currentDirection);
                }
            }, 200); // Move every 200ms
        });
    </script>
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
                <div class="grid-cell snake-head" data-index="{{i}}"></div>
            % elif i in snake[1:]:
                <div class="grid-cell snake" data-index="{{i}}"></div>
            % elif i == food:
                <div class="grid-cell food" data-index="{{i}}"></div>
            % else:
                <div class="grid-cell" data-index="{{i}}"></div>
            % end
        % end
    </div>
</body>
</html>
''' 