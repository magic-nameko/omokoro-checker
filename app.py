import streamlit as st
import pandas as pd

# ページの設定
st.set_page_config(
    page_title="オモコロチャンネル 終了画面予測シミュレーター",
    page_icon="📺",
    layout="centered"
)

# タイトル・導入
st.title("📺 オモコロ終了画面予測シミュレーター")
st.markdown("""
オモコロチャンネル累計1,200本以上の動画データから導き出された**「終了画面推測の手引き」**に基づき、
本日の動画の条件から終了画面の発生確率をロジカルにシミュレートします。
""")

st.divider()

# --- 入力セクション ---
st.header("1. 動画の条件を入力")

# ① 主演者の有無
has_main = st.radio("Q1. 動画に明確な「主演者（主役）」はいますか？", ["なし", "あり"], horizontal=True)
main_person = "なし"
if has_main == "あり":
    main_person = st.selectbox("主演者は誰ですか？", ["永田", "原宿", "加藤", "ARuFa", "恐山"])

st.write("")

# ② 対戦形式か
video_type = st.radio("Q2. 動画の形式はどちらですか？", ["非対戦形式", "対戦形式（対決・クイズ・ゲームなど）"], horizontal=True)

st.write("")

# ③ 不在者の有無
has_absent = st.radio("Q3. 動画を欠席しているレギュラーメンバー（不在者）はいますか？", ["なし", "あり"], horizontal=True)
absent_person = "なし"
if has_absent == "あり":
    absent_person = st.selectbox("不在者は誰ですか？", ["永田", "原宿", "加藤", "ARuFa", "恐山"])

st.write("")

# ④ 優勝者（対戦形式の場合のみ）
winner_person = "なし"
if video_type == "対戦形式（対決・クイズ・ゲームなど）":
    has_winner = st.radio("Q4. 優勝者は決まりましたか？（複数人の場合は最も優先度の高い人物を選択）", ["なし", "あり"], horizontal=True)
    if has_winner == "あり":
        winner_person = st.selectbox("優勝者は誰ですか？（優先度：原宿 ＞ 永田・恐山 ＞ 加藤・ARuFa）", ["永田", "原宿", "加藤", "ARuFa", "恐山"])

st.divider()

# --- ロジック計算セクション ---
# 結果を格納する辞書 {終了画面名: 確率%}
prediction = {}

if has_main == "あり":
    # 経路①：主演者関連
    if main_person == "永田":
        prediction = {"永田ガチャ": 50, "キュートペット永田くん": 30, "空白（その他ランダム）": 20}
    elif main_person == "原宿":
        prediction = {"あったけぇ金": 50, "しょん蛸別館": 30, "空白（その他ランダム）": 20}
    elif main_person == "加藤":
        prediction = {"電脳チャイナパトロール": 80, "空白（その他ランダム）": 20}
    elif main_person == "ARuFa":
        prediction = {"プライドの高いおじさん": 80, "空白（その他ランダム）": 20}
    elif main_person == "恐山":
        prediction = {"なにがあるのうた": 80, "空白（その他ランダム）": 20}

