from gi.repository import GLib
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop

from DBusServer.emissor import Emissor


class DBusServer(dbus.service.Object):
    listaUsuarios = []
    listaMensagens = []
    loopDBus = None

    def __init__(self, bus_name, object_path, loopDBus):
        dbus.service.Object.__init__(self, bus_name, object_path)
        self.loop = loopDBus
        self.emissor = Emissor(bus_name, '/bus/com/DBusServer/event')

    @dbus.service.method('com.bus.DBusServer.Interface')
    def adicionar_usuario(self, nome_usuario):
        if nome_usuario not in self.listaUsuarios:
            self.listaUsuarios.append(nome_usuario)
            return "Usuário adicionado na conversa"
        else:
            return f'{nome_usuario} já foi adicionado na conversa'

    @dbus.service.method('com.bus.DBusServer.Interface')
    def remover_usuario(self, nome_usuario):
        if nome_usuario in self.listaUsuarios:
            self.listaUsuarios.remove(nome_usuario)
            return "Usuário saiu da conversa"
        else:
            return f'{nome_usuario} não foi entrou na conversa'

    @dbus.service.method('com.bus.DBusServer.Interface')
    def adicionar_mensagem(self, nome_usuario, mensagem):
        self.listaMensagens.append([nome_usuario, mensagem])
        self.emissor.mensagem_recebida([nome_usuario,mensagem])
        return "Mensagem adicionada a conversa"

    @dbus.service.method('com.bus.DBusServer.Interface')
    def encerrar_app(self, nome_usuario):
        self.emissor.encerrar_app(nome_usuario)
        return "Sinal para enverrar app enviado"

    @dbus.service.method('com.bus.DBusServer.Interface')
    def retornarMensagens(self):
        if len(self.listaMensagens) != 0:
            return self.listaMensagens
        else:
            return 'Lista vazia'

    # Parar o loop princial
    @dbus.service.method('com.bus.DBusServer.Interface')
    def stop(self):
        self.loop.quit()
        self.emissor.quit_signal()
        return 'Quit loop'

    # mandar uma exceção pelo DBus
    @dbus.service.method('com.bus.DBusServer.Interface')
    def fail(self):
        """Mandar uma exceção"""
        raise Exception('Erro!')


class StartServer():
    def __init__(self):
        """
         Primeiramente é necessário selecionamos em qual bus iremos rodar,
         podendo ser o session bus que é único para cada usuário,
         usado normalmente para as aplicações abertas se comunicarem ou o system bus que é
         usado para passar informações por todo o sistema, para utilizá-lo é
         necessário ter permissão de root
        """
        self.loopDBus = DBusGMainLoop(set_as_default=True)
        self.loopMain = GLib.MainLoop()
        self.bus = dbus.SystemBus(mainloop=self.loopDBus)
        self.bus_name = dbus.service.BusName('com.bus.DBusServer', bus=self.bus)

        """
         Aqui inicializamos o objeto do nosso objeto de serviço com o nosso nome e o caminho do objeto.
         O caminho deve ser formado na forma de um domínio reverso separado por / com o nome da 
         classe no final, ele é importante pois o cliente usará o caminho definido aqui para chamá-lo
        """
        self.obj = DBusServer(self.bus_name, '/bus/com/DBusServer', loopDBus=self.loopDBus)

        """
        Aqui adicionamos um handler de sinais que ira executar assim que o metodo selecionado emita
        um sinal no DBus, sendo possivel escutar a todos os sinais emitidos no DBus ou apenas um especifico.
        """
        self.bus.add_signal_receiver(self.quit_handler,
                                dbus_interface='com.bus.DBusServer',
                                signal_name='encerrar_servidor')

        self.loopMain.run()

    def quit_handler(self):
        print('Quitting....')
        self.loopMain.quit()
