# Projeto-D-Bus-SOII
Este projeto foi feito com o intuito de criar um exemplo de funcionamento de um aplicativo utilizando o D-Bus para  a aula de Sistemas Operacionais II da faculdade Fatec de Americana lecionada pelo Professor Rossano Pablo Pinto.
 
O primeiro exemplo criado pelo nosso grupo foi um aplicativo de console que utiliza a implementação da Interface MPRIS D-Bus, cujo objetivo é padronizar a implementação de uma interface de comunicação pelo D-Bus para aplicativos de reprodução de música.

Nosso segundo exemplo é um aplicativo que possibilita que usuários que estão conectados em uma mesma máquina, consigam mandar mensagens entre si pelo D-Bus. Para implementá-lo foi criado um servidor que centraliza as mensagens enviadas pelos usuários em um só local através de um objeto de serviço que fica instanciado no SystemBus do sistema, um emissor que envia sinais pelo D-Bus que podem ser assinados pelo cliente para chamar uma função após um evento acontecer e um cliente gráfico. 

A comunicação funciona da seguinte maneira:

<ul>
O servidor ao ser instanciado no D-Bus deixa expostos algumas funções para que o cliente ao recuperar sua instancia possa chamar, por exemplo a função que salva a mensagem enviada pelo cliente em uma lista que contém as mensagens enviadas durante a sessão, e emite um sinal pelo emissor que avisa todos os usuários que estão observando aquele evento de que há uma nova mensagem a ser exibida.
</ul>
Na página de releases <a href="https://github.com/henriquealmeida39/Projeto-D-Bus-SOII/releases">https://github.com/henriquealmeida39/Projeto-D-Bus-SOII/releases</a> do projeto é possível baixar executáveis do projeto que não necessitam a instalação das dependências usadas, mas é possivel compilar seus próprios utilizando o Pyinstaller por exemplo.

# Dificuldades econtradas durante o desenvolvimento
Durante o desenvolvimento do projeto nosso grupo encontrou algumas dificuldades para implementar o wrapper padrão do dbus com o TKinter pois o mainloop do Tkinter não era aceito pelo dbus, então, foi necessário criar a aplicação em uma thread diferente do listener de eventos para conseguirmos rodar os dois em conjunto.

Tivemos que aprender também como que um aplicativo que desejasse usar o SystemBus deveria expressar as permissões que o aplicativo teria pra poder ser instanciado, sua localidade no Ubuntu que foi a distribuição que realizamos o teste fica em /usr/share/dbus-1/system.d, podendo ser diferente depenendo do local escolhido por outras distribuições pelo o que vimos.      

## Licença

    Copyright 2020 Henrique Barros de Almeida, Guilherme Moriggi de Souza, Lucas Abrahão, Daniel Dinardi Francisco e Wilson José Caetano Junior
    
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