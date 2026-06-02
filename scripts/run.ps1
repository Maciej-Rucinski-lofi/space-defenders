$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot

Set-Location $ProjectRoot

if (-not (Test-Path ".venv\Scripts\Activate.ps1")) {
    Write-Error "Virtual environment not found. Run scripts\setup.ps1 first."
}

& ".venv\Scripts\Activate.ps1"
Set-Location src
python main.py
Set-Location $ProjectRoot
