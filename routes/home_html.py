def get_template():
    return '''
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Snake Game</title>
    <style>
        body {
            text-align: center;
            padding-top: 50px;
        }
        a {
            display: inline-block;
            padding: 10px 20px;
            background-color: #333;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        a:hover {
            background-color: #444;
        }
    </style>
</head>
<body>
    <h1>Welcome to Snake Game</h1>
    <a href="/game">Play Game</a>
</body>
</html>
''' 