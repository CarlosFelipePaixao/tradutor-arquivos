=========================
TRADUTOR DE DOCUMENTOS
=========================

Este programa permite traduzir arquivos .docx, .pdf e .txt automaticamente.

Você pode usar de duas formas:

-----------------------------------------
1. MODO INTERFACE GRÁFICA (Tkinter)
-----------------------------------------
- Execute o script com duplo clique OU use:

    python tradutor.py

- Selecione o arquivo que deseja traduzir.
- Escolha o idioma de destino.
- O arquivo será traduzido e poderá ser salvo onde desejar.


-----------------------------------------
2. MODO AUTOMÁTICO VIA CONFIG.JSON
-----------------------------------------

- Configure o arquivo "config.json" com os blocos de tradução desejados.

  Exemplo de bloco:
  
    {
      "idioma_origem": "auto",
      "idioma_destino": "en",
      "diretoria": "./documentos/ingles"
    }

- Você pode adicionar quantos blocos quiser. Exemplo com 3 blocos:
  
    {
      "blocos": [
        {
          "idioma_origem": "auto",
          "idioma_destino": "en",
          "diretoria": "./documentos/ingles"
        },
        {
          "idioma_origem": "auto",
          "idioma_destino": "es",
          "diretoria": "./documentos/espanhol"
        },
        {
          "idioma_origem": "auto",
          "idioma_destino": "fr",
          "diretoria": "./documentos/frances"
        }
      ]
    }

- Para executar o modo automático, use no terminal:

    python tradutor.py --config config.json

- O programa irá traduzir automaticamente todos os arquivos nas pastas indicadas.

- Os arquivos traduzidos serão salvos no mesmo diretório com um sufixo indicando o idioma. Exemplo:

    relatorio.docx  →  relatorio_en.docx
    resumo.pdf      →  resumo_es.pdf


-----------------------------------------
Idiomas suportados:
-----------------------------------------
- en → Inglês
- es → Espanhol
- fr → Francês
- de → Alemão
- it → Italiano
- pt → Português

=========================
Qualquer dúvida, fale com Carlos :)
=========================
