from flask import Blueprint, request, jsonify
from app.services import processar_traducao

bp = Blueprint("routes", __name__)

@bp.route("/")
def home():
    return jsonify({"message": "API de Tradução de Arquivos está funcionando!"})

@bp.route("/traduzir", methods=["POST"])
def traduzir():
    """
    Endpoint para traduzir um arquivo PowerPoint (.pptx)
    """
    if "file" not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400
    
    file = request.files["file"]
    if not file.filename.endswith(".pptx"):
        return jsonify({"error": "Apenas arquivos .pptx são suportados"}), 400
    
    # Processar a tradução
    try:
        caminho_saida, log = processar_traducao(file)
        return jsonify({
            "message": "Tradução concluída com sucesso!",
            "arquivo_traduzido": caminho_saida,
            "log": log
        })
    except Exception as e:
        return jsonify({"error": f"Erro ao processar o arquivo: {str(e)}"}), 500