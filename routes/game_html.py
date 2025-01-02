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