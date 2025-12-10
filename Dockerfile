# 軽量版のPython 3.10を使用
FROM python:3.10-slim

# ログを即座に出力させる設定（Northflankで重要）
ENV PYTHONUNBUFFERED=1

# 作業フォルダ設定
WORKDIR /app

# 依存ファイルを先にコピーしてインストール（ビルド高速化）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 残りのコードをコピー
COPY . .

# 一般ユーザーを作成して実行（セキュリティ対策）
RUN useradd -m botuser
USER botuser

# ボット起動
CMD ["python", "main.py"]
