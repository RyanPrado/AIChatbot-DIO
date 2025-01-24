# AIChatbot-DIO

## 🌐 Sobre

Neste projeto teremos a resolução de dois desafios de codigo propostos no bootcamp BairesDev - Machine Learning Practitioner da [DIO](web.dio.me/), os desafios de codigo envolvidos são "Criando um Sistema de Recomendação por Imagens Digitais" e "
Criando um sistema de assistência virtual do zero"

## 🔰 Propostas dos desafios
#### • Criando um Sistema de Recomendação por Imagens Digitais
Este desafio tem como proposta a leitura de uma imagem e trazer oque ela representa (classificação) em texto, este texto poderia ser utilizado para uma recomendação para o úsuario, exemplo, imagine que o úsuario está procurando um relógio, ele poderia enviar uma foto do mesmo, e baseado nisto a nossa base de dados teria uma massiva gama de opções (bem classificadas), para que relogios semelhantes pudessem ser recomendados
#### • Criando um sistema de assistência virtual do zero
Este desfio tem como proposta o desenvolvimento de uma "assistente" simples, semelhante a alexia, seu desenvolvimento é bem simples, deve ser capaz de emitir VOZ (text-to-speech) e também de ouvir e interpretar (speech-to-text), e baseado nisto deve ter alguma funcionalidade aplicada.

## 💻 Como instalar

### Windows
Realizaremos a instalação através do [Anaconda](https://www.anaconda.com/), caso tenha familiaridade com Python e instalação de dependências, pode utilizar outro gerenciador.

#### 1º - Faça o clone do repositório através com comando: (Necessário [Git](https://git-scm.com/downloads))
```bash
git clone https://github.com/
cd aichatbot-dio
```
#### 2º - Instalando o FLAC:
* Faça o [download do FLAC](https://xiph.org/flac/download.html)
* Extraia do `zip` a versão do seu sistema operacional, coloque em uma pasta (recomendação: `%USERPROFILE%/.flac`)
* Copie e clone o `flac.exe` e renomeie a cópia para apenas `flac` (exato sem `.exe`)
* Adicione o diretório nas variaveis de ambiente [[tutorial]](https://answers.microsoft.com/pt-br/windows/forum/all/como-ter-acesso-%C3%A0s-vari%C3%A1veis-do-sistema/418ff7c5-f671-4633-a516-f84ce1cd0028)
#### 3º - Criando um ambiente isolado com o anaconda:
```bash
conda env create -f environment.yml #Criando um ambiente isolado
conda activate AIChatBot-DIO #Ativando o ambiente isolado
```
#### 4º - Iniciando a aplicação
```bash
python -m aichatbot
```

## 🤖 Como utilizar
Como a proposta da aplicação é simples, sua utilização também é, será necessário um microfone disponivel para que possa ser feito a comunicação com a Assistente, você poderá utilizar a lingua portuguesa para sua comunicação, o comando disponivel é de identificação de imagem, então basta dizer algo que contenha as palavras `identificar` e `imagem`, na mesma frase que uma caixa de dialogo aparecerá pedindo para você inserir o endereço da imagem, exemplos de frases são:

* Identifique está imagem para mim
* Você pode indetificar oque tem nesta imagem?
* Identifique oque há na imagem

Basta utilizar na mesma frase as duas palavras chaves que a Assistente irá auxilia-lo, posterior a isto um dos itens identificados será mencionado como o sugerido a busca

## 🤩 Conclusão
Por mais que o desafio tenha seu objetivo simples, apartir deste gancho somos capazes de visualizar coisas complexas que podem ser geradas apartir deste ponto de partida, muitas bibliotecas e frameworks potentes são utilizadas aqui, mesmo em um projeto tão "simples".

## 📚 Bibliotecas & Frameworks de Destaque utilizados(as)

* [PyTorch](https://pytorch.org/)
* [NumPy](https://numpy.org/)
* [SciPy](https://scipy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Pillow](https://pillow.readthedocs.io/en/stable/)
* [gTTS](https://gtts.readthedocs.io/en/latest/)
* [OpenCV](https://opencv.org/)
* [PlaySound](https://github.com/TaylorSMarks/playsound)
* [Ultralytics(YOLO)](https://pjreddie.com/darknet/yolo/)