from flask import Flask, render_template, request, redirect, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT, category TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, pinned BOOLEAN DEFAULT 0)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('SELECT title, content, category, id FROM notes ORDER BY pinned DESC, created_at DESC')
    notes = c.fetchall()
    conn.close()
    return render_template('index.html', notes=notes)

@app.route('/notes', methods=['POST'])
def create_note():
    title = request.form['title']
    content = request.form['content']
    category = request.form.get('category', '')
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    c.execute('INSERT INTO notes (title, content, category) VALUES (?, ?, ?)', (title, content, category))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/notes/<int:note_id>/edit', methods=['GET', 'POST'])
def edit_note(note_id):
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form.get('category', '')
        c.execute('UPDATE notes SET title=?, content=?, category=?, updated_at=CURRENT_TIMESTAMP WHERE id=?', (title, content, category, note_id))
        conn.commit()
        conn.close()
        return redirect('/')
    c.execute('SELECT title, content, category FROM notes WHERE id=?', (note_id,))
    note = c.fetchone()
    conn.close()
    return render_template('edit_note.html', note=note, id=note_id)
