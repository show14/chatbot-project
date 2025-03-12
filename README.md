# README
## 環境構築
このプロジェクトをローカル環境で実行するには、以下の手順を実行してください。
### パッケージのインストール
Python 3.9 以上の環境で以下のコマンドを実行してください。
pip3 install fastapi uvicorn langchain chainlit

### モデルの準備
チャットボットモデルはollamaを使用します。以下の手順でモデルを準備してください。
1. ollamaをインストールしていない場合は、[公式サイト](https://ollama.com/)からインストールして下さい。
2. ollama を起動する。
ollama serve
3. llama3.1:8b をダウンロードする。
ollama pull llama3.1:8b

## 実行方法
### Chainlit チャットボットの起動
以下のコマンドで Chainlit チャットボットを起動できます。
chainlit run my_chat.py