# ==========================================
# 社内情報特化型生成AI検索アプリ - Dockerfile
# ==========================================

FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# システムパッケージの更新とクリーンアップ
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Pythonの依存関係をコピーしてインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルをコピー
COPY . .

# ログディレクトリを作成
RUN mkdir -p logs

# ポートを公開
EXPOSE 8501

# ヘルスチェック
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Streamlitを起動
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]

