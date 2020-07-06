#!/usr/bin/python
from DBusServer.server import StartServer

try:
    StartServer()
except:
    print("É necessário inciar usando o comando sudo")