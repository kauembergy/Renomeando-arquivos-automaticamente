# pseudocódigo para o projeto 

# 1. importar todas as bibliotecas necessárias 
import os

# 2. pegar o caminho da pasta necessária
caminho_da_pasta = os.path.abspath("C:/Users/kauem/OneDrive/Área de Trabalho/Projeto de automação para renomear arquivos/20042023")
# 3. ler o nome da pasta 
Nome_pasta = os.path.basename(caminho_da_pasta) 
# 4. entrar na pasta
dentro_da_pasta = os.listdir(caminho_da_pasta) 
# 6. renomear cada arquivo dentro da pasta com o código da pasta
for arquivo in dentro_da_pasta:
    # caminho para o nome do arquivo antes de renomear
    nome_arquivo = os.path.join(caminho_da_pasta,arquivo)
    # dá um split no nome do arquivo com o nome e a extensão
    aruiqvo_escrito_antes, extensao_arquivo = os.path.splitext(arquivo)
    #renomeia o arquivo
    nome_arquivo_novo = f"{aruiqvo_escrito_antes}_{Nome_pasta}_{extensao_arquivo}"
    #cria um caminho para o arquivo renomeado
    caminho_novo_arquivo = os.path.join(caminho_da_pasta, nome_arquivo_novo)
    #renomeia o arquivo
    os.rename(nome_arquivo,caminho_novo_arquivo)

print("Arquivos renomeados com sucesso")