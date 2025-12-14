"""
管理画面
アクセスログの確認と統計情報を提供する管理者専用ページ
"""

import streamlit as st
import json
import datetime
from pathlib import Path
import pandas as pd
import os

# ページ設定
st.set_page_config(
    page_title="管理画面 - MMI AI管理部長",
    page_icon="🛡️",
    layout="wide"
)


def get_admin_password() -> str:
    """管理者パスワードを取得します"""
    # 環境変数から取得
    admin_password = os.getenv("ADMIN_PASSWORD")
    
    # Streamlit secretsから取得
    if not admin_password and hasattr(st, "secrets") and "auth" in st.secrets:
        admin_password = st.secrets["auth"].get("admin_password", "")
    
    # デフォルトパスワード（開発用）
    if not admin_password:
        admin_password = "admin2024"
    
    return admin_password


def check_admin_auth() -> bool:
    """管理者認証をチェックします"""
    if "admin_authenticated" not in st.session_state:
        st.session_state.admin_authenticated = False
    
    if st.session_state.admin_authenticated:
        return True
    
    st.markdown("# 🔐 管理者認証")
    st.markdown("---")
    st.info("管理画面にアクセスするには、管理者パスワードを入力してください。")
    
    with st.form("admin_auth_form"):
        password = st.text_input(
            "管理者パスワード",
            type="password",
            placeholder="管理者パスワードを入力"
        )
        submit = st.form_submit_button("ログイン")
        
        if submit:
            correct_password = get_admin_password()
            if password == correct_password:
                st.session_state.admin_authenticated = True
                st.success("✅ 認証に成功しました！")
                st.rerun()
            else:
                st.error("❌ パスワードが正しくありません。")
                return False
    
    st.markdown("---")
    st.caption("💡 管理者パスワードは環境変数 `ADMIN_PASSWORD` または Streamlit Secrets で設定できます。")
    st.stop()
    return False


