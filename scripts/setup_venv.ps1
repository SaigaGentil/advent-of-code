param(
    [string]$VenvPath = ".venv"
)

Write-Host "Creating virtual environment at $VenvPath..."
python -m venv $VenvPath
$venvPython = Join-Path $VenvPath "Scripts\python.exe"
if (-Not (Test-Path $venvPython)) {
    Write-Error "Python in venv not found at $venvPython"
    exit 1
}
& $venvPython -m pip install --upgrade pip
if (Test-Path "requirements-dev.txt") {
    & $venvPython -m pip install -r requirements-dev.txt
}
Write-Host "Virtual environment ready. Activate with: .\$VenvPath\Scripts\Activate.ps1"