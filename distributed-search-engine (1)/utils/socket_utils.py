# TCP/IP socket helper utilities
import socket

def create_server(host='localhost', port=9090):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    return s

def create_client(host='localhost', port=9090):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s
