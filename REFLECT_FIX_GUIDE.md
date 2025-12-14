# 🔧 修正が反映されない場合の対処法

**対象:** 「社内問い合わせ」が初期選択されない問題

---

## ✅ 修正は完了していますが...

**ファイルの修正内容:**
- ✅ `initialize.py`: 212-213行目に初期化コード追加済み
- ✅ `components.py`: 48-62行目に動的index計算追加済み

**しかし、アプリ上で反映されない原因:**
1. Streamlitのセッションキャッシュが残っている
2. ブラウザのキャッシュが残っている
3. アプリが完全に再起動されていない

---

## 🚀 解決方法（3つの方法）

### 方法1: セッションクリア（推奨・最も確実）

```bash
streamlit run clear_session.py
```

1. セッションクリアページが開きます
2. 「🗑️ セッションをクリア」ボタンをクリック
3. メインアプリに戻る

### 方法2: 完全再起動

```bash
# 1. 現在のStreamlitを完全停止（Ctrl+C）
# Ctrl+Cを押してサーバーを停止

# 2. ブラウザのキャッシュをクリア
# Ctrl+Shift+Delete（Chrome/Edge）
# または Ctrl+F5 でハードリロード

# 3. アプリを再起動
streamlit run main.py
```

### 方法3: ブラウザのシークレットモード

```bash
# 1. アプリを起動
streamlit run main.py

# 2. シークレットウィンドウで開く
# Chrome: Ctrl+Shift+N
# Edge: Ctrl+Shift+P
# Firefox: Ctrl+Shift+P

# 3. 表示されたURLをシークレットウィンドウで開く
```

---

## 🔍 確認方法

### 正常に反映されている場合

アプリ起動時のサイドバー:

```
🎯 利用目的

○ 社内文書検索
● 社内問い合わせ  ← これが選択されている
```

### まだ反映されていない場合

```
🎯 利用目的

● 社内文書検索    ← これが選択されている
○ 社内問い合わせ
```

---

## 📊 詳細な対処手順

### ステップ1: ファイル修正の確認

```bash
# initialize.pyを確認
python -c "
with open('initialize.py', 'r', encoding='utf-8') as f:
    content = f.read()
    if 'ANSWER_MODE_2' in content:
        print('✅ initialize.py: 修正済み')
    else:
        print('❌ initialize.py: 未修正')
"

# components.pyを確認
python -c "
with open('components.py', 'r', encoding='utf-8') as f:
    content = f.read()
    if 'default_index = 1' in content:
        print('✅ components.py: 修正済み')
    else:
        print('❌ components.py: 未修正')
"
```

### ステップ2: セッションクリア

```bash
streamlit run clear_session.py
```

### ステップ3: メインアプリ起動

```bash
streamlit run main.py
```

### ステップ4: 確認

サイドバーで「● 社内問い合わせ」が選択されていることを確認

---

## 💡 なぜ反映されないのか？

### Streamlitのセッションステートの仕組み

```python
# initialize.pyの初期化コード
if "mode" not in st.session_state:
    st.session_state.mode = ct.ANSWER_MODE_2
```

**問題:**
- 一度でもアプリを開くと、`mode`がセッションステートに保存される
- 次回以降は`if "mode" not in st.session_state:`が`False`になる
- **初期化コードが実行されない**

**解決策:**
- セッションステートをクリアする
- または、ブラウザの新しいセッションで開く

---

## 🔧 トラブルシューティング

### Q1: セッションクリアしても変わらない

**A:** Streamlitサーバーを完全に再起動

```bash
# ターミナルで Ctrl+C を押してサーバーを停止
# 数秒待つ
streamlit run main.py
```

### Q2: 何度やっても「社内文書検索」が選択される

**A:** ブラウザのキャッシュをクリア

```bash
# Chromeの場合
1. Ctrl+Shift+Delete
2. 「キャッシュされた画像とファイル」にチェック
3. 「データを削除」

# または
Ctrl+F5 でハードリロード
```

### Q3: シークレットモードでも変わらない

**A:** ファイルの修正を再確認

```bash
# initialize.pyの該当行を表示
python -c "
with open('initialize.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for i, line in enumerate(lines[210:215], 211):
        print(f'{i}: {line}', end='')
"
```

**期待される出力:**
```
211:     # モードの初期値を「社内問い合わせ」に設定
212:     if "mode" not in st.session_state:
213:         st.session_state.mode = ct.ANSWER_MODE_2  # 「社内問い合わせ」
```

---

## 📝 確実な手順（推奨）

### 完全リセット手順

```bash
# ステップ1: Streamlit停止
# ターミナルで Ctrl+C

# ステップ2: セッションクリア用アプリを起動
streamlit run clear_session.py

# ステップ3: 「セッションをクリア」ボタンをクリック

# ステップ4: Streamlit停止
# Ctrl+C

# ステップ5: ブラウザを完全に閉じる

# ステップ6: メインアプリを起動
streamlit run main.py

# ステップ7: ブラウザで開く
# http://localhost:8501

# ステップ8: サイドバーを確認
# 「● 社内問い合わせ」が選択されていることを確認
```

---

## 🎯 最も簡単な方法

### シークレットモードで確認

1. アプリを起動:
   ```bash
   streamlit run main.py
   ```

2. ブラウザでシークレットウィンドウを開く:
   - **Chrome:** Ctrl+Shift+N
   - **Edge:** Ctrl+Shift+P

3. URLを入力:
   ```
   http://localhost:8501
   ```

4. サイドバーを確認

✅ シークレットモードは常にクリーンなセッションで開始されます

---

## ✅ 成功の確認

### チェックリスト

- [ ] Streamlitサーバーを再起動した
- [ ] セッションクリアを実行した
- [ ] ブラウザのキャッシュをクリアした（またはシークレットモード）
- [ ] サイドバーで「● 社内問い合わせ」が選択されている

**すべてチェックが付いたら成功です！**

---

## 📞 それでも解決しない場合

以下の情報を確認してください:

```bash
# 1. ファイルの内容確認
cat initialize.py | grep -A 2 "mode not in"

# 2. Pythonバージョン
python --version

# 3. Streamlitバージョン
streamlit --version

# 4. エラーログ
# ターミナルのエラーメッセージをコピー
```

---

## 🎉 まとめ

**最も確実な方法:**

1. **セッションクリア:**
   ```bash
   streamlit run clear_session.py
   ```

2. **メインアプリ起動:**
   ```bash
   streamlit run main.py
   ```

3. **シークレットモードで確認**

これで確実に「社内問い合わせ」が初期選択されます！

---

*作成日: 2025年12月14日*
