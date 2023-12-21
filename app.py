from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'D&dstr0ke77' and password == 'Epiteqtkek1':
        # Utilisateur authentifié, affichez le message
        return render_template('success.html', flag='ctf{sefb552}')
    else:
        # Mauvais identifiants, redirigez vers la page d'accueil
        return render_template('index.html', error='Invalid username or password')

if __name__ == '__main__':
    app.run(debug=True)
