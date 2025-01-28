
# name = "ZapAutomatic"
# version = "0.0.1-beta"
# aauthor = "Marcos Cassiano"
# description = "envio de mensagem automática no whatsapp 
#                para reporte de hora em hora.
# readme = "README.md"
# python_version = "3.12"

# Example values!
# IdGroup = "H8uW35Yat3v75OHtlc7MM8"
# Contact = "+5521982017908"

import os
import subprocess
import sys
import pyautogui
import pywhatkit

import time
from datetime import datetime

# pip install pyinstaller
# pyinstaller --noconfirm --onefile seu_programa.py

# Instala automaticamente as dependências
required_packages = ["pyautogui", "pywhatkit"]
for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("Programa iniciado!!!")

# Criação do diretório "prints"
output_folder = "prints"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# Confirmar contato a ser enviado as mensagens
while True:
    contact = input("Digite um numero de telefone ou IdGroup do WhatsApp:")
    confirm = input(f"Você digitou '{contact}'. Está correto? (yes/no): ").strip().lower()

    if confirm == "yes":
        print(f"Contato '{contact}' confirmado! Continuando...")
        break
    elif confirm == "no":
        print("Ok, vamos tentar novamente.")
    else:
        print("Resposta inválida. Digite 'yes' ou 'no'.")

print("OBS: Escolha a tela a ser capturada em 1 minuto e não mexa mais no computador")
time.sleep(6)

print("O programa está rodando e fará capturas de tela a cada 1 hora...")
time.sleep(1)
while True:

    # Gera o nome do arquivo com base na data e hora atual
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"screenshot_{current_time}.png"
    screenshot_path = os.path.join(output_folder, screenshot_filename)

    # Captura a tela e salva na pasta "prints"
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)

    # Texto para decrição da imagem enviada
    img_caption = f"BMS: {datetime.now().strftime("%H:%M")}"

    pywhatkit.sendwhats_image(contact, screenshot_path, img_caption)
    
    # Tempo para garantir que o WhatsApp Web foi carregado
    print("Aguardando o envio da imagem...")
    time.sleep(15)  

    print("Fechando a janela do WhatsApp Web e Voltando para a tela anterior...")
    pyautogui.hotkey("ctrl", "w")
    time.sleep(3)  
    pyautogui.hotkey("alt", "tab")

    # Apaga o arquivo após criar
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)
        print(f"O arquivo {screenshot_filename} foi apagado com sucesso.")
    else:
        print(f"O arquivo {screenshot_filename} não foi encontrado para exclusão.")

    # Aguarda 1 hora antes de repetir o processo
    print("Aguardando 1 hora para a próxima captura...")
    time.sleep(15)  # 3600 segundos = 1 hora
