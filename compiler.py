import configuracion 
from cryptography.fernet import Fernet

def do(desencriptable):

    key = configuracion.Fernetkey
    fernet = Fernet(key)
    string_desencriptado = fernet.decrypt(desencriptable).decode("utf-8")

    return string_desencriptado