import sys
import socket
import os
import time
def open_file(filename):
	with open(filename, mode="rb") as file:
		file_bytes = file.read()
		file_size=os.stat(filename).st_size
		return file_bytes,file_size

def socket_to_screen(socket, sock_addr):
#
	# Reads data from a passed socket and prints it on screen.

	# Returns either when a newline character is found in the stream or the connection is closed.
    #     The return value is the total number of bytes received through the socket.
	# The second argument is prepended to the printed data to indicate the sender.
	# """
	print(sock_addr + ": ", end="", flush=True) # Use end="" to avoid adding a newline after the communicating partner's info, flush=True to force-print the info

	data = bytearray(1)
	bytes_read = 0

	"""
	 Loop for as long as data is received (0-length data means the connection was closed by
	 the client), and newline is not in the data (newline means the complete input from the
	 other side was processed, as the assumption is that the client will send one line at
	 a time).
	"""
	while len(data) > 0 and "\n" not in data.decode():
		"""
		 Read up to 4096 bytes at a time; remember, TCP will return as much as there is
		 available to be delivered to the application, up to the user-defined maximum,
		 so it could as well be only a handful of bytes. This is the reason why we do
		 this in a loop; there is no guarantee that the line sent by the other side
		 will be delivered in one recv() call.
		"""
		data = socket.recv(2048)

		print(data.decode(), end="") # Use end="" to avoid adding a newline per print() call
		bytes_read += len(data)
	return bytes_read

def keyboard_to_socket(socket):
	"""Reads data from keyboard and sends it to the passed socket.
	
	Returns number of bytes sent, or 0 to indicate the user entered "EXIT"
	"""
	print("  You: ", end="", flush=True) # Use end="" to avoid adding a newline after the prompt, flush=True to force-print the prompt

	# Read a full line from the keyboard. The returned string will include the terminating newline character.
	
	# Send the whole line through the socket; remember, TCP provides no guarantee that it will be delivered in one go.
	return 1


def recv_all(socket,size):
	msg=[]
	msglist=[]
	iterator=0
	size=int(size)
	while 0<size:
		if size>2048:
			if iterator%100==0:
				print(iterator)
			size-=2048
			iterator+=1
			msg.append(socket.recv(2048))
		else:
			msg.append(socket.recv(size))
			size=0
	lambda msg: [i for sublist in msg for i in sublist]
	msg=bytes(msg)
	return msg

def get_header_size(header):
	header_size=len(bytes(header,"utf-8"))
	return header_size

def send_header_size(socket,header_size):
	return socket.sendall(bytes(str(header_size),"utf-8"))

def recv_header_size(socket):
	incoming=socket.recv(24)
	header_size=int(incoming.decode())
	return header_size
# def send_header(command,filename,size):
# 	header=str(request)+"\0"+str(filename)+"\0"+str(size)
# 	get_header_size(header)
# 	socket.
def existingfile(filename):
	try:
		f = open(filename)
		f.close()
	except FileNotFoundError:
		print('File does not exist')
		return False
	return FileExistsError("Cannot create file that already exists")
def put_send(socket,filename):
	file,file_size=open_file(filename)
	header=f"put\0{filename}\0{file_size}"#+"\0"
	header_size=get_header_size(header)
	print(header,bytes(header,"utf-8"),header_size)
	#import pdb; pdb.set_trace()
	print("Errors while sending header size:",send_header_size(socket,header_size))
	print("Errors while sending header:",socket.sendall(bytes(header,"utf-8")))
	print("Errors while sending file:",socket.sendall(file))
	return f"upload finished"

def recv_start(socket):
	header_size=recv_header_size(socket)
	print("Reciever header's size")
	header=socket.recv(header_size).decode("utf-8")
	print("Recieved header")
	if header=="EXIT\n":
		print("User requested Exit")
		IsExit=True
		return IsExit
	header=header.split("\0")
	command = header[0]
	print(f"{command} command was requested")
	if command=="put":
		return recv_put(header[1],header[2],socket)
	elif command=="get":
		return send_get(header[1],header[2],socket)
	elif command=="list":
		return send_listing(socket)
	else: return SyntaxError("No such command found")

def recv_put(filename,file_size,socket):
	file=recv_all(socket,file_size)
	if existingfile(filename)==False:
		with open(filename,mode="xb") as f:
			f.write(file)
			print(f"{filename} has been uploaded(filesize={file_size})")
			return "DONE"
	else:
		print(FileExistsError)

def send_get(filename,file_size,socket):
	#import pdb; pdb.set_trace()
	file,file_size=open_file(filename)
	header=bytes(str(file_size),"utf-8")
	print("Errors while sending file:",socket.sendall(header))
	print("Errors while sending file:",socket.sendall(file))
	return "DONE"

def recv_get(filename,socket):
	header=f"get\0{filename}\0"#+"\0"
	header_size=get_header_size(header)
	print(header,bytes(header,"utf-8"),header_size)
	#import pdb; pdb.set_trace()
	print("Errors while sending header size:",send_header_size(socket,header_size))
	print("Errors while sending header:",socket.sendall(bytes(header,"utf-8")))
	file_size=int(socket.recv(24).decode())
	file=recv_all(socket,file_size)
	if existingfile(filename)==False:
		with open(filename,mode="xb") as f:
			f.write(file)
			print(f"{filename} has been downloaded(filesize={file_size}")
	



def send_listing(socket):
	print("HERE")
	listing=os.listdir(os.path.abspath("lab3-server.py")[:-len("lab3-server.py")])
	print(listing)
	listing_bin=str(listing).encode('utf-8')
	listing_size=len(listing_bin)
	socket.sendall(bytes(str(listing_size),"utf-8"))
	socket.sendall(listing_bin)
	return "DONE"

def recv_listing(socket):
	header="list\0"#+"\0"
	header_size=5
	print("Errors while sending header size:",send_header_size(socket,header_size))
	print("Errors while sending header:",socket.sendall(bytes(header,"utf-8")))
	listing_size_byte=socket.recv(24)
	print("listing size got")
	listing_size=int(listing_size_byte.decode())
	print(listing_size)
	listing=recv_all(socket,listing_size)
	print(f"Server's listings are the following: \n {listing}")


	
