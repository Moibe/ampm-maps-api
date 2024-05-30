import configuracion
from cryptography.fernet import Fernet

key = configuracion.Fernetkey
fernet = Fernet(key)

string_original = configuracion.conn
print("String original: ", string_original)
string_encriptado = fernet.encrypt(string_original.encode("utf-8"))
string_desencriptado = fernet.decrypt(string_encriptado).decode("utf-8")

print(string_encriptado)