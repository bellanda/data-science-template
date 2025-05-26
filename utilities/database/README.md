# Database Utilities

Este módulo contém utilitários para conexão e operações com bancos de dados.

## Oracle Database (`oracle.py`)

Utilitário para conexão com banco de dados Oracle usando SQLAlchemy e oracledb.

### Funcionalidades

- Conexão automática com Oracle Database
- Pool de conexões configurado
- Suporte a Oracle Client (modo Thick) e modo Thin
- Logging detalhado de operações
- Trace Oracle opcional para debugging
- Configuração via variáveis de ambiente

### Variáveis de Ambiente Necessárias

```env
ORACLE_USERNAME=seu_usuario
ORACLE_PASSWORD=sua_senha
ORACLE_HOST=localhost
ORACLE_PORT=1521
ORACLE_SERVICE_NAME=XEPDB1
CLIENT_PATH=/opt/oracle/instantclient_21_1  # Opcional
ORACLE_ENABLE_SQL_ALCHEMY_LOG=false  # Opcional
ORACLE_ENABLE_TRACE=false  # Opcional
```

### Uso

```python
from utilities.database.oracle import engine
import pandas as pd

# Executar query e retornar DataFrame
df = pd.read_sql("SELECT * FROM sua_tabela", engine)

# Usar com SQLAlchemy
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM sua_tabela"))
    count = result.scalar()
    print(f"Total de registros: {count}")
```

### Recursos Avançados

#### Trace Oracle

Para habilitar o trace Oracle (útil para debugging de performance):

```env
ORACLE_ENABLE_TRACE=true
```

#### Logging SQLAlchemy

Para ver todas as queries SQL executadas:

```env
ORACLE_ENABLE_SQL_ALCHEMY_LOG=true
```

### Dependências

- `oracledb`: Driver oficial Oracle para Python
- `sqlalchemy`: ORM e toolkit SQL
- `python-dotenv`: Carregamento de variáveis de ambiente
- `pandas`: Para operações com DataFrames (opcional)
