@echo off
chcp 65001 >nul
echo ===================================================
echo CHAT TING TING - TỰ ĐỘNG BIÊN DỊCH (ONE-CLICK BUILD)
echo ===================================================

echo [1/4] Kiem tra Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [LOI] Khong tim thay Python. Vui long cai dat Python va check box "Add Python to PATH" luc cai dat.
    pause
    exit /b
)

echo [2/4] Tao va kich hoat moi truong ao (virtualenv)...
if not exist "venv\" (
    python -m venv venv
)
call venv\Scripts\activate.bat

echo [3/4] Cai dat thu vien can thiet (PyInstaller)...
pip install -r requirements.txt

echo [4/4] Dang bien dich chuong trinh thanh file thuc thi (.exe)...
pyinstaller --noconfirm --onefile --noconsole --name "ChatTingTing_Guide" "main.py"

echo ===================================================
echo HOAN TAT!
echo File thuc thi ChatTingTing_Guide.exe da duoc tao thanh cong trong thu muc 'dist'.
echo ===================================================
pause
