# OpenSSL-Socket

This repository utilizes OpenSSL and Socket to establish secure communication.

Support for using multiple Client's CRT.

Usage
===

Generate the keys
---

* Notice: The Common Name (CN) of the server's certificate must match the variable `self.server_hostname` in `ssl_client.py` on line 16.
```bash
bash gen_keys.sh
```

Run the Server
---

```bash
python3 ssl_server.sh
```

Run the Client
---

```bash
python3 ssl_client.sh
```