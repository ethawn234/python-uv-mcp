- Create a venv in `venv` (and seed pip/setuptools/wheel):
```powershell
uv venv venv --seed
```

- Create a venv in the current directory:
```powershell
uv venv .
```

- Run Python (or any command) inside the venv without activating:
```powershell
uv run python
uv run -- python script.py
```

- Use uv's pip wrapper:
```powershell
uv pip install <package>
```

- (Windows PowerShell activation alternative)
```powershell
.\venv\Scripts\Activate.ps1

- Auto starts when terminal opens
& C:/Users/obd1/repos/python-uv-mcp/.venv/Scripts/Activate.ps1
```

- Install from pyproject.toml
`uv pip install -r pyproject.toml`