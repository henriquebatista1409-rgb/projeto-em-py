from flask import Flask , render_template, request
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def login():
    USUARIO_CORRETO = "pedro"
    SENHA_HASH = generate_password_hash("1234") # Senha correta é "1234"
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    print(f"usuario e senha recebido: '{usuario}', '{senha}'")

    if usuario == USUARIO_CORRETO and check_password_hash(SENHA_HASH, senha):
        return  "Login realizado com sucesso!"
    else:
        return render_template('login.html', mensagem="Usuário ou senha incorretos.")
    
   

if __name__ == '__main__':
    app.run(debug=True)
