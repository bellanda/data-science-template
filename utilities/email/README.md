# Email Utilities

Este módulo contém utilitários para envio de emails via SMTP.

## SMTP Client (`smtp_client.py`)

Cliente SMTP completo para envio de emails com suporte a anexos, CC, BCC e conteúdo HTML.

### Funcionalidades

- Envio de emails via SMTP com autenticação TLS
- Suporte a anexos múltiplos
- Suporte a CC (cópia) e BCC (cópia oculta)
- Conteúdo HTML nos emails
- Detecção automática de tipos MIME para anexos
- Codificação adequada para caracteres especiais

### Variáveis de Ambiente Necessárias

```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=seu_email@gmail.com
SMTP_PASSWORD=sua_senha_de_app
```

### Uso

```python
from utilities.email.smtp_client import SMTPClient

# Criar cliente SMTP
client = SMTPClient(
    smtp_server="smtp.gmail.com",
    smtp_port=587,
    email="seu_email@gmail.com",
    app_password="sua_senha_de_app"
)

# Enviar email simples
client.send_email(
    to="destinatario@email.com",
    subject="Assunto do Email",
    email_content="<h1>Olá!</h1><p>Este é um email de teste.</p>"
)

# Enviar email com anexos e cópias
client.send_email(
    to="destinatario@email.com",
    cc="copia@email.com",
    bcc="copia_oculta@email.com",
    subject="Relatório Mensal",
    email_content="<h1>Relatório</h1><p>Segue relatório em anexo.</p>",
    attachments=["relatorio.xlsx", "grafico.png"]
)
```

### Exemplo de Uso (`example.py`)

Arquivo de exemplo mostrando como usar o cliente SMTP com variáveis de ambiente.

### Dependências

- `python-dotenv`: Carregamento de variáveis de ambiente
- Bibliotecas padrão do Python: `smtplib`, `email`, `mimetypes`
