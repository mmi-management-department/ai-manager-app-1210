"""
賃金規程の検索テスト
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# 環境変数の読み込み
load_dotenv()

# OpenAI APIキーの取得
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    print("[ERROR] OPENAI_API_KEY が設定されていません")
    exit(1)

print("=" * 60)
print("賃金規程 検索テスト")
print("=" * 60)

# 埋め込みモデルの初期化
print("\n[1] 埋め込みモデルを初期化しています...")
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=openai_api_key
)
print("[OK] 埋め込みモデルの初期化完了")

# ベクターストアの読み込み
vectorstore_path = "./vectorstore"
print(f"\n[2] ベクターストアを読み込んでいます: {vectorstore_path}")

db = Chroma(
    persist_directory=vectorstore_path,
    embedding_function=embeddings
)
print("[OK] ベクターストアの読み込み完了")

# ドキュメント数の確認
print("\n[3] ベクターストアの内容を確認しています...")
try:
    collection = db._collection
    doc_count = collection.count()
    print(f"[OK] ドキュメント数: {doc_count}件")
except Exception as e:
    print(f"[WARNING] ドキュメント数の確認に失敗: {e}")

# 賃金規程で検索
test_queries = [
    "賃金規程",
    "賃金形態",
    "給与体系",
    "エムエムの賃金形態は？",
    "賃金規程について教えて"
]

for query in test_queries:
    print(f"\n{'=' * 60}")
    print(f"クエリ: 「{query}」")
    print("=" * 60)
    
    results = db.similarity_search(query, k=5)
    
    print(f"\n検索結果: {len(results)}件")
    
    if len(results) > 0:
        for i, doc in enumerate(results, 1):
            print(f"\n【結果 {i}】")
            source = doc.metadata.get('source', 'N/A')
            print(f"ソース: {source}")
            
            # 賃金規程のファイルかチェック
            if "賃金規程" in source or "I-02" in source:
                print("★ 賃金規程のファイルです！")
            
            print(f"内容（最初の300文字）:")
            print(doc.page_content[:300])
            print("-" * 60)
    else:
        print("[ERROR] 検索結果が0件です！")

print("\n" + "=" * 60)
print("テスト完了")
print("=" * 60)