elif video_type == "対戦形式（対決・クイズ・ゲームなど）":
    if has_absent == "あり":
        # 経路②：対戦形式かつ不在者あり（最優先）
        if absent_person == "永田":
            prediction = {"永田ガチャ": 35, "キュートペット永田くん": 15, "空白（その他ランダム）": 30, "特殊（画面なし・エンディング固定）": 20}
        elif absent_person == "原宿":
            prediction = {"しょん蛸別館": 90, "特殊（画面なし・告知など）": 10}
        elif absent_person == "加藤":
            prediction = {"電脳チャイナパトロール": 50, "空白（その他ランダム）": 30, "特殊（画面なし・エンディング固定）": 20}
        elif absent_person == "ARuFa":
            prediction = {"プライドの高いおじさん": 55, "空白（その他ランダム）": 25, "特殊（画面なし・エンディング固定）": 20}
        elif absent_person == "恐山":
            prediction = {"なにがあるのうた": 100}
    else:
        # 経路③：対戦形式かつ不在者なし
        if winner_person == "永田":
            prediction = {"低評価博士": 15, "チャンネル登録体操": 13, "空白（その他ランダム）": 45, "特殊（画面なし）": 27}
        elif winner_person == "原宿":
            prediction = {"あったけぇ金": 50, "空白（その他ランダム）": 30, "特殊（画面なし）": 20}
        elif winner_person == "加藤":
            prediction = {"電脳チャイナパトロール": 42, "空白（その他ランダム）": 38, "特殊（画面なし）": 20}
        elif winner_person == "ARuFa":
            prediction = {"プライドの高いおじさん": 42, "空白（その他ランダム）": 38, "特殊（画面なし）": 20}
        elif winner_person == "恐山":
            prediction = {"なにがあるのうた": 35, "空白（その他ランダム）": 45, "特殊（画面なし）": 20}
        else:
            # 優勝者なしの対戦
            prediction = {"なにがあるのうた": 20, "ふとやるコーナー": 20, "空白（その他ランダム）": 30, "特殊（画面なし）": 30}

else: # 非対戦形式
    if has_absent == "あり":
        # 経路④：非対戦形式かつ不在者あり
        if absent_person == "永田":
            prediction = {"永田ガチャ": 30, "チャンネル登録体操": 20, "空白（その他ランダム）": 30, "特殊（画面なし）": 20}
        elif absent_person == "原宿":
            prediction = {"あったけぇ金": 40, "空白（その他ランダム）": 40, "特殊（画面なし）": 20}
        elif absent_person == "加藤":
            prediction = {"電脳チャイナパトロール": 100}
        elif absent_person == "ARuFa":
            prediction = {"プライドの高いおじさん": 68, "空白（その他ランダム）": 20, "特殊（画面なし）": 12}
        elif absent_person == "恐山":
            prediction = {"なにがあるのうた": 100}
    else:
        # 経路⑤：非対戦形式かつ不在者なし（完全なカオス領域）
        prediction = {
            "なにがあるのうた（空白優勢択）": 30,
            "ふとやるコーナー（空白優勢択）": 25,
            "特殊（画面なし・空気感による終了）": 40,
            "石モッパン（警戒択）": 5
        }

# --- 出力セクション ---
st.header("📊 2. 終了画面 予測結果")

# データをDataFrameに変換して降順ソート
df = pd.DataFrame(list(prediction.items()), columns=["終了画面候補", "的中確率 (%)"])
df = df.sort_values(by="的中確率 (%)", ascending=False).reset_index(drop=True)

# 最有力候補の表示
most_likely = df.iloc[0]["終了画面候補"]
most_likely_pct = df.iloc[0]["的中確率 (%)"]

st.success(f"🏆 最有力候補は **【{most_likely}】** です！（予測確率: {most_likely_pct}%）")

# 確率表の表示
st.dataframe(
    df.style.format({"的中確率 (%)": "{:.1f}%"}),
    use_container_width=True
)

# 考察コメントの自動生成
st.subheader("💡 データアナリスト（上位0.001%）の考察")
if "100%" in df.style.format({"的中確率 (%)": "{:.1f}%"}).to_string():
    st.info("データ上、この条件における終了画面はほぼ固定されています。鉄板の予想です。")
elif "空白" in most_likely or "なにがあるのうた" in most_likely or "ふとやるコーナー" in most_likely:
    st.warning("動画の秩序が崩壊している（脈絡のない）ルートです。『なにがあるのうた』か『ふとやるコーナー』、あるいは動画全体の『空気感』を察して特殊（画面なし）に張るのが玄人好みの選択です。")
elif "永田" in str(prediction.keys()) and winner_person == "永田":
    st.error("永田氏が絡む優勝ルートは、過去のデータを見ても終了画面が非常に多岐にわたるため、予測が極めて困難です。低評価博士か体操の2択が比較的安全です。")
else:
    st.info("ロジカルな規則性が働きやすい条件下にあります。フローチャートの導きを信じる価値は高いです。")
