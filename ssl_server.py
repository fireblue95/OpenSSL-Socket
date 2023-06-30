import ssl
import socket

class SSL_Server:
    def __init__(self):
        self.server_addr = ("127.0.0.1", 8888)

        self.ssl_server_crt = 'cert/server.crt'
        self.ssl_server_key = 'cert/server.key'

        self.ssl_client_crts = ['cert/client.crt', 'cert/client2.crt']

        self.max_connection = 5

    def run(self) -> None:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(self.server_addr)
        server_socket.listen(self.max_connection)

        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.verify_mode = ssl.CERT_REQUIRED

        context.load_cert_chain(certfile=self.ssl_server_crt, keyfile=self.ssl_server_key)

        for client_crt in self.ssl_client_crts:
            context.load_verify_locations(client_crt)

        context.verify_mode = ssl.CERT_REQUIRED
        print('Server started.')
        print('Server IP:', self.server_addr)

        while True:
            try:
                client_socket, addr = server_socket.accept()
                secure_socket = context.wrap_socket(client_socket, server_side=True)

                secure_socket.sendall(f'Hello client! your ip address is {addr}'.encode())
                print('=' * 50)
                print('Send the msg to client', addr)

                # Get client's certification.
                client_cert = secure_socket.getpeercert()

                # Get info of client's certification.
                subject = dict(item[0] for item in client_cert['subject'])

                print("\n=== Client's info ===")
                print("Country Name:", subject.get('countryName'))
                print("Organization Name", subject.get('organizationName'))
                print("Common Name", subject.get('commonName'))
                
                message = secure_socket.recv(1024)
                print('Recv message:', message.decode())

                secure_socket.close()

                print('=' * 50)

            except Exception as e:
                print(e)

if __name__ == "__main__":
    app = SSL_Server()
    app.run()
