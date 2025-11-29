import socket
import json
from threading import Thread
import time
import random

WIDTH, HEIGHT = 800, 600
BALL_SPEED = 4
PADDLE_SPEED = 7

class gameserver:
    def __init__(self, host="localhost", port = "12345"):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(2)
        print("Сервер підключено")
        self.client = {0: None, 1: None}
        self.connected = {0: False, 1: False}


    def run(self):
        while True:
            self.accept_players()
            self.reset_game_state()
            Thread(target = self.ball, daemon=True).start()
            while not self.game_over and all(self.connected.values()):
                time.sleep(0.1)

            print("Гравець переміг")
            time.sleep(5)

            for id [0,1]:
            try:
                self.clients[id].close
            except:
                pass
            self.clients[id] = None
            self.connected[id] = False

gameserver().run()