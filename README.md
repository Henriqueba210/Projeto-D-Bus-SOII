# Projeto-D-Bus-SOII
Este projeto foi feito com o intuito de criar um exemplo de funcionamento de um aplicativo utilizando o D-Bus para  a aula de Sistemas Operacionais II da faculdade Fatec de Americana lecionada pelo professor Rossano Pablo Pinto.
<br>O primeiro exemplo criado pelo nosso grupo foi um aplicativo de console que utiliza a implementação da Interface MPRIS D-Bus, cujo objetivo é padronizar a implementação de uma interface de comunicação pelo D-Bus para aplicativos de reprodução de música.
<br><br>Nosso segundo exemplo é um aplicativo que possibilita que usuários que estão conectados em uma mesma máquina, consigam mandar mensagens entre si pelo D-Bus. Para implementá-lo foi criado um servidor que centraliza as mensagens enviadas pelos usuários em um só local através de um objeto de serviço que fica instanciado no SystemBus do sistema, um emissor que envia sinais pelo D-Bus que podem ser assinados pelo cliente para chamar uma função após um evento acontecer e um cliente gráfico. 
<br>A comunicação funciona da seguinte maneira:<br>
<ul>
O servidor ao ser instanciado no D-Bus deixa expostos algumas funções para que o cliente ao recuperar sua instancia possa chamar, por exemplo a função que salva a mensagem enviada pelo cliente em uma lista que contém as mensagens enviadas durante a sessão, e emite um sinal pelo emissor que avisa todos os usuários que estão obeservando aquele evento de que há uma nova mensagem a ser exibida.
</ul>
Na página de releases <a href="https://github.com/henriquealmeida39/Projeto-D-Bus-SOII/releases">https://github.com/henriquealmeida39/Projeto-D-Bus-SOII/releases</a> do projeto é possível baixar executáveis do projeto que não necssitam a instalação das dependencias usadas, mas é possivel compilar seus próprios utilizando o Pyinstaller por exemplo.
      

## Licença

    Copyright 2020 Henrique Barros de Almeida, Guilherme Moriggi de Souza, Lucas Abrahão, Daniel Franciso Dinardi e Wilson José Caetano Junior
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
