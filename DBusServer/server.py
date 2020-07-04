from gi.repository import GLib
import dbus
import dbus.service
from dbus.mainloop import NativeMainLoop
from dbus.mainloop.glib import DBusGMainLoop


class Test(dbus.service.Object):
    listaMensagens = []
    loop = None

    def __init__(self, bus_name, object_path):
        dbus.service.Object.__init__(self, bus_name, object_path)

    @dbus.service.method('tld.domain.sub.TestInterface')
    def foo(self):
        return 'Foo'

    # Stop the main loop
    @dbus.service.method('tld.domain.sub.TestInterface')
    def stop(self):
        self.loop.quit()
        return 'Quit loop'


def catchall_handler(*args, **kwargs):
    """Catch all handler.
    Catch and print information about all singals.
    """
    print('---- Caught signal ----')
    print('%s:%s\n' % (kwargs['dbus_interface'], kwargs['member']))

    print('Arguments:')
    for arg in args:
        print('* %s' % str(arg))

    print("\n")


def quit_handler():
    """Signal handler for quitting the receiver."""
    print('Quitting....')
    loop.quit()


loop: NativeMainLoop = DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus(mainloop=loop)
bus_name = dbus.service.BusName('com.bus.busao', bus=bus)

"""
We initialize our service object with our name and object path. Object
path should be in form of a reverse domain dame, delimited by / instead of .
and the Class name as last part.
The object path we set here is of importance for our invoker, since it will to
call it exactly as defined here.
"""
obj = Test(bus_name, '/com/bus/busao')

"""
Attach signal handler.
Signal handlers may be attached in different ways, either by interface keyword
or DBUS interface and a signal name or member keyword.
You can easily gather all information by running the DBUS monitor.
"""
bus.add_signal_receiver(catchall_handler, interface_keyword='dbus_interface', member_keyword='member')
bus.add_signal_receiver(quit_handler, dbus_interface='tld.domain.sub.event', signal_name='quit_signal')
GLib.MainLoop().run()
