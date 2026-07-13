# 🤖 LinkedIn Auto Connect Bot

Automação desenvolvida em **Python** utilizando **PyAutoGUI** para localizar o botão **"Conectar"** na tela e realizar interações automáticas por meio de reconhecimento de imagem.

> **⚠️ Aviso Importante**
>
> Este projeto foi desenvolvido **para fins de estudo e aprendizado em automação de interface gráfica (GUI Automation)** utilizando Python.
>
> O uso de automações em plataformas de terceiros pode violar seus Termos de Uso. Utilize este projeto apenas em ambientes de teste, aplicações próprias ou quando possuir autorização para automatizar a interface.

---

# 📑 Índice

- [✨ Funcionalidades](#-funcionalidades)
- [🛠️ Tecnologias](#️-tecnologias)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [⚙️ Requisitos](#️-requisitos)
- [🚀 Instalação](#-instalação)
- [▶️ Como Executar](#️-como-executar)
- [🖼️ Captura da Imagem](#️-captura-da-imagem)
- [📍 Captura de Coordenadas](#-captura-de-coordenadas)
- [⚙️ Configuração](#️-configuração)
- [📋 Fluxo de Funcionamento](#-fluxo-de-funcionamento)
- [❗ Possíveis Problemas](#-possíveis-problemas)
- [📄 Licença](#-licença)

---

# ✨ Funcionalidades

- ✅ Abre automaticamente o Google Chrome
- ✅ Acessa uma página pré-definida
- ✅ Localiza um botão através de reconhecimento de imagem
- ✅ Realiza rolagem automática da página
- ✅ Clica automaticamente no botão encontrado
- ✅ Conta quantas ações foram realizadas
- ✅ Fecha o navegador ao finalizar
- ✅ Interrompe automaticamente caso o botão não seja localizado
- ✅ Tratamento básico de exceções

---

# 🛠️ Tecnologias

- Python 3
- PyAutoGUI
- OpenCV
- Pillow

---

# 📁 Estrutura do Projeto

```text
LinkedIn-AutoConnect/
│
├── app.py
├── capturar-posicao.py
├── botao-conectar.png
├── requirements.txt
├── README.md
└── _config.yml
```

---

# ⚙️ Requisitos

- Python 3.10 ou superior
- Google Chrome instalado
- Resolução de tela compatível com a imagem utilizada
- Windows

---

# 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/sergiocalazans/linkedin-autoconnect-bot.git
```

Entre na pasta:

```bash
cd linkedin-autoconnect-bot
```

Crie um ambiente virtual:

### Windows

```bash
python -m venv .venv
```

Ative o ambiente:

```powershell
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# ▶️ Como Executar

Execute:

```bash
python app.py
```

O programa irá:

1. Abrir o Google Chrome
2. Acessar a página configurada
3. Posicionar a barra de rolagem
4. Procurar pela imagem **botao-conectar.png**
5. Clicar quando encontrada
6. Repetir o processo até atingir o número configurado

---

# 🖼️ Captura da Imagem

O reconhecimento é realizado através do arquivo:

```
botao-conectar.png
```

Para obter melhores resultados:

- utilize zoom do navegador em **100%**
- utilize a mesma resolução da captura
- recorte somente o botão
- evite sombras e áreas extras
- utilize o mesmo tema (claro ou escuro)

Quanto mais limpa for a imagem, maior será a precisão do reconhecimento.

---

# 📍 Captura de Coordenadas

O projeto possui um script auxiliar:

```text
capturar-posicao.py
```

Ele pode ser utilizado para descobrir as coordenadas do mouse.

Exemplo de saída:

```
X: 1358
Y: 160
```

Essas coordenadas podem ser utilizadas para alterar esta linha do código:

```python
pyautogui.click(x=1358, y=160)
```

---

# ⚙️ Configuração

No arquivo **app.py** é possível alterar:

## Quantidade de ações

```python
convites = 60
```

---

## Tempo de espera

```python
sleep(5)
```

---

## Pausa entre comandos

```python
pyautogui.PAUSE = 0.5
```

---

## Sensibilidade da imagem

```python
confidence=0.8
```

Valores menores encontram mais imagens, porém aumentam a chance de falsos positivos.

---

# 📋 Fluxo de Funcionamento

```text
Início
   │
   ▼
Abrir Chrome
   │
   ▼
Acessar página
   │
   ▼
Posicionar Scroll
   │
   ▼
Procurar imagem
   │
   ├── Encontrou
   │      │
   │      ▼
   │   Clicar
   │      │
   │      ▼
   │   Incrementar contador
   │      │
   │      ▼
   │   Próxima tentativa
   │
   └── Não encontrou
          │
          ▼
     Encerrar processo
```

---

# ❗ Possíveis Problemas

## O botão não é encontrado

Verifique:

- Zoom do navegador
- Resolução da tela
- Escala do Windows
- Tema claro/escuro
- Qualidade da imagem

---

## O scroll não funciona

Verifique se:

- a página possui foco;
- a barra lateral está ativa;
- a janela do navegador está maximizada.

---

## Erro com confidence

Instale o OpenCV:

```bash
pip install opencv-python
```

---

## Erro ao abrir o navegador

Verifique se o Chrome está instalado e acessível pelo menu Iniciar.

---

# 📄 Licença

Este projeto é disponibilizado exclusivamente para fins educacionais e de estudo sobre automação de interfaces gráficas utilizando Python.

O autor não incentiva nem se responsabiliza pelo uso deste código em desacordo com os Termos de Serviço de plataformas de terceiros.

---

Desenvolvido por: [Sérgio Calazans](https://github.com/sergiocalazans)
