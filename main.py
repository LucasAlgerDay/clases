from BotAmino import *
import time

client = BotAmino("lucasday1234@gmail.com", "animes1234")

@client.command("ayuda")
def help(data):
    data.subClient.send_message(data.chatId, "Hola, estos son mis comandos")

@client.on_member_join_chat()
def bienvenida(data):
    data.subClient.send_message(data.chatId, "Bienvenido al chat")

@client.on_member_leave_chat()
def despedida(data):
    data.subClient.send_message(data.chatId, "Adios")

@client.command()
def chica(data):
    imagen = open("chica.png", "rb")
    data.subClient.send_message(data.chatId, file = imagen, fileType = "image")

@client.command()
def embed(data):
    imagen = open("chica.png", "rb")
    data.subClient.send_message(data.chatId,message = "Sabias que los gatos caen en 4 patas",embedTitle = "Datos random", embedContent = "datos de michis #18", embedImage = imagen, replyTo= data.messageId)

@client.command()
def audios(data):
    audio = open("audio.mp3", "rb")
    data.subClient.send_message(data.chatId, file = audio, fileType = "audio")

@client.command()
def respuestas(data):
    data.subClient.send_message(data.chatId, message= data.message)

@client.answer("Hola")
def saludo(data):
    data.subClient.send_message(data.chatId, message= "Hola", replyTo = data.messageId)


@client.command("everyone")
def menciones(data):
    usuarios = []
    for cantidad in range(0, 1000, 100):
        usuario = data.subClient.get_chat_users(data.chatId, start = cantidad, size = 1000).json
        for user in usuario:
            usuarios.append(user['uid'])
    data.subClient.send_message(data.chatId, message= f"<$@{data.message}$>", mentionUserIds = usuarios)


client.launch(True)
print("ready")

def socketRoot():
	j=0
	while True:
		if j>=180:
			client.close()
			client.run_amino_socket()
			j=0
		j=j+1
		time.sleep(1)
socketRoot()
