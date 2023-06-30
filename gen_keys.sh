CERT_DIR=cert

rm -rf ${CERT_DIR}

mkdir ${CERT_DIR}

cd ${CERT_DIR}

openssl req -x509 -newkey rsa:2048 -nodes -keyout server.key -out server.crt -days 365

openssl req -x509 -newkey rsa:2048 -nodes -keyout client.key -out client.crt -days 365

openssl req -x509 -newkey rsa:2048 -nodes -keyout client2.key -out client2.crt -days 365