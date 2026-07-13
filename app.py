import pyautogui
from time import sleep

pyautogui.PAUSE = 0.5
interrupido = False  # Indicar se o processo foi interrompido

def fechar_janela():
    # Fechar a janela, caso esteja aberta
    pyautogui.hotkey("alt", "f4")
    print("Janela fechada.")

def enviar_convites(contador, convites, interrupido):
    
    # Loop para clicar no botão "Conectar" 10 vezes
    while contador < convites:
        pyautogui.scroll(-100)  # Scroll para baixo para garantir que o botão "Conectar" esteja visível
        sleep(1)  # Aguardar 1 segundo para garantir que a página carregou
        print(f"\nTentativa {contador + 1} de clicar no botão 'Conectar'...")
        print("Procurando o botão 'Conectar' na tela...")

        try:
            # Localizar o botão "Conectar" na tela
            localizacao_botao = pyautogui.locateCenterOnScreen("botao-conectar.png", confidence=0.8)

            if localizacao_botao is not None:
                # Clicar no botão "Conectar"
                pyautogui.click(localizacao_botao)
                contador += 1
                print(f"Clique {contador} realizado com sucesso!")
            else:
                print("Botão 'Conectar' não encontrado na tela.")
                # Fechar a janela, caso esteja aberta
                fechar_janela()
                interrupido = True
                break
        except Exception as e:
            print(f"Ocorreu um erro ao localizar o botão: {e}")
            break

    if interrupido:
        print("O processo foi interrompido devido a um erro ou botão não encontrado.")
    else:
        print("Todos os convites foram enviados com sucesso!")
        fechar_janela()

    print("Processo finalizado.")

def main():

  contador = 0  # Inicializar o contador de cliques
  convites = 60  # Definir o número de convites a serem enviados

  try:
    
    # Abrir navegador
    pyautogui.press("win")
    pyautogui.write("chrome")
    pyautogui.press("enter")

    sleep(4)  # Aguardar 4 segundos para o navegador abrir

    # Escrever o endereço do site
    pyautogui.hotkey("ctrl", "l")
    pyautogui.write("https://www.linkedin.com/mynetwork/grow/")

    sleep(2)  # Aguardar 2 segundos para o endereço ser digitado

    pyautogui.press("enter")  # Pressionar Enter para acessar o site

    sleep(5)  # Aguardar 5 segundos para o site carregar

    # Obter posição do Scroll da tela
    pyautogui.click(x=1358, y=160)  # Clicar na posição do Scroll para garantir que ele esteja ativo
    pyautogui.scroll(-500)  # Scroll para baixo para garantir que o botão "Conectar" esteja visível

  except Exception as e:
    print(f"Ocorreu um erro durante a execução do programa: {e}")
    fechar_janela()
    interrupido = True
    return None

  # Função do loop para enviar convites
  enviar_convites(contador, convites, interrupido)

  if contador == convites:
    print(f"\nTodos os convites foram enviados com sucesso!")
  elif contador > 0:
    print(f"\nProcesso interrompido. Foram enviados {contador} convites antes da interrupção.")
  elif contador == 0:
    print("\nNenhum convite foi enviado. O processo foi interrompido antes de enviar qualquer convite.")

  fechar_janela()

if __name__ == "__main__":
    main()

    if interrupido:
        print(f"\nO processo foi interrompido devido a um erro ou botão não encontrado.")
    else:
        print("\nProcesso finalizado.")