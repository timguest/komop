from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In memory storage for player data. Use a database in production.
players = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        handicap = request.form.get('handicap')

        players.append({'name': name, 'handicap': handicap})

        return redirect(url_for('home'))

    return render_template('home.html', players=players)

@app.route('/generate-competition')
def generate_competition():
    return render_template('competition.html')

if __name__ == '__main__':
    app.run(port=5051)
