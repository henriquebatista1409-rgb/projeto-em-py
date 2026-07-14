# Sistema de Login

Sistema simples de autenticação com cadastro e login de usuários, feito com Flask e Supabase.

## Funcionalidades

- Cadastro de novos usuários
- Login com validação de usuário e senha
- Senhas armazenadas com hash (nunca em texto puro), usando `werkzeug.security`
- Banco de dados PostgreSQL hospedado no Supabase

## Tecnologias usadas

- Python 3
- Flask
- Supabase (PostgreSQL)
- python-dotenv
- Werkzeug (hash de senha)

## Como rodar o projeto

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd <pasta-do-projeto>
```

2. Instale as dependências:
```bash
pip install flask supabase python-dotenv
```

3. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
SUPABASE_URL=sua_url_aqui
SUPABASE_secret_key=sua_chave_aqui
```

4. Rode o servidor:
```bash
python3 app.py
```

5. Acesse `http://localhost:5000` no navegador

## Estrutura do banco de dados

Tabela `usuarios`:

| Coluna | Tipo | Descrição |
|---|---|---|
| id | int8 | Identificador único (automático) |
| usuario | text | Nome de usuário |
| senha_hash | text | Hash da senha (nunca a senha crua) |

## Próximos passos

- [ ] Adicionar sistema de sessão (manter usuário logado)
- [ ] Adicionar logout
- [ ] Validações extras no cadastro (senha mínima, usuário duplicado com mensagens melhores)

---

Projeto de estudo, desenvolvido como parte do aprendizado de desenvolvimento back-end.