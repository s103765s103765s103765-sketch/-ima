# 軽量なPython 3.10 (slim) イメージを使用
# full imageよりサイズが小さく、ビルドも早いです
FROM python:3.10-slim

# ログがバッファリングされずにすぐに表示されるように設定
# (これがないとNorthflankのログ画面で出力が遅延します)
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# 作業ディレクトリを作成
WORKDIR /app

# セキュリティ対策: rootユーザーではなく一般ユーザーを作成して使用する
RUN useradd -m -u 1000 botuser

# 依存関係ファイルを先にコピー（キャッシュ効率化のため）
COPY requirements.txt .

# 依存ライブラリのインストール
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコピー
COPY . .

# ユーザーを切り替え
USER botuser

# ボットを実行 (ファイル名が違う場合は main.py を書き換えてください)
CMD ["python", "main.py"]
