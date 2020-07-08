import threading
import tkinter
import tkinter as tk
import dbus
from _dbus_glib_bindings import DBusGMainLoop
from gi.repository import GLib
from Interface.scrollable import Scrollable
from PIL import Image, ImageTk
import os
from tkinter.simpledialog import askstring

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class initInterfaceApp:
    def encerrar_app(self, usuarioEncerrando):
        if usuarioEncerrando == nomeUsuario:
            self.loopMain.quit()

    def __init__(self):
        self.app = App(interfaceApp= self)
        self.nomeUsuario = ""
        self.loopDbus = DBusGMainLoop(set_as_default=True)
        self.loopMain = GLib.MainLoop()
        self.bus = dbus.SystemBus(mainloop=self.loopDbus)
        try:
            self.objServidor = self.bus.get_object('com.bus.DBusServer', '/bus/com/DBusServer')
            self.bus.add_signal_receiver(self.app.ReceivedMensagem, dbus_interface='com.bus.DBusServer.event',
                                         signal_name='mensagem_recebida')
            self.bus.add_signal_receiver(self.encerrar_app,
                                         dbus_interface='com.bus.DBusServer.event',
                                         signal_name='encerrar_app')
            self.loopMain.run()
        except dbus.exceptions.DBusException:
            print("Servidor de mensagens não está rodando")
            self.app.callback()


class App(threading.Thread, initInterfaceApp):

    def __init__(self, interfaceApp):
        self.interfaceApp = interfaceApp
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.destroy()
        try:
            print(self.interfaceApp.objServidor.remover_usuario(nomeUsuario))
            self.interfaceApp.objServidor.encerrar_app(nomeUsuario)
        except:
            print("Não foi possível comunicar com o servidor")
            self.interfaceApp.loopMain.quit()

    def AddMensagemBotao(self):
        a = tk.Label(self.scrollable_body, text=self.processText(f"{nomeUsuario}:\n{self.entry1.get()}"),
                     justify='right', anchor='e',
                     bg='white')
        a.pack(fill=tk.X, expand=True)
        self.scrollable_body.update()
        self.root.update()
        self.interfaceApp.objServidor.adicionar_mensagem(nomeUsuario, self.entry1.get())
        self.entry1.delete(0, tkinter.END)

    def AddMensagem(self, mensagem):
        a = tk.Label(self.scrollable_body, text=self.processText(f"{nomeUsuario}:\n{mensagem}"),
                     justify='right', anchor='e',
                     bg='white')
        a.pack(fill=tk.X, expand=True)
        self.scrollable_body.update()
        self.root.update()

    def ReceivedMensagem(self, mensagem):
        if mensagem[0] != nomeUsuario:
            a = tk.Label(self.scrollable_body, text=self.processText(f"{mensagem[0]}:\n{mensagem[1]}"), justify='left',
                         anchor='w',
                         bg='#CCCCCC')
            a.pack(fill=tk.X, expand=True)
            self.scrollable_body.update()
            self.root.update()

    def processText(self, texto):
        return '\n'.join(texto[i:i + 35] for i in range(0, len(texto), 35))

    def configure_app(self):
        global nomeUsuario
        self.root.withdraw()
        retorno = 'Insira seu nome'
        while retorno != "Usuário adicionado na conversa":
            nomeUsuario = askstring(retorno, 'Insira seu nome', initialvalue='')
            retorno = self.interfaceApp.objServidor.adicionar_usuario(nomeUsuario)

        mensagensAnteriories = self.interfaceApp.objServidor.retornarMensagens()
        if mensagensAnteriories != 'Lista vazia':
            for value in mensagensAnteriories:
                if value[0] == nomeUsuario:
                    self.AddMensagem(value[1])
                else:
                    self.ReceivedMensagem([value[0], value[1]])

        self.root.iconify()
        return retorno
    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.body = tk.Frame(self.root)
        self.body.pack(fill=tk.X)

        self.img = Image.open("bg.jpg")
        self.imgTK = ImageTk.PhotoImage(self.img)

        self.canvas = tk.Canvas(self.root, height=500)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imgTK)

        self.canvas.pack()

        self.scrollable_body = Scrollable(self.body)

        self.entry1 = tk.Entry(self.canvas, width=100)
        self.entry1.pack(side='left', fill=tk.X, expand=True, padx=15, pady=15)

        self.button1 = tk.Button(
            self.canvas,
            text='Enviar',
            command=self.AddMensagemBotao,
            bg='green',
            height=1,
            fg='white',
            font=('helvetica', 9, 'bold')
        )
        self.button1.pack(side='right', padx=15)
        self.configure_app()
        self.root.title("Trava Zap")
        self.root.resizable(0, 0)
        self.root.mainloop()