def get_log_file_path() -> Path:
    """ログファイルのパスを取得します"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    return log_dir / "access_log.json"


def load_access_logs() -> list:
    """アクセスログを読み込みます"""
    try:
        log_file = get_log_file_path()
        if not log_file.exists():
            return []
        
        with open(log_file, 'r', encoding='utf-8') as f:
            logs = json.load(f)
        
        return logs
    except Exception as e:
        st.error(f"ログの読み込みに失敗しました: {e}")
        return []


def format_timestamp(timestamp_str: str) -> str:
    """タイムスタンプを読みやすい形式にフォーマットします"""
    try:
        dt = datetime.datetime.fromisoformat(timestamp_str)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return timestamp_str


def get_statistics(logs: list) -> dict:
    """ログから統計情報を計算します"""
    if not logs:
        return {
            "total": 0,
            "success": 0,
            "failed": 0,
            "success_rate": 0,
            "unique_ips": 0,
            "recent_24h": 0,
            "failed_24h": 0
        }
    
    total = len(logs)
    success = sum(1 for log in logs if log.get("success", False))
    failed = total - success
    success_rate = (success / total * 100) if total > 0 else 0
    
    # ユニークIPアドレス数
    unique_ips = len(set(log.get("ip_address", "unknown") for log in logs))
    
    # 過去24時間の統計
    cutoff_time = datetime.datetime.now() - datetime.timedelta(hours=24)
    recent_24h = 0
    failed_24h = 0
    
    for log in logs:
        try:
            log_time = datetime.datetime.fromisoformat(log["timestamp"])
            if log_time > cutoff_time:
                recent_24h += 1
                if not log.get("success", False):
                    failed_24h += 1
        except:
            continue
    
    return {
        "total": total,
        "success": success,
        "failed": failed,
        "success_rate": success_rate,
        "unique_ips": unique_ips,
        "recent_24h": recent_24h,
        "failed_24h": failed_24h
    }


def get_data_folders() -> list:
    """dataフォルダ内のサブフォルダ一覧を取得します"""
    data_dir = Path("data")
    if not data_dir.exists():
        return []
    
    folders = []
    for item in data_dir.iterdir():
        if item.is_dir():
            folders.append(item.name)
    
    return sorted(folders)


def save_uploaded_file(uploaded_file, target_folder: str) -> bool:
    """アップロードされたファイルを保存します"""
    try:
        data_dir = Path("data") / target_folder
        data_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = data_dir / uploaded_file.name
        
        # ファイルを保存
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        return True
    except Exception as e:
        st.error(f"ファイルの保存に失敗しました: {e}")
        return False


def get_folder_files(folder_name: str) -> list:
    """指定フォルダ内のファイル一覧を取得します（サブフォルダを含む）"""
    folder_path = Path("data") / folder_name
    if not folder_path.exists():
        return []
    
    files = []
    
    def scan_directory(directory: Path, base_path: Path):
        """ディレクトリを再帰的にスキャンします"""
        for item in directory.iterdir():
            if item.is_file():
                try:
                    stat = item.stat()
                    # 相対パスを取得（data/フォルダ名からの相対パス）
                    relative_path = item.relative_to(base_path)
                    files.append({
                        "name": str(relative_path),
                        "size": stat.st_size,
                        "modified": datetime.datetime.fromtimestamp(stat.st_mtime)
                    })
                except Exception:
                    # エラーが発生したファイルはスキップ
                    pass
            elif item.is_dir():
                # サブディレクトリを再帰的にスキャン
                scan_directory(item, base_path)
    
    scan_directory(folder_path, folder_path)
    
    return sorted(files, key=lambda x: x["modified"], reverse=True)


def format_file_size(size_bytes: int) -> str:
    """ファイルサイズを読みやすい形式にフォーマットします"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def show_file_management():
    """ファイル管理タブの内容を表示します"""
    st.markdown("## 📁 ファイル管理")
    st.markdown("dataフォルダ内にファイルをアップロードできます。")
    st.markdown("---")
    
    # フォルダ一覧を取得
    folders = get_data_folders()
    
    if not folders:
        st.warning("⚠️ dataフォルダ内にサブフォルダが見つかりませんでした。")
        return
    
    # ファイルアップロードセクション
    st.markdown("### 📤 ファイルアップロード")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        selected_folder = st.selectbox(
            "アップロード先フォルダ",
            folders,
            help="ファイルをアップロードするフォルダを選択してください"
        )
    
    with col2:
        uploaded_files = st.file_uploader(
            "ファイルを選択（複数可）",
            accept_multiple_files=True,
            help="PDF、Word、Excel、PowerPoint、Markdown、画像（JPG/PNG/GIF等）、動画（MP4/AVI/MOV等）をアップロードできます"
        )
    
    if uploaded_files:
        if st.button("📤 アップロード実行", type="primary", use_container_width=True):
            success_count = 0
            error_count = 0
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, uploaded_file in enumerate(uploaded_files):
                status_text.text(f"アップロード中: {uploaded_file.name}")
                
                if save_uploaded_file(uploaded_file, selected_folder):
                    success_count += 1
                    st.success(f"✅ {uploaded_file.name} をアップロードしました")
                else:
                    error_count += 1
                
                progress_bar.progress((i + 1) / len(uploaded_files))
            
            status_text.empty()
            progress_bar.empty()
            
            st.success(f"🎉 {success_count}個のファイルをアップロードしました！")
            
            if error_count > 0:
                st.warning(f"⚠️ {error_count}個のファイルでエラーが発生しました。")
            
            # ベクターストア再生成の通知
            st.markdown("---")
            st.info("⚠️ **重要**: ファイルをアップロードした後は、ベクターストアを再生成する必要があります。")
            st.markdown("""
            **手順:**
            1. ローカル環境で `scripts/deployment/create_vectorstore_openai.bat` を実行
            2. 生成された `vectorstore` フォルダをGitHubにプッシュ
            3. 新しい情報が検索可能になります
            
            または、管理者に再生成を依頼してください。
            """)
    
    st.markdown("---")
    
    # ファイル一覧表示
    st.markdown("### 📋 ファイル一覧")
    
    selected_view_folder = st.selectbox(
        "表示するフォルダ",
        folders,
        key="view_folder"
    )
    
    files = get_folder_files(selected_view_folder)
    
    if not files:
        st.info(f"📂 `{selected_view_folder}` フォルダにファイルがありません。")
    else:
        st.caption(f"📊 合計 {len(files)} ファイル")
        
        # ファイル情報をDataFrameに変換
        file_df_data = []
        for file_info in files:
            file_df_data.append({
                "ファイル名": file_info["name"],
                "サイズ": format_file_size(file_info["size"]),
                "更新日時": file_info["modified"].strftime("%Y-%m-%d %H:%M:%S")
            })
        
        file_df = pd.DataFrame(file_df_data)
        
        st.dataframe(
            file_df,
            use_container_width=True,
            hide_index=True,
            height=400
        )
    
    st.markdown("---")
    st.caption("💡 サポートされるファイル形式: PDF, Markdown (.md), Word (.docx), Excel (.xlsx), PowerPoint (.pptx)")
    st.caption("⚠️ アップロード後は必ずベクターストアを再生成してください")


def main():
    """メイン処理"""
    # 管理者認証チェック
    if not check_admin_auth():
        return
    
    # ヘッダー
    st.markdown("# 🛡️ 管理画面")
    st.markdown("---")
    
    # ログアウトボタン
    col1, col2, col3 = st.columns([6, 1, 1])
    with col3:
        if st.button("🚪 ログアウト", use_container_width=True):
            st.session_state.admin_authenticated = False
            st.rerun()
    
    # タブで機能を切り替え
    tab1, tab2 = st.tabs(["📊 アクセスログ", "📁 ファイル管理"])
    
    with tab1:
        show_access_logs()
    
    with tab2:
        show_file_management()


def show_access_logs():
    """アクセスログタブの内容を表示します"""
    st.markdown("## 📊 アクセスログと統計情報")
    st.markdown("---")
    
    # ログを読み込む
    logs = load_access_logs()
    
    if not logs:
        st.warning("⚠️ アクセスログが見つかりませんでした。")
        st.info("ユーザーがアプリにアクセスするとログが記録されます。")
        return
    
    # 統計情報
    stats = get_statistics(logs)
    
    st.markdown("## 📊 統計情報")
    
    # メトリクスを表示
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("総アクセス数", stats["total"])
    
    with col2:
        st.metric("成功", stats["success"], delta=f"{stats['success_rate']:.1f}%")
    
    with col3:
        st.metric("失敗", stats["failed"])
    
    with col4:
        st.metric("ユニークIP", stats["unique_ips"])
    
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        st.metric("過去24時間", stats["recent_24h"])
    
    with col6:
        st.metric("24h失敗数", stats["failed_24h"])
    
    st.markdown("---")
    
    # フィルタリングオプション
    st.markdown("## 🔍 ログフィルター")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        filter_status = st.selectbox(
            "ステータス",
            ["すべて", "成功のみ", "失敗のみ"]
        )
    
    with col2:
        # IPアドレスのリスト
        all_ips = sorted(set(log.get("ip_address", "unknown") for log in logs))
        filter_ip = st.selectbox(
            "IPアドレス",
            ["すべて"] + all_ips
        )
    
    with col3:
        filter_hours = st.selectbox(
            "期間",
            ["すべて", "過去1時間", "過去24時間", "過去7日間", "過去30日間"]
        )
    
    # ログをフィルタリング
    filtered_logs = logs.copy()
    
    # ステータスフィルター
    if filter_status == "成功のみ":
        filtered_logs = [log for log in filtered_logs if log.get("success", False)]
    elif filter_status == "失敗のみ":
        filtered_logs = [log for log in filtered_logs if not log.get("success", False)]
    
    # IPアドレスフィルター
    if filter_ip != "すべて":
        filtered_logs = [log for log in filtered_logs if log.get("ip_address") == filter_ip]
    
    # 期間フィルター
    if filter_hours != "すべて":
        hours_map = {
            "過去1時間": 1,
            "過去24時間": 24,
            "過去7日間": 24 * 7,
            "過去30日間": 24 * 30
        }
        hours = hours_map.get(filter_hours, 0)
        cutoff_time = datetime.datetime.now() - datetime.timedelta(hours=hours)
        
        filtered_logs = [
            log for log in filtered_logs
            if datetime.datetime.fromisoformat(log["timestamp"]) > cutoff_time
        ]
    
    st.markdown("---")
    
    # ログテーブルを表示
    st.markdown(f"## 📋 アクセスログ ({len(filtered_logs)}件)")
    
    if not filtered_logs:
        st.info("フィルター条件に一致するログがありません。")
        return
    
    # DataFrameに変換
    df_data = []
    for log in reversed(filtered_logs):  # 新しい順に表示
        df_data.append({
            "タイムスタンプ": format_timestamp(log.get("timestamp", "")),
            "ステータス": "✅ 成功" if log.get("success", False) else "❌ 失敗",
            "ユーザー名": log.get("username", "unknown"),
            "IPアドレス": log.get("ip_address", "unknown")
        })
    
    df = pd.DataFrame(df_data)
    
    # テーブル表示
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=400
    )
    
    # CSVダウンロード
    csv = df.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📥 CSVでダウンロード",
        data=csv,
        file_name=f"access_logs_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )
    
    st.markdown("---")
    
    # IPアドレス別統計
    st.markdown("## 🌐 IPアドレス別統計")
    
    ip_stats = {}
    for log in logs:
        ip = log.get("ip_address", "unknown")
        if ip not in ip_stats:
            ip_stats[ip] = {"total": 0, "success": 0, "failed": 0}
        
        ip_stats[ip]["total"] += 1
        if log.get("success", False):
            ip_stats[ip]["success"] += 1
        else:
            ip_stats[ip]["failed"] += 1
    
    # DataFrameに変換
    ip_df_data = []
    for ip, stats in sorted(ip_stats.items(), key=lambda x: x[1]["total"], reverse=True):
        success_rate = (stats["success"] / stats["total"] * 100) if stats["total"] > 0 else 0
        ip_df_data.append({
            "IPアドレス": ip,
            "総アクセス": stats["total"],
            "成功": stats["success"],
            "失敗": stats["failed"],
            "成功率": f"{success_rate:.1f}%"
        })
    
    ip_df = pd.DataFrame(ip_df_data)
    
    st.dataframe(
        ip_df,
        use_container_width=True,
        hide_index=True
    )
    
    st.markdown("---")
    st.caption("💡 ログは最新100件まで自動的に保持されます。")
    st.caption("🔒 この管理画面は管理者パスワードで保護されています。")


if __name__ == "__main__":
    main()

