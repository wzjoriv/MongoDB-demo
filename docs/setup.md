# Backend Environment Setup

It is expected that all shell commands are executed from the root directory of the project (e.g., `path/to/lar-backend`)

## Dependencies

### I. Software

1. Install MongoDB
    
    * [Window](https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-6.0.6-signed.msi)

    * [macOS](https://fastdl.mongodb.org/osx/mongodb-macos-x86_64-6.0.6.tgz)

    * [macOS ARM 64](https://fastdl.mongodb.org/osx/mongodb-macos-arm64-6.0.6.tgz)

    * [Linux](https://www.mongodb.com/try/download/community)

2. Install [python](https://www.python.org/downloads/)

3. Install virtual environment package (**Optional**)

    It comes built-in with the latest python release
     
    ```bash
    pip install venv
    ```


### II. Setup virtual environment

1. Create environment and activate virtual enviorment (**Optional**)

    ```bash
    python -m venv .venv

    source .venv/bin/activate # macOS/Linux
    .venv\Scripts\Activate.ps1 # Windows PS
    .venv\Scripts\activate.bat # Windows CMD


2. **VS Code:** Select environment

    1. Go to a python file (e.g., `python.py`)
    2. Select environment

        ![Select environment on the bottom left of VS Code](media/environment%20selection.gif)

3. Install packages

    ```bash
    pip install -r requirements.txt
    ```


## Execution

### I. Start MongoDB

```bash
path/to/mongod.exe --config “path/to/mongod.cfg” # Windows
mongod --config /usr/local/etc/mongod.conf --fork # macOS
mongod --config /opt/homebrew/etc/mongod.conf --fork # macOS ARM 64
```

## Extra

To deactivate a python environment, execute:

```bash
deactivate
```