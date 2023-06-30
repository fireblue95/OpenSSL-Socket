# OpenSSL-Socket

Using OpenSSL with Socket to build the security communication.

Support using multi Client's CRT.

Usage
===

Generate the keys
---

* Notice: The Common Name of certification of the server needs to match the variable `self.server_hostname` in `ssl_client.py` line 16
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