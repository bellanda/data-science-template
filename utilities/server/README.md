# Server Utilities

Este módulo contém utilitários para conexão com servidores.

## SMB Client (`smb.py`)

Utilitário para conexão com servidores SMB/CIFS usando credenciais de autenticação.

### Funcionalidades

- Configuração automática de conexão SMB
- Autenticação usando variáveis de ambiente
- Caminho pré-configurado para o servidor de arquivos

### Variáveis de Ambiente Necessárias

```env
SMB_USERNAME=seu_usuario
SMB_PASSWORD=sua_senha
```

### Uso Básico

```python
from utilities.server.smb import FILE_SERVER_PATH

# O caminho do servidor já está configurado e autenticado
print(FILE_SERVER_PATH)  # \\fscatorg01\FileServer
```

### Exemplos Práticos

#### Listar arquivos no servidor

```python
import smbclient
from utilities.server.smb import FILE_SERVER_PATH

# Listar conteúdo de uma pasta
pasta_relatorios = FILE_SERVER_PATH / "relatorios"
arquivos = smbclient.listdir(str(pasta_relatorios))
print("Arquivos encontrados:", arquivos)
```

#### Ler arquivo do servidor

```python
import smbclient
from utilities.server.smb import FILE_SERVER_PATH

# Ler um arquivo de texto
arquivo_path = FILE_SERVER_PATH / "dados" / "config.txt"
with smbclient.open_file(str(arquivo_path), mode="r") as f:
    conteudo = f.read()
    print(conteudo)
```

#### Salvar arquivo no servidor

```python
import smbclient
from utilities.server.smb import FILE_SERVER_PATH

# Salvar um arquivo no servidor
arquivo_destino = FILE_SERVER_PATH / "uploads" / "novo_arquivo.txt"
with smbclient.open_file(str(arquivo_destino), mode="w") as f:
    f.write("Conteúdo do arquivo")

print("Arquivo salvo com sucesso!")
```

#### Copiar arquivo local para o servidor

```python
import smbclient
from utilities.server.smb import FILE_SERVER_PATH

# Copiar arquivo local para o servidor
arquivo_local = "relatorio_local.xlsx"
arquivo_servidor = FILE_SERVER_PATH / "relatorios" / "relatorio_remoto.xlsx"

smbclient.copyfile(arquivo_local, str(arquivo_servidor))
print("Arquivo copiado para o servidor!")
```

#### Verificar se arquivo existe

```python
import smbclient
from utilities.server.smb import FILE_SERVER_PATH

# Verificar se um arquivo existe
arquivo_path = FILE_SERVER_PATH / "dados" / "importante.xlsx"
try:
    stat_info = smbclient.stat(str(arquivo_path))
    print(f"Arquivo existe! Tamanho: {stat_info.st_size} bytes")
except FileNotFoundError:
    print("Arquivo não encontrado")
```

#### Criar diretório no servidor

```python
import smbclient
from utilities.server.smb import FILE_SERVER_PATH

# Criar um novo diretório
nova_pasta = FILE_SERVER_PATH / "nova_pasta"
try:
    smbclient.mkdir(str(nova_pasta))
    print("Diretório criado com sucesso!")
except FileExistsError:
    print("Diretório já existe")
```

### Dependências

- `smbclient`: Cliente SMB para Python
- `python-dotenv`: Carregamento de variáveis de ambiente
