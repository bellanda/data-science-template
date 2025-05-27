import os
import pathlib

import dotenv
from smbclient import register_session

dotenv.load_dotenv()

# Configurações do servidor SMB
server = os.getenv("SMB_SERVER")
share = os.getenv("SMB_SHARE")
username = os.getenv("SMB_USERNAME")
password = os.getenv("SMB_PASSWORD")

# Registrar a sessão com o servidor usando credenciais explícitas
register_session(server, username=username, password=password)

FILE_SERVER_PATH = pathlib.Path(r"\\{}\{}".format(server, share))
