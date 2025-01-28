
# name = "ZapAutomatic"
# version = "0.0.1-beta"
# aauthor = "Marcos Cassiano"
# description = "envio de mensagem automática no whatsapp 
#                para reporte de hora em hora.
# readme = "README.md"
# python_version = "3.12"

import os
import subprocess
import sys
import pyautogui
import pywhatkit
import pywin32

import time
from datetime import datetime

# Instala automaticamente as dependências
required_packages = ["pyautogui", "pywhatkit", "pywin32"]
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
    time.sleep(15)  
    pyautogui.hotkey("ctrl", "w")
    time.sleep(15)  
    pyautogui.hotkey("alt", "tab")
    time.sleep(15)  
    # Apaga o arquivo após criar
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)
    else:
        print(f"O arquivo {screenshot_filename} não foi encontrado para exclusão.")

    time.sleep(3515)  # 3600 segundos = 1 hora
