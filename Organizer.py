import os
import shutil

pasta = input("Digite o caminho da pasta que deseja organizar: ")

tipos_arquivos = {
       "Imagens": [".png", ".jpg", ".jpeg"],
       "PDF": [".pdf", ".PDF"],
       "Musicas": [".mp3", ".m4a"],
       "Video": [".avi", ".mov", ".mp4"],
       "Documentos": [".docx", ".txt"],
}

for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho_arquivo):
        for pasta_destino, extensoes in tipos_arquivos.items():
            if arquivo.lower().endswith(tuple(extensoes)):

                nova_pasta = os.path.join(pasta, pasta_destino)

                if not os.path.exists(nova_pasta):
                    os.makedirs(nova_pasta)

                shutil.move(caminho_arquivo, os.path.join(nova_pasta, arquivo))

print("Arquivos organizados com sucesso!")