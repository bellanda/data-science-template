# Excel Utilities

Este módulo contém utilitários para manipulação e exportação de arquivos Excel.

## Export Excel with Style (`export_excel_with_style.py`)

Utilitário para exportar DataFrames do pandas para Excel com formatação e estilo profissional.

### Funcionalidades

- Exportação de DataFrames com formatação automática
- Cabeçalhos estilizados (azul com texto branco)
- Bordas e alinhamento automático
- Ajuste automático da largura das colunas
- Aplicação de filtros e tabelas formatadas

### Funções Principais

#### `export_excel_with_style(df, file_path)`

Exporta um DataFrame para Excel com estilo pré-definido.

#### `adjust_column_width(writer, df, sheet_name)`

Ajusta automaticamente a largura das colunas baseado no conteúdo.

#### `apply_filter(writer, df, sheet_name)`

Aplica filtros automáticos e formatação de tabela.

### Uso

```python
import pandas as pd
from utilities.excel.export_excel_with_style import export_excel_with_style

# Criar um DataFrame de exemplo
df = pd.DataFrame({
    'Nome': ['João', 'Maria', 'Pedro'],
    'Idade': [25, 30, 35],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
})

# Exportar com estilo
export_excel_with_style(df, 'relatorio_estilizado.xlsx')
```

### Dependências

- `pandas`: Manipulação de dados
- `openpyxl`: Manipulação de arquivos Excel
- `xlsxwriter`: Engine para escrita de Excel com formatação
