from pygame import *
import socket
import json
from threading import Thread
init()

window = display.set_mode((800, 600))
display.set_caption("ping-pong")
fps = time.Clock()

#Підкл до сервера
def connect_to_server():
    while True:
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(("localhost", 12345))  
            id = int(client.recv(24).decode())
            buffer = ""
            game_state = {}
            return id, game_state, buffer, client
        except:
            pass


def receive():
    global buffer, game_state, game_over
    while not game_over:
        try:
            data = client.recv(1024).decode()
            buffer += data
            while "\n" in buffer:
                packet, buffer = buffer.split("\n", 1)
                if packet.strip():
                    game_state = json.loads(packet)
        except:
            game_state["winner"] = -1



id, game_state, buffer, client = connect_to_server()
game = True
while game:
    for ev in event.get():
        if ev.type == QUIT:
            game = False
    display.flip()
    fps.tick(60)