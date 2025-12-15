"""
デプロイ準備状況チェックスクリプト

このスクリプトは、WEB公開の準備が整っているか確認します。
"""

import os
import sys
from pathlib import Path

# プロジェクトルートをパスに追加
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

def check_files():
    """必要なファイルが存在するか確認"""
    print("=" * 60)
    print("ファイルチェック")
    print("=" * 60)
    
    required_files = [
        "main.py",
        "requirements.txt",
        "runtime.txt",
        "Procfile",
        ".streamlit/config.toml",
        ".streamlit/secrets.toml.template",
        ".gitignore",
        "Dockerfile",
        "docker-compose.yml",
    ]
    
    all_exist = True
    for file_path in required_files:
        full_path = project_root / file_path
        exists = full_path.exists()
        status = "OK" if exists else "MISSING"
        print(f"  [{status}] {file_path}")
        if not exists:
            all_exist = False
    
    return all_exist

def check_gitignore():
    """機密情報が.gitignoreに含まれているか確認"""
    print("\n" + "=" * 60)
    print(".gitignoreチェック")
    print("=" * 60)
    
    gitignore_path = project_root / ".gitignore"
    if not gitignore_path.exists():
        print("  [ERROR] .gitignoreが見つかりません")
        return False
    
    with open(gitignore_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    required_entries = [
        ".env",
        ".streamlit/secrets.toml",
        "API_KEYS_ACTUAL.md",
        "logs/",
    ]
    
    all_included = True
    for entry in required_entries:
        included = entry in content
        status = "OK" if included else "MISSING"
        print(f"  [{status}] {entry}")
        if not included:
            all_included = False
    
    return all_included

def check_environment():
    """環境変数が設定されているか確認"""
    print("\n" + "=" * 60)
    print("環境変数チェック")
    print("=" * 60)
    
    from dotenv import load_dotenv
    load_dotenv()
    
    env_vars = [
        "GOOGLE_API_KEY",
        "OPENAI_API_KEY",
    ]
    
    all_set = True
    for var in env_vars:
        value = os.getenv(var)
        if value and value != "your-openai-api-key-here" and value != "your-serpapi-key-here":
            print(f"  [OK] {var}: {value[:10]}...")
        else:
            print(f"  [MISSING] {var}")
            if var == "GOOGLE_API_KEY":
                all_set = False
    
    return all_set

def check_vectorstore():
    """ベクターストアが存在するか確認"""
    print("\n" + "=" * 60)
    print("ベクターストアチェック")
    print("=" * 60)
    
    vectorstore_path = project_root / "vectorstore"
    if not vectorstore_path.exists():
        print("  [MISSING] vectorstoreフォルダが見つかりません")
        print("  [INFO] scripts/deployment/create_vectorstore_openai.bat を実行してください")
        return False
    
    sqlite_file = vectorstore_path / "chroma.sqlite3"
    if sqlite_file.exists():
        size_mb = sqlite_file.stat().st_size / (1024 * 1024)
        print(f"  [OK] chroma.sqlite3 ({size_mb:.2f} MB)")
        return True
    else:
        print("  [MISSING] chroma.sqlite3が見つかりません")
        return False

def check_data():
    """データフォルダが存在するか確認"""
    print("\n" + "=" * 60)
    print("データフォルダチェック")
    print("=" * 60)
    
    data_path = project_root / "data"
    if not data_path.exists():
        print("  [MISSING] dataフォルダが見つかりません")
        return False
    
    # サブフォルダをカウント
    subfolders = [d for d in data_path.iterdir() if d.is_dir()]
    print(f"  [OK] dataフォルダ: {len(subfolders)} サブフォルダ")
    
    # ファイル数をカウント
    file_count = 0
    for root, dirs, files in os.walk(data_path):
        file_count += len(files)
    
    print(f"  [OK] 合計ファイル数: {file_count}")
    
    return file_count > 0

def check_dependencies():
    """依存関係がインストールされているか確認"""
    print("\n" + "=" * 60)
    print("依存関係チェック")
    print("=" * 60)
    
    required_packages = [
        ("streamlit", "streamlit"),
        ("langchain", "langchain"),
        ("chromadb", "chromadb"),
        ("google-generativeai", "google.generativeai"),
    ]
    
    all_installed = True
    for package_name, import_name in required_packages:
        try:
            __import__(import_name)
            print(f"  [OK] {package_name}")
        except ImportError:
            print(f"  [MISSING] {package_name}")
            all_installed = False
    
    return all_installed

def main():
    """メイン処理"""
    print("\n" + "=" * 60)
    print("デプロイ準備状況チェック")
    print("=" * 60)
    print()
    
    results = {
        "ファイル": check_files(),
        ".gitignore": check_gitignore(),
        "環境変数": check_environment(),
        "ベクターストア": check_vectorstore(),
        "データ": check_data(),
        "依存関係": check_dependencies(),
    }
    
    print("\n" + "=" * 60)
    print("チェック結果サマリー")
    print("=" * 60)
    
    for category, result in results.items():
        status = "OK" if result else "NG"
        print(f"  [{status}] {category}")
    
    all_ok = all(results.values())
    
    print("\n" + "=" * 60)
    if all_ok:
        print("すべてのチェックが完了しました！")
        print("デプロイの準備が整っています。")
        print("\n次のステップ:")
        print("  1. GitHubにプッシュ: git push")
        print("  2. Streamlit Cloudでデプロイ: https://share.streamlit.io/")
        print("  3. Secretsを設定")
    else:
        print("いくつかの問題が見つかりました。")
        print("上記のエラーを修正してから再度実行してください。")
    print("=" * 60)
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())

