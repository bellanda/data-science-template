# Data Science Project Template

A comprehensive template for data science projects with pre-configured tools and utilities for Oracle database connections, email functionality, SMB file sharing, and more.

## Features

- Pre-configured Oracle database connections
- Email functionality for reports and alerts
- SMB file server access
- Excel export with styling
- RAPIDS AI libraries for GPU-accelerated data processing
- Various data manipulation libraries (pandas, polars)

## Project Structure

```
data-science-template/
├── data/                # Data files (CSV, Excel, Parquet, etc.)
├── documents/           # Project documentation
├── notebooks/           # Jupyter notebooks
├── sql/                 # SQL queries
│   └── temporary.sql    # Temporary SQL scripts
├── utilities/           # Utility functions
├── scripts/             # Standalone Python scripts
├── .env                 # Environment variables (not in version control)
├── .env.example         # Example environment variables
└── pyproject.toml       # Project dependencies
```

## Prerequisites

- Python 3.11 or later
- Oracle Instant Client (for Oracle database connections)
- NVIDIA GPU with CUDA 12.x support (for RAPIDS libraries)

## Installation

### Linux/macOS

```bash
# Clone the repository (or use as template)
cd YOUR_PROJECT_FOLDER

# Install uv (package manager)
curl -LsSf https://astral.sh/uv/install.sh | bash

# Install dependencies
uv sync

# Create directory structure (Git doesn't track empty directories)
mkdir -p data/{csv,excel,parquet,json,pickle,raw,processed}
```

### Windows

```powershell
# Clone the repository (or use as template)
cd YOUR_PROJECT_FOLDER

# Install uv (package manager)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Install dependencies
uv sync

# Create directory structure (Git doesn't track empty directories)
mkdir -Force -Path data/csv, data/excel, data/parquet, data/json, data/pickle, data/raw, data/processed
```

## Configuration

1. Copy `.env.example` to `.env`
2. Update the values in `.env` with your credentials and configuration

```bash
cp .env.example .env
```

## Utilities

The `utilities` directory contains helper functions for:

- Oracle database connections
- Email sending (reports and alerts)
- SMB file server access
- Excel export with styling

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
