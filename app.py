from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Página principal
@app.route("/")
def home():
    return render_template("index.html")

# Rota para processar o formulário de contato
@app.route("/enviar_mensagem", methods=["POST"])
def enviar_mensagem():
    nome = request.form.get("nome")
    email = request.form.get("email")
    mensagem = request.form.get("mensagem")

    # Aqui você pode salvar em banco de dados, enviar email etc.
    print(f"Mensagem recebida de {nome} ({email}): {mensagem}")

    return jsonify({"status": "sucesso", "mensagem": "Mensagem enviada com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True)
