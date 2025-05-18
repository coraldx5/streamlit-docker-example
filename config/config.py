from pathlib import Path
import os

# ログディレクトリの絶対パスを指定（推奨）
BASE_DIR = Path(__file__).resolve().parent.parent
log_dir = BASE_DIR / "logs"
log_dir.mkdir(parents=True, exist_ok=True)  # 存在しない場合は作成

class Config:
    AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY","")