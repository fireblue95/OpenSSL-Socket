import ssl
import socket

class SSL_Client:
    def __init__(self, check_hostname: bool = True):
        self.server_addr = ("127.0.0.1", 8888)

        self.ssl_client_crt = 'cert/client.crt'
        self.ssl_client_key = 'cert/client.key'

        self.ssl_server_crt = 'cert/server.crt'

        self.check_hostname = check_hostname
        if self.check_hostname:
            # Need to match the Common Name of the certification of the server
            self.server_hostname = 'server'

    def run(self) -> None:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect(self.server_addr)

        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        
        context.load_cert_chain(certfile=self.ssl_client_crt, keyfile=self.ssl_client_key)
        context.load_verify_locations(cafile=self.ssl_server_crt)
        
        context.verify_mode = ssl.CERT_REQUIRED
        
        if self.check_hostname:
            self.secure_socket = context.wrap_socket(server_socket, server_hostname=self.server_hostname)
        else:
            context.check_hostname = False
            self.secure_socket = context.wrap_socket(server_socket)
        print(f'Connect to server {self.server_addr} successfully.')


        message = self.secure_socket.recv(1024)
        print('Recv message from server:', message.decode())

        self.secure_socket.send('Hello server.'.encode())

        self.secure_socket.close()


if __name__ == "__main__":
    app = SSL_Client()
    app.run()
