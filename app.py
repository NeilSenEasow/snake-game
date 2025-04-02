from flask import Flask, render_template, request, jsonify
from time import time
from datetime import datetime
import json
import os
//testing 
app = Flask(__name__)

# Game state
snake = [42, 41, 40]  
food = 200  
foodEaten = 0
start_time = 0
GRID_SIZE = 20
LEADERBOARD_FILE = 'leaderboard.json'

# Initialize leaderboard file if it doesn't exist
if not os.path.exists(LEADERBOARD_FILE):
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump([], f)

def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_to_leaderboard(score_data):
    leaderboard = load_leaderboard()
    score_data['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    leaderboard.append(score_data)
    # Sort by score in descending order and keep top 10
    leaderboard.sort(key=lambda x: x['score'], reverse=True)
    leaderboard = leaderboard[:10]
    
    with open(LEADERBOARD_FILE, 'w') as f:
        json.dump(leaderboard, f, indent=2)  # Added indent for better readability

def generate_food():
    from random import randint
    while True:
        new_food = randint(0, GRID_SIZE * GRID_SIZE - 1)
        if new_food not in snake:
            return new_food

def calculate_final_score(food_eaten, time_taken):
    return (food_eaten * 100) + (time_taken * 2)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/game')
def game():
    global snake, food, foodEaten, start_time
    snake = [42, 41, 40]
    food = generate_food()
    foodEaten = 0
    start_time = time()
    leaderboard = load_leaderboard()
    return render_template('game.html', snake=snake, food=food, foodEaten=foodEaten, leaderboard=leaderboard)

@app.route('/update_game', methods=['POST'])
def update_game():
    global snake, food, foodEaten
    
    data = request.get_json()
    direction = data.get('direction')
    
    head = snake[0]
    row = head // GRID_SIZE
    col = head % GRID_SIZE
    
    # Calculate new head position with wrapping
    if direction == 'UP':
        new_row = (row - 1) % GRID_SIZE
        new_head = new_row * GRID_SIZE + col
    elif direction == 'DOWN':
        new_row = (row + 1) % GRID_SIZE
        new_head = new_row * GRID_SIZE + col
    elif direction == 'LEFT':
        new_col = (col - 1) % GRID_SIZE
        new_head = row * GRID_SIZE + new_col
    elif direction == 'RIGHT':
        new_col = (col + 1) % GRID_SIZE
        new_head = row * GRID_SIZE + new_col
    else:
        elapsed_time = int(time() - start_time)
        final_score = calculate_final_score(foodEaten, elapsed_time)
        return jsonify({
            'game_over': True, 
            'foodEaten': foodEaten,
            'time': elapsed_time,
            'final_score': final_score
        })

    # Check collision with self
    if new_head in snake:
        elapsed_time = int(time() - start_time)
        final_score = calculate_final_score(foodEaten, elapsed_time)
        return jsonify({
            'game_over': True, 
            'foodEaten': foodEaten,
            'time': elapsed_time,
            'final_score': final_score
        })
    
    snake.insert(0, new_head)
    
    if new_head == food:
        foodEaten += 1
        food = generate_food()
    else:
        snake.pop()
    
    elapsed_time = int(time() - start_time)
    current_score = calculate_final_score(foodEaten, elapsed_time)
    
    return jsonify({
        'snake': snake,
        'food': food,
        'foodEaten': foodEaten,
        'time': elapsed_time,
        'current_score': current_score,
        'game_over': False
    })

@app.route('/submit_score', methods=['POST'])
def submit_score():
    data = request.get_json()
    score_data = {
        'name': data.get('name', 'Anonymous'),
        'score': data.get('final_score', 0),
        'foodEaten': data.get('foodEaten', 0),
        'time': data.get('time', 0)
    }
    save_to_leaderboard(score_data)
    return jsonify({'success': True, 'leaderboard': load_leaderboard()})

@app.route('/get_leaderboard', methods=['GET'])
def get_leaderboard():
    return jsonify({'leaderboard': load_leaderboard()})

if __name__ == '__main__':
    app.run(debug=True)