import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

# 1. ページ設定
st.set_page_config(page_title="Concept Mapper", layout="wide")

st.title("🎓 自己調整学習支援：概念マップ生成器")
st.caption("用語の関係性を入力して、スキーマを可視化しましょう。")

# 2. サイドバーで入力を受け付ける
with st.sidebar:
    st.header("エディタ")
    st.write("`A -> B` の形式で関係を入力してください。")
    
    # サンプル入力を初期値に設定
    default_data = """自己調整学習 -> メタ認知
自己調整学習 -> 学習戦略
自己調整学習 -> 動機づけ
メタ認知 -> モニタリング
メタ認知 -> コントロール"""
    
    graph_input = st.text_area("関係性の定義", value=default_data, height=300)

# 3. 描画処理
if graph_input:
    # GraphvizのDOT言語形式に整形
    # ユーザーの入力を1行ずつ読み込み、全体を 'digraph { ... }' で囲む
    dot_code = "digraph {\n"
    dot_code += "  node [fontname='MS Gothic', shape=box, style=filled, fillcolor='#E1F5FE'];\n"
    dot_code += "  edge [fontname='MS Gothic'];\n"
    dot_code += graph_input
    dot_code += "\n}"

    # メインエリアに図を表示
    st.subheader("現在の理解の構造（スキーマ）")
    st.graphviz_chart(dot_code)

    # 4. 教育的アドバイス（メタ認知の促進）
    st.divider()
    st.info("💡 **セルフモニタリングのヒント**: 孤立している用語はありませんか？ 矢印の向きは正しいですか？")
