eamlit as st
import random

# ページの設定
st.set_page_config(
    page_title="オモコロチャンネル 終了画面ガチャ",
    page_icon="🎰",
    layout="centered"
)

# --- スタイリッシュなカスタムデザイン（CSS）の適用 ---
st.markdown("""
<style>
    .stApp {
        background-color: #0f111a;
        color: #e3e6ed;
    }
    .main-title {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        text-align: center;
        background: linear-gradient(45deg, #ff4b4b, #ff7676);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        text-align: center;
        color: #8892b0;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .question-box {
        background-color: #1e2235;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        border: 1px solid #2d334d;
        margin-bottom: 1.5rem;
        animation: fadeIn 0.4s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .result-text {
        font-size: 3rem !important;
        font-weight: 900 !important;
        text-align: center;
        color: #00ffcc;
        text-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
        padding: 1.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# タイトル表示
st.markdown('<p class="main-title">🎰 ENDING SCREEN GACHA</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">オモコロチャンネル 終了画面ガチャ（2025.05.02〜2026.04.29最新版データモデル）</p>', unsafe_allow_html=True)

# --- セッション状態（記憶）の初期化 ---
if "step" not in st.session_state:
    st.session_state.step = 1
if "has_main" not in st.session_state:
    st.session_state.has_main = None
if "main_person" not in st.session_state:
    st.session_state.main_person = "なし"
if "video_type" not in st.session_state:
    st.session_state.video_type = None
if "has_absent" not in st.session_state:
    st.session_state.has_absent = None
if "absent_person" not in st.session_state:
    st.session_state.absent_person = "なし"
if "winner_person" not in st.session_state:
    st.session_state.winner_person = "なし"

# 最初からやり直すボタン
if st.session_state.step > 1:
    col1, col2 = st.columns([6, 2])
    with col2:
        if st.button("🔄 最初からやり直す", use_container_width=True):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()

# --- 各ステップの一問一答処理 ---

# 【Q1. 主演者の有無】
if st.session_state.step == 1:
    with st.container():
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("### Q1. 動画に明確な「主演者（主役）」はいますか？")
        has_main = st.radio("", ["なし", "あり"], horizontal=True, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("次へ進む ➡️", use_container_width=True, type="primary"):
            st.session_state.has_main = has_main
            st.session_state.step = 1.5 if has_main == "あり" else 2
            st.rerun()

# 【Q1-Sub. 主演者の選択】
elif st.session_state.step == 1.5:
    with st.container():
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("### Q1-Sub. 主演者は誰ですか？")
        main_person = st.selectbox("", ["永田", "原宿", "加藤", "ARuFa", "恐山"], label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("条件を確定する ➡️", use_container_width=True, type="primary"):
            st.session_state.main_person = main_person
            st.session_state.step = 5
            st.rerun()

# 【Q2. 動画の形式】
elif st.session_state.step == 2:
    with st.container():
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("### Q2. 動画の形式はどちらですか？")
        video_type = st.radio("", ["非対戦形式", "対戦形式（対決・クイズ・ゲームなど）"], horizontal=True, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("次へ進む ➡️", use_container_width=True, type="primary"):
            st.session_state.video_type = video_type
            st.session_state.step = 3
            st.rerun()

# 【Q3. 不在者の有無】
elif st.session_state.step == 3:
    with st.container():
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("### Q3. 動画を欠席しているメンバー（不在者）はいますか？")
        has_absent = st.radio("", ["なし", "あり"], horizontal=True, label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("次へ進む ➡️", use_container_width=True, type="primary"):
            st.session_state.has_absent = has_absent
            if has_absent == "あり":
                st.session_state.step = 3.5
            elif st.session_state.video_type == "対戦形式（対決・クイズ・ゲームなど）":
                st.session_state.step = 4
            else:
                st.session_state.step = 5
            st.rerun()

# 【Q3-Sub. 不在者の選択】
elif st.session_state.step == 3.5:
    with st.container():
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("### Q3-Sub. 不在者は誰ですか？")
        absent_person = st.selectbox("", ["永田", "原宿", "加藤", "ARuFa", "恐山"], label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("条件を確定する ➡️", use_container_width=True, type="primary"):
            st.session_state.absent_person = absent_person
            if st.session_state.video_type == "対戦形式（対決・クイズ・ゲームなど）":
                st.session_state.step = 4  # 対戦形式なら不在者アリでも優勝者選択へ
            else:
                st.session_state.step = 5
            st.rerun()

# 【Q4. 優勝者の選択】
elif st.session_state.step == 4:
    with st.container():
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown("### Q4. 優勝者は誰ですか？")
        winner_person = st.selectbox("", ["なし", "永田", "原宿", "加藤", "ARuFa", "恐山"], label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        if st.button("条件を確定する ➡️", use_container_width=True, type="primary"):
            st.session_state.winner_person = winner_person
            st.session_state.step = 5
            st.rerun()

# --- 【ステップ5: ガチャ画面（提出データに基づく厳密な確率計算）】 ---
elif st.session_state.step == 5:
    has_main = st.session_state.has_main
    main_person = st.session_state.main_person
    video_type = st.session_state.video_type
    has_absent = st.session_state.has_absent
    absent_person = st.session_state.absent_person
    winner_person = st.session_state.winner_person

    # 確率を格納する辞書
    prediction = {}

    # 共通関数：特定ルートの「空白」内訳を確率辞書にブレンド加算する
    def add_blank_distribution(target_dict, total_pct, distribution):
        for item, item_ratio in distribution.items():
            target_dict[item] = target_dict.get(item, 0.0) + (total_pct * (item_ratio / 100.0))

    # 1. 主演エンド（最優先）
    if has_main == "あり":
        if main_person == "永田": prediction = {"永田ガチャ": 100.0}
        elif main_person == "原宿": prediction = {"あったけぇ金": 100.0}
        elif main_person == "加藤": prediction = {"電脳チャイナパトロール": 100.0}
        elif main_person == "ARuFa": prediction = {"プライドの高いおじさん": 100.0}
        elif main_person == "恐山": prediction = {"なにがあるのうた": 100.0}

    # 2. 対戦形式かつ不在者なし
    elif video_type == "対戦形式（対決・クイズ・ゲームなど）" and has_absent == "なし":
        # ベースの「空白」と「特殊」の内訳
        blank_dist = {"ふとやるコーナー": 40, "なにがあるのうた": 25, "石モッパン": 10, "ピタゴラ": 5, "低評価博士": 5, "永田ガチャ": 5, "キュートペット永田くん": 5, "電脳チャイナパトロール": 5}
        
        if winner_person != "なし":
            # 「優勝者」ルート（36.46%）
            p_route = 36.46
            if winner_person == "永田":
                p_label = 28.0
                prediction["永田ガチャ"] = p_route * (p_label / 100.0) * 0.1429
                prediction["低評価博士"] = p_route * (p_label / 100.0) * 0.4286
                prediction["高評価博士"] = p_route * (p_label / 100.0) * 0.1429
                prediction["チャンネル登録体操"] = p_route * (p_label / 100.0) * 0.2857
            elif winner_person == "原宿":
                p_label = 50.0
                prediction["しょん蛸別館"] = p_route * (p_label / 100.0) * 0.75
                prediction["石モッパン"] = p_route * (p_label / 100.0) * 0.25
            elif winner_person == "加藤":
                p_label = 42.31
                prediction["電脳チャイナパトロール"] = p_route * (p_label / 100.0) * 1.0
            elif winner_person == "ARuFa":
                p_label = 42.11
                prediction["プライドの高いおじさん"] = p_route * (p_label / 100.0) * 1.0
            elif winner_person == "恐山":
                p_label = 35.0
                prediction["なにがあるのうた"] = p_route * (p_label / 100.0) * 0.5714
                prediction["ピタゴラ"] = p_route * (p_label / 100.0) * 0.1429
            
            # ラベルが適用されなかった残り（72%〜50%等）は、本来の「空白」と「特殊」の比率(20.83 : 28.13)で分ける
            p_remain = p_route * ((100.0 - p_label) / 100.0)
            ratio_sum = 20.83 + 28.13
            p_remain_blank = p_remain * (20.83 / ratio_sum)
            p_remain_special = p_remain * (28.13 / ratio_sum)
            
            add_blank_distribution(prediction, p_remain_blank, blank_dist)
            prediction["特殊（画面なし）"] = prediction.get("特殊（画面なし）", 0.0) + p_remain_special
            
            # 独立した本来の「空白(20.83%)」「特殊(28.13%)」枠をそのまま足す（分母を100に合わせる調整）
            # 優勝者判定が外れた通常確率分を上乗せ
            add_blank_distribution(prediction, 20.83 * (100 - p_route)/100, blank_dist)
            prediction["特殊（画面なし）"] = prediction.get("特殊（画面なし）", 0.0) + (28.13 * (100 - p_route)/100)
        else:
            # 優勝者なし、あるいは特定材料なしの場合
            add_blank_distribution(prediction, 20.83 + 15.63, blank_dist) # 空白と優勝不発枠の統合
            prediction["特殊（画面なし）"] = 28.13 + 35.41

    # 3. 对戦形式かつ不在あり
    elif video_type == "対戦形式（対決・クイズ・ゲームなど）" and has_absent == "あり":
        p_winner_route = 17.86
        p_absent_route = 67.86
        
        # 3-A. 優勝者判定のブレンド
        if winner_person == "永田":
            prediction["永田ガチャ"] = prediction.get("永田ガチャ", 0.0) + (p_winner_route * 0.3333 * 0.50)
            prediction["低評価博士"] = prediction.get("低評価博士", 0.0) + (p_winner_route * 0.3333 * 0.25)
            prediction["チャンネル登録体操"] = prediction.get("チャンネル登録体操", 0.0) + (p_winner_route * 0.3333 * 0.25)
        elif winner_person == "原宿":
            prediction["しょん蛸別館"] = prediction.get("しょん蛸別館", 0.0) + (p_winner_route * 0.90 * 0.50)
            prediction["石モッパン"] = prediction.get("石モッパン", 0.0) + (p_winner_route * 0.90 * 0.50)
        elif winner_person == "恐山":
            prediction["ピタゴラ"] = prediction.get("ピタゴラ", 0.0) + (p_winner_route * 0.25 * 0.50)
            prediction["なにがあるのうた"] = prediction.get("なにがあるのうた", 0.0) + (p_winner_route * 0.25 * 0.50)
            
        # 3-B. 不在者判定のブレンド
        if absent_person == "永田":
            prediction["永田ガチャ"] = prediction.get("永田ガチャ", 0.0) + (p_absent_route * 0.50 * 0.80)
            prediction["キュートペット永田くん"] = prediction.get("キュートペット永田くん", 0.0) + (p_absent_route * 0.50 * 0.20)
        elif absent_person == "原宿":
            prediction["しょん蛸別館"] = prediction.get("しょん蛸別館", 0.0) + (p_absent_route * 0.90 * 0.63)
            prediction["あったけぇ金"] = prediction.get("あったけぇ金", 0.0) + (p_absent_route * 0.90 * 0.25)
            prediction["石モッパン"] = prediction.get("石モッパン", 0.0) + (p_absent_route * 0.90 * 0.12)
        elif absent_person == "加藤":
            prediction["電脳チャイナパトロール"] = prediction.get("電脳チャイナパトロール", 0.0) + (p_absent_route * 0.50 * 1.0)
        elif absent_person == "ARuFa":
            prediction["プライドの高いおじさん"] = prediction.get("プライドの高いおじさん", 0.0) + (p_absent_route * 0.5714 * 1.0)
        elif absent_person == "恐山":
            prediction["なにがあるのうた"] = prediction.get("なにがあるのうた", 0.0) + (p_absent_route * 1.0 * 0.80)
            prediction["不快"] = prediction.get("不快", 0.0) + (p_absent_route * 1.0 * 0.20)

        # 3-C. 固定の「空白（3.57%）」「特殊（3.57%）」および不発ラベル分の補完
        prediction["ふとやるコーナー"] = prediction.get("ふとやるコーナー", 0.0) + 3.57 + (p_winner_route * 0.2) # 不発充当
        prediction["特殊（画面なし）"] = prediction.get("特殊（画面なし）", 0.0) + 3.57 + (p_absent_route * 0.1)

    # 4. 非対戦形式かつ不在者あり
    elif video_type == "非対戦形式" and has_absent == "あり":
        p_absent_route = 62.50
        # 不在者ラベルの処理
        if absent_person == "永田":
            prediction["永田ガチャ"] = p_absent_route * 0.80
            prediction["キュートペット永田くん"] = p_absent_route * 0.20
        elif absent_person == "原宿":
            prediction["あったけぇ金"] = p_absent_route * 0.40 * 0.50
            prediction["石モッパン"] = p_absent_route * 0.40 * 0.50
            # ラベル不適用分(60%)を空白・特殊に配分
            add_blank_distribution(prediction, p_absent_route * 0.60 * 0.66, {"なにがあるのうた": 70, "チャンネル登録体操": 30})
            prediction["特殊（画面なし）"] = p_absent_route * 0.60 * 0.34
        elif absent_person == "加藤":
            prediction["電脳チャイナパトロール"] = p_absent_route * 1.0
        elif absent_person == "ARuFa":
            prediction["プライドの高いおじさん"] = p_absent_route * 0.6667
            add_blank_distribution(prediction, p_absent_route * 0.3333 * 0.66, {"なにがあるのうた": 70, "チャンネル登録体操": 30})
            prediction["特殊（画面なし）"] = p_absent_route * 0.3333 * 0.34
        elif absent_person == "恐山":
            prediction["なにがあるのうた"] = p_absent_route * 1.0
            
        # 本来の「空白(25%)」「特殊(12.50%)」枠の加算
        add_blank_distribution(prediction, 25.0, {"なにがあるのうた": 70, "チャンネル登録体操": 30})
        prediction["特殊（画面なし）"] = prediction.get("特殊（画面なし）", 0.0) + 12.50

    # 5. 非対戦かつ不在者なし
    else:
        # 空白(63.72%)の内訳
        blank_dist_non_combat = {"なにがあるのうた": 37.50, "ふとやるコーナー": 22.22, "石モッパン": 6.94, "あったけぇ金": 5.56, "高評価博士": 5.56, "電脳チャイナパトロール": 5.56, "ピタゴラ": 4.17, "キュートペット永田くん": 2.78, "不快": 2.78}
        add_blank_distribution(prediction, 63.72, blank_dist_non_combat)
        # 特殊(21.24%)および残余の100%調整用
        prediction["特殊（画面なし）"] = 100.0 - sum(prediction.values())

    # --- 画面描画 ---
    with st.container():
        st.markdown('<div class="question-box" style="text-align: center;">', unsafe_allow_html=True)
        st.markdown("### 📊 精密データ分析完了")
        st.write("2025/5/2〜2026/4/29の記録に基づき、終了画面をシミュレートします。")
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔮 ガチャを引く（運命の決定）", type="primary", use_container_width=True):
        # 確率データの正規化（合計を100%にする安全処理）
        total_w = sum(prediction.values())
        candidates = list(prediction.keys())
        weights = [w / total_w for w in prediction.values()]
        
        result_ending = random.choices(candidates, weights=weights, k=1)[0]
        
        st.balloons()
        st.markdown("<p class='result-text'>🌟 " + result_ending + " 🌟</p>", unsafe_allow_html=True)
        
        st.subheader("💡 蓄積データに基づく考察")
        if "特殊" in result_ending:
            st.warning("この条件下のデータでは、固有の終了画面を出さずに動画を終える「特殊エンド」の確率が高くなっています。")
        elif "なにがあるのうた" in result_ending or "ふとやるコーナー" in result_ending:
            st.info(f"空白期・非対戦時の定番である『{result_ending}』が選ばれました。チャンネルの王道の空気感です。")
        else:
            st.success(f"条件に合致した固有ラベル『{result_ending}』が見事に的中しました！集計データが示す通りの美しい結果です。")
