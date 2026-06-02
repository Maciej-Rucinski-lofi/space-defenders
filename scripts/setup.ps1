$ErrorActionPreference = "Stop"
$ProjectRoot = Split-Path -Parent $PSScriptRoot

Set-Location $ProjectRoot

if (-not (Test-Path ".venv")) {
    python -m venv .venv
    Write-Host "Created virtual environment in .venv"
}

& ".venv\Scripts\Activate.ps1"
python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host ""
Write-Host "Setup complete. Activate the environment with:"
Write-Host "  .\.venv\Scripts\Activate.ps1"
