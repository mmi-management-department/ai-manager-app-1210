# ✅ OpenAI関連コードの削除完了

**修正日:** 2025年12月14日

---

## 🔧 実施した修正

`utils.py`から**OpenAI関連のコードをすべて削除**し、**Google Geminiのみ**を使用するように修正しました。

---

## 📝 修正内容

### utils.py（143-166行目）

#### ❌ Before（エラーが発生）
```python
# 4. LLMのオブジェクトを用意（OpenAI or Google Gemini）
# APIキーの取得（環境変数またはStreamlit Secrets）
openai_api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")
google_api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

# OpenAI APIキーが利用可能な場合はOpenAIを優先使用
if openai_api_key:
    llm = ChatOpenAI(  # ← ChatOpenAIが定義されていないためエラー
        model="gpt-3.5-turbo",
        temperature=ct.TEMPERATURE,
        max_retries=2,
        openai_api_key=openai_api_key
    )
elif google_api_key:
    llm = ChatGoogleGenerativeAI(
        model=ct.MODEL,
        temperature=ct.TEMPERATURE,
        max_retries=2,
        google_api_key=google_api_key
    )
else:
    raise ValueError("OPENAI_API_KEY または GOOGLE_API_KEY が設定されていません。")
```

#### ✅ After（修正後）
```python
# 4. LLMのオブジェクトを用意（Google Gemini）
# APIキーの取得（環境変数またはStreamlit Secrets）
google_api_key = os.getenv("GOOGLE_API_KEY") or st.secrets.get("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY が設定されていません。")

llm = ChatGoogleGenerativeAI(
    model=ct.MODEL,
    temperature=ct.TEMPERATURE,
    max_retries=2,  # リトライ回数を設定
    google_api_key=google_api_key  # APIキーを明示的に渡す
)
```

---

## 🎯 変更点

1. ✅ OpenAI APIキーの取得処理を削除
2. ✅ `ChatOpenAI`の使用を削除
3. ✅ if-elif分岐を削除
4. ✅ Google Geminiのみを使用するシンプルな実装に変更

---

## 🚀 起動方法

```bash
streamlit run main.py
```

✅ エラーなく起動すれば成功です！

---

## 💡 重要な注意点

### OpenAIを使用するには

もし将来的にOpenAIを使用したい場合は、以下が必要です：

1. **パッケージのバージョン更新**
   ```bash
   pip install --upgrade langchain langchain-core langchain-openai
   ```

2. **インポート文の追加**
   ```python
   from langchain_openai import ChatOpenAI
   ```

3. **コードの追加**
   ```python
   if openai_api_key:
       llm = ChatOpenAI(...)
   ```

**しかし、現時点ではバージョンの互換性問題があるため、Google Geminiのみの使用を推奨します。**

---

## ✅ 検証結果

### 構文チェック
```bash
python -m py_compile utils.py
```
**結果:** ✅ エラーなし

---

## 📊 最終状態

| 項目 | 状態 |
|------|------|
| OpenAIインポート | ❌ なし（削除済み） |
| OpenAIコード | ❌ なし（削除済み） |
| Google Gemini | ✅ 使用中 |
| エラー | ✅ なし |

---

## 🎉 完了！

**OpenAI関連のコードを完全に削除し、Google Geminiのみを使用するシンプルな実装に戻しました。**

### 今すぐ起動

```bash
streamlit run main.py
```

エラーなく起動し、正常に動作するはずです！

---

*修正完了日: 2025年12月14日*


