import dbus
import dbus.service
import dbus.glib


class Emissor(dbus.service.Object):
    """Objeto de serviço de emissão no DBus."""

    def __init__(self, bus_name, object_path):
        """Inicializar o objeto de serviço de emissão no DBus"""
        dbus.service.Object.__init__(self, bus_name, object_path)

    @dbus.service.signal('com.bus.DBusServer.event')
    def mensagem_recebida(self, mensagem):
        print(f'Nova mensagem de {mensagem[0]}:\n{mensagem[1]}')

    @dbus.service.signal('com.bus.DBusServer.event')
    def quit_signal(self):
        """Emite um sinal de desligamento."""
        print('Emitiu um sinal de desligamento')

    @dbus.service.signal('com.bus.DBusServer.event')
    def encerrar_app(self, nome_usuario):
        """Emite um sinal de desligamento."""
        print(f'{nome_usuario} emitiu um sinal de desligamento')
