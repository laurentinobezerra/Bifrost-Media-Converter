import subprocess
import sys

# Função para instalar pacotes automaticamente
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Tenta importar o pytubefix; se falhar, instala automaticamente
try:
    from pytubefix import YouTube
except ImportError:
    print("Instalando dependências...")
    install("pytubefix==8.3.0")
    from pytubefix import YouTube  # Tenta importar novamente

from pytubefix.cli import on_progress
import utils



#Execução do Programa
def main():
    print("Olá, bem-vindo ao BifrostMedia Converter!")
    
    while True:
        url = input("Informe o url do vídeo que deseja baixar: ")
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"\nTítulo do vídeo: {yt.title}")
        
        while True:
            opcao = utils.exibe_menu()
            
            match opcao:
                case 1:
                    utils.baixar_video(yt)
                case 2:
                    utils.baixar_audio(yt)
                case 0:
                    print("Voltando ao menu principal.")
                    break
                case _:
                    print("Opção inválida, tente novamente.")
        
        continuar = input("\nDeseja baixar outro vídeo? (s/n): ").strip().lower()
        if (continuar != "s"):
            print("Encerrando progama, até a próxima!")
            break
        utils.limpar_terminal()
if __name__ == "__main__":
    main()