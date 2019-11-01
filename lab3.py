import sys
import socket

def open_file(filename)
	with open(filename, mode="rb") as file:
		file_bytes = file.read()
		file_size=len(file)
		return file_bytes,file_size
def send_file(socket, filename):
	with open(filename, mode="rb") as file:
		file_bytes = file.read(4096)
		while file_bytes:
			socket.send(file_bytes)
			file_bytes = file.read(4096)


def get_header(socket, sock_addr):
	print(sock_addr + ": ", end="", flush=True) # Use end="" to avoid adding a newline after the communicating partner's info, flush=True to force-print the info

	data = bytearray(1)

	"""
	 Loop for as long as data is received (0-length data means the connection was closed by
	 the client), and newline is not in the data (newline means the complete input from the
	 other side was processed, as the assumption is that the client will send one line at
	 a time).
	"""
	header=str(request)+"\0"+str(filename)+"\0"+str(size)
	header_size=len(bytes(header))
	socket.sendall(header_size)
	socket.sendall(bytes(header))
	data = socket.recv(4096)
	if len(data) > 0 and "\n" not in data.decode():
		"""
		 Read up to 4096 bytes at a time; remember, TCP will return as much as there is
		 available to be delivered to the application, up to the user-defined maximum,
		 so it could as well be only a handful of bytes. This is the reason why we do
		 this in a loop; there is no guarantee that the line sent by the other side
		 will be delivered in one recv() call.
		"""
		return data
	else return 0
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
		data = socket.recv(4096)

		print(data.decode(), end="") # Use end="" to avoid adding a newline per print() call
		bytes_read += len(data)
	return bytes_read

def keyboard_to_socket(socket):
	"""Reads data from keyboard and sends it to the passed socket.
	
	Returns number of bytes sent, or 0 to indicate the user entered "EXIT"
	"""
	print("  You: ", end="", flush=True) # Use end="" to avoid adding a newline after the prompt, flush=True to force-print the prompt

	# Read a full line from the keyboard. The returned string will include the terminating newline character.
	user_input = sys.stdin.readline()
	if user_input == "EXIT\n": # The user requested that the communication is terminated.
		return 0

	# Send the whole line through the socket; remember, TCP provides no guarantee that it will be delivered in one go.
	#bytes_sent = socket.sendall(str.encode(user_input))
	return bytes_sent


def recv_all(size):
	msg=0
	while 0<size:
		if size>4096:
			size-=4096
			msg+=socket.recv(4096)
		else:
			msg+=socket.recv(size)
			size=0
	return size

def get_header_size(header):
	header_size=len(bytes(header))
	return header_size
def send_header_size(cli_sock,header_size):
	return cli_sock.sendall(header_size)

def recv_header_size():
	header_size=int(recv(24),2)
	return header_size
def send_header(command,filename,size):
	header=str(request)+"\0"+str(filename)+"\0"+str(size)
	get_header_size(header)
	socket.
def existingfile(filename):
	try:
		f = open(filename)
		f.close()
	except FileNotFoundError:
		print('File does not exist')
		return False
	return FileExistsError("Cannot create file as file already exists")
def put_send(cli_sock,filename):
	file,file_size=open_file(filename)
	header="put"+"\0"+"filename"+"\0"+"file_size" #+"\0"
	header_size=get_header_size(header)
	print("Errors while sending header size:",send_header_size(header_size))
	print("Errors while sending file:",cli_sock.sendall(file))

def recv_start(cli_sock):
	commandsdict={"put":recv_put(),
			"get":recv_get(),
			"list":recv_list()}
	header_size=recv_header_size()
	header=recv(header_size)
	header=header.split("\0")
	if header[0] in commandsdict:
		commandsdict[header[0]]
	else raise SyntaxError("No such command found")
	
	filename=header
	with open(filename,mode="xb") as f:


def recv_file(socket, filename):
	with open(filename, mode='xb') as file:
		data = socket.recv(4096)
		while data:
			file.write(data)
			data = socket.recv(4096)


	
