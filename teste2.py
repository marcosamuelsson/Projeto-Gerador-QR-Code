import os

def verificar_tipo_arquivo(caminho_arquivo):
    # Verifica se o arquivo existe
    if not os.path.isfile(caminho_arquivo):
        return "O arquivo não existe."

    # Obtém a extensão do arquivo
    _, extensao = os.path.splitext(caminho_arquivo)

    # Verifica se a extensão é .txt ou .xlsx
    if extensao.lower() == '.txt':
        return "O arquivo é um arquivo de texto (.txt)."
    elif extensao.lower() == '.xlsx':
        return "O arquivo é um arquivo do Excel (.xlsx)."
    else:
        return "O arquivo não é nem .txt nem .xlsx."

# Exemplo de uso
caminho = 'seu_arquivo_aqui.txt'  # Substitua pelo caminho do seu arquivo
resultado = verificar_tipo_arquivo(caminho)
print(resultado)