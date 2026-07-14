from flask import Flask , render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
SUPABASE_secret_key = os.getenv("SUPABASE_secret_key")
supabase: Client = create_client(supabase_url, SUPABASE_secret_key)

print("Chave carregada:", SUPABASE_secret_key[:10])  # só os 10 primeiros caracteres, por segurança

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def login():
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    
    response = supabase.table("usuarios").select("*").eq("usuario", usuario).execute()

    if len(response.data) == 0:
        return render_template("login.html", mensagem="Usuário não encontrado.")
    
    usuario_encontrado = response.data[0]
    senha_hash = usuario_encontrado["senha_hash"]
    
    if check_password_hash(senha_hash, senha):
        return "Login realizado com sucesso!"
    else:
        return render_template("login.html", mensagem="Usuário ou senha incorretos.")
    

@app.route("/registrar", methods=["GET", "POST"])
def registrar():
 if request.method == "POST":
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    
    # Verifica se o usuário já existe
    response = supabase.table("usuarios").select("*").eq("usuario", usuario).execute()
    if len(response.data) > 0:
        return render_template("registrar.html", mensagem="Usuário já existe.")
    
    # Cria o hash da senha
    senha_hash = generate_password_hash(senha)
    
    # Insere o novo usuário no banco de dados
    supabase.table("usuarios").insert({"usuario": usuario, "senha_hash": senha_hash}).execute()
    
    return render_template("registrar.html", mensagem="Usuário registrado com sucesso!")
 
 return render_template("registrar.html")

if __name__ == '__main__':
    app.run(debug=True) 
