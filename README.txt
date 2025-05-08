# Tradutor de Documentos em Lote

traduz documentos em lote mantendo formatação e imagens originais

## Funcionalidades

- Tradução em lote de múltiplos documentos
- Preservação de formatação original
- Manutenção de imagens nos documentos
- Suporte a múltiplos formatos
- Processamento via arquivo de configuração JSON

## Formatos Suportados

- Microsoft Word (.docx)
- PDF (.pdf)
- Arquivos de texto (.txt)
- PowerPoint (.pptx)

## Idiomas Suportados

- Inglês (en)
- Espanhol (es)
- Francês (fr)
- Alemão (de)
- Italiano (it)
- Português (pt)



## Estrutura do Projeto

```
projeto/
│
├── main.py           # Arquivo principal
├── requirements.txt  # Dependências
├── config.json      # Arquivo de configuração
└── README.md        # Este arquivo
```

### Em Documentos Word
- Preservação da estrutura original
- Manutenção de posicionamento

## Em PowerPoint
- Mapeamento de coordenadas das imagens
- Salvamento temporário
- Recriação do novo arquivo

### Tradução

Utiliza a biblioteca `deep_translator` com Google Translate:
```python
from deep_translator import GoogleTranslator
translator = GoogleTranslator(source='en', target='pt')
```

### Formato do JSON de Configuração

```json
{
    "blocos": [
        {
            "idioma_origem": "auto",  // Use "auto" para detecção automática
            "idioma_destino": "pt",   // Idioma alvo
            "diretorio": "caminho/para/arquivos"
        }
    ]
}
```

- Os arquivos traduzidos são salvos com sufixo do idioma alvo
- Mantém a formatação original dos documentos
- Preserva imagens e suas posições
- Requer conexão com internet para tradução

