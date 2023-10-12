import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

class GUI:
	def __init__(self):
		
		self.window = Tk()
		self.window.withdraw()
		
		self.login = Toplevel()
		self.login.title("Login")
		self.login.resizable(width = False,
							height = False)
		self.login.configure(width = 400,
							height = 300,
							bg="#CD5C08")
		self.pls = Label(self.login,
					text = "Please login to continue",
					justify = CENTER,
					font = "Helvetica 14 bold",
					bg="#CD5C08",
					fg="#ffffff")
		
		self.pls.place(relheight = 0.15,
					relx = 0.2,
					rely = 0.07)
		self.label_name = Label(self.login,
							text = "Name: ",
							font = "Helvetica 12",
							bg="#CD5C08",
							fg="#ffffff"
							)
		
		self.label_name.place(relheight = 0.2,
							relx = 0.1,
							rely = 0.2)
		
		self.entry_name = Entry(self.login,
							font = "Helvetica 14",
							bg = "#F5E8B7",
							fg = "#444444",
							)
		
		self.entry_name.place(relwidth = 0.4,
							relheight = 0.12,
							relx = 0.35,
							rely = 0.2)
		
		self.entry_name.focus()

		self.go = Button(self.login,
						text = "CONTINUE",
						font = "Helvetica 16",
						bg="#FFA259",
						fg="#333333",
						command = lambda: self.go_ahead(self.entry_name.get()))
		
		self.go.place(relx = 0.35,
					rely = 0.55)
		self.window.mainloop()

	def go_ahead(self, name):
		self.login.destroy()
		self.layout(name)
		rcv = Thread(target=self.receive)
		rcv.start()

	def layout(self,name):
		
		self.name = name
		self.window.deiconify()
		self.window.title("CHATROOM")
		self.window.resizable(width = False,
							height = False)
		self.window.configure(width = 470,
							height = 550,
							bg = "#CD5C08")
		self.label_head = Label(self.window,
							bg = "#CD5C08",
							fg = "#EAECEE",
							text = self.name ,
							font = "Helvetica 13 bold",
							pady = 5)
		
		self.label_head.place(relwidth = 1)
		
		self.text_comm = Text(self.window,
							width = 20,
							height = 2,
							bg = "#F5E8B7",
							fg = "#444444",
							font = "Helvetica 14",
							padx = 5,
							pady = 5)
		
		self.text_comm.place(relheight = 0.745,
							relwidth = 1,
							rely = 0.08)
		
		self.label_bottom = Label(self.window,
								bg = "#CD5C08",
								height = 80)
		
		self.label_bottom.place(relwidth = 1,
							rely = 0.825)
		
		self.entry_msg = Entry(self.label_bottom,
							bg = "#F5E8B7",
							fg = "#444444",
							font = "Helvetica 13")
		
		self.entry_msg.place(relwidth = 0.74,
							relheight = 0.06,
							rely = 0.008,
							relx = 0.011)
		
		self.entry_msg.focus()
		
		self.buttonMsg = Button(self.label_bottom,
								text = "Send",
								font = "Helvetica 10 bold",
								width = 20,
								bg = "#FFA259",
								command = lambda: self.sendButton(self.entry_msg.get()))
		
		self.buttonMsg.place(relx = 0.77,
							rely = 0.008,
							relheight = 0.06,
							relwidth = 0.22)
		
		self.text_comm.config(cursor = "arrow")
		self.text_comm.config(state = DISABLED)
		
		# Create scrollbar on self.text_comm

        # Place scrollbar on right side and give it size accordingly
		
		# Configure the scrollbar to move y axis
		

	def sendButton(self, msg):
		self.text_comm.config(state = DISABLED)
		self.msg=msg
		self.entry_msg.delete(0, END)
		snd= Thread(target = self.write)
		snd.start()

    
	def show_message(self, message):
        # Configure text_comm state to NORMAL
		
        # Use insert method on text_comm to add the message
		
        # Configure text_comm state to DISABLED
		
        # Use see(END) method to scroll to end of the text_comm

		pass

	def receive(self):
		while True:
			try:
				message = client.recv(2048).decode('utf-8')
				if message == 'NICKNAME':
					client.send(self.name.encode('utf-8'))
				else:
					self.show_message(message)
			except:
				print("An error occured!")
				client.close()
				break

	def write(self):
		self.text_comm.config(state=DISABLED)
		while True:
			message = (f"{self.name}: {self.msg}")
			client.send(message.encode('utf-8'))
			self.show_message(message)	
			break

g = GUI()
