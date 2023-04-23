from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def message_board():
    if request.method == 'POST':
        # Get user's message
        message = request.form['message']
        # Add message to database
        conn = sqlite3.connect('messages.db')
        c = conn.cursor()
        c.execute("INSERT INTO messages (message) VALUES (?)", (message,))
        conn.commit()
        conn.close()
    # Retrieve all messages from database
    conn = sqlite3.connect('messages.db')
    c = conn.cursor()
    c.execute("SELECT message FROM messages")
    messages = c.fetchall()
    conn.close()
    # Render template with messages
    return render_template('message_board.html', messages=messages)