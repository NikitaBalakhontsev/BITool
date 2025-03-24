import os
import sys
import subprocess
import threading
import time
from typing import Optional

import webview

child_proc: Optional[subprocess.Popen] = None

def get_dashboard_script() -> str:
    # """Путь к dashboard.py (для PyInstaller onefile)."""
    # if hasattr(sys, "_MEIPASS"):
    #     return os.path.join(sys._MEIPASS, "dashboard.py")
    # else:
    return os.path.join(os.path.dirname(__file__), "dashboard.py")

def run_streamlit():
    global child_proc
    dashboard_path = get_dashboard_script()
    # Запускаем Streamlit в фоне
    child_proc = subprocess.Popen([
        sys.executable, "-m", "streamlit", "run",
        dashboard_path,
        "--server.headless=true",
        "--server.port=8501"
    ], shell=False)

def on_closing():
    global child_proc
    if child_proc and child_proc.poll() is None:
        try:
            child_proc.terminate()
            child_proc.wait(timeout=3)
        except Exception:
            child_proc.kill()
    sys.exit(0)

def main():
    # 1. Запускаем Streamlit в отдельном потоке
    t = threading.Thread(target=run_streamlit, daemon=True)
    t.start()

    # 2. Делаем паузу, чтобы сервер успел стартовать
    time.sleep(3)

    # 3. Создаём окно PyWebView
    window = webview.create_window(
        title="BI-инструмент (Desktop)",
        url="http://localhost:8501",
        width=1200,
        height=800
    )
    # Обработчик закрытия окна
    window.events.closing += on_closing

    # 4. Запускаем PyWebView c движком Edge Chromium
    webview.start(gui='edgechromium')

if __name__ == "__main__":
    main()
