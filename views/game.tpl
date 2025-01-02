<!DOCTYPE html>
<html>
<head>
    <title>{{title}}</title>
    <style>
        #game-grid {
            display: grid;
            grid-template-columns: repeat({{size}}, 20px);
            grid-template-rows: repeat({{size}}, 20px);
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
    <h1 style="text-align: center;">{{title}}</h1>
    <div id="game-container">
        <div id="game-grid">
            % for i in range(size * size):
                <div class="grid-cell" data-index="{{i}}"></div>
            % end
        </div>
    </div>
</body>
</html> 