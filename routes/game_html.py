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
    </style>
</head>
<body>
    <h1 style="text-align: center;">Snake Game</h1>
    <div id="game-grid">
        % for i in range(400):
        <div class="grid-cell"></div>
        % end
    </div>
</body>
</html>
''' 