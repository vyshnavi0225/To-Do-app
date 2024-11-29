from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Note model (table in the database)
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

# Route for the homepage to display all notes
@app.route('/')
def index():
    notes = Note.query.all()  # Fetch all notes from the database
    return render_template('index.html', notes=notes)

# Route to add a new note
@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    description = request.form['description']
    new_note = Note(title=title, description=description)
    try:
        db.session.add(new_note)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue adding your note'

# Route to delete a note
@app.route('/delete/<int:id>')
def delete_note(id):
    note_to_delete = Note.query.get_or_404(id)
    try:
        db.session.delete(note_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting your note'

# Initialize the database and create tables
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True, host='0.0.0.0', port=8080)  # Flask listens on all interfaces
