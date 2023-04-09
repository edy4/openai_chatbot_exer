# section3 Exercise

import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# st.session_stateを使いメッセージのやり取りを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role":"system", "content":st.secrets.AppSetting.chatbot_setting}
    ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role":"user", "content":st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        temperature = 1.2
    )

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""



# UIの構築
st.title("My AI アシスタントゥ")
st.write("ChatGPT APIを使ったチャットボットかも")

user_input = st.text_input("メッセージを入れる？", key = "user_input", on_change = communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):
        speaker = "😄"
        if message["role"] == "assistant":
            speaker = "🤖"

        st.write(speaker + ": " + message["content"])
