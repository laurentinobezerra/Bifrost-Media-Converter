import time
import os
def exibe_menu():
    print("""
========== BifrostMedia Converter ==========
Escolha uma opção:
1 - Baixar Vídeo (MP4)
2 - Baixar Áudio (MP3)
0 - Voltar
==========================================
""")
    return int(input("Escolha uma opção: "))


def baixar_video(yt):
    inicio_time = time.time()
    ys = yt.streams.get_highest_resolution()
    ys.download()
    fim_time = time.time()
    duracao = fim_time - inicio_time
    print(f"\nSeu vídeo foi baixado com sucesso! Tempo de download: {duracao:.2f}")


def baixar_audio(yt):
    inicio_time = time.time()
    ys = yt.streams.get_audio_only()
    ys.download()
    fim_time = time.time()
    duracao = fim_time - inicio_time
    print(f"\nSeu áudio foi baixado com sucesso! Tempo de download: {duracao:.2f}")


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')