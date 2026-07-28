# Flask Notes

A simple Flask web app for creating and organizing personal notes.

## Requirements
- Python 3.x
- Flask
- SQLite

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/flask-notes.git
   cd flask-notes
   ```
2. Install the required packages:
   ```bash
   pip install Flask
   ```
3. Initialize the database:
   ```bash
   python -c 'from app import init_db; init_db()'
   ```
4. Run the app:
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000/`.