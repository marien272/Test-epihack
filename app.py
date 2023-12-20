from flask import Flask, render_template, request

app = Flask(__name__)

# ... Autres configurations ...

@app.route('/')
def index():
    return render_template('index.html')

# Vulnérabilité SQL Injection (à des fins éducatives uniquement)
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Attention: Ne jamais utiliser cette approche en production
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    # Exécutez la requête SQL et vérifiez si l'utilisateur est authentifié

    # ... Logique d'authentification ...

    return "Login successful"  # Cela doit être remplacé par une redirection ou une réponse appropriée

if __name__ == '__main__':
    app.run(debug=True)
