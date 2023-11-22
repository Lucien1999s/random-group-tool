import streamlit as st
import random
import time
from pygame import mixer

MEMBERS = "Lucien, Sam, Patty, Henry, Johnny, Wendy, Mason, Aki"

def play_audio():
    mixer.init()
    mixer.music.load("fall.mp3")
    mixer.music.play()

def assign_members_to_themes(members, themes):
    """Assign members to themes"""
    if len(themes) > len(members):
        return "錯誤，主題的數量不能比成員數量多！"
    num_members_per_theme = len(members) // len(themes)
    theme_dict = {}
    random.shuffle(members)
    for i in range(len(themes)):
        theme_dict[themes[i]] = members[i*num_members_per_theme : (i+1)*num_members_per_theme]
    remaining_members = members[len(themes)*num_members_per_theme:]
    random.shuffle(remaining_members)
    for i, member in enumerate(remaining_members):
        theme_dict[themes[i]].append(member)
    return theme_dict


def interface():
    """Show streamlit interface"""
    
    st.markdown("<h1 style='text-align: center; color: orange;'>🎁 聖誕禮物主題分配 🎁</h1>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 20px;'>參與人員</div>", unsafe_allow_html=True)

    members = st.text_area("", value=MEMBERS)
    st.markdown("<div style='font-size: 20px;'>主題名稱(每行一個主題)</div>", unsafe_allow_html=True)
    themes_input = st.text_area("")

    if st.button("隨機分組"):
        if not themes_input:
            st.error("Man ~ you didn't 輸入主題")
        else:
            themes = themes_input.split("\n")
            members = members.split(",")
            play_audio()
            gif_placeholder = st.empty()
            gif_placeholder.image("angry-birds.gif")
            time.sleep(2)
            gif_placeholder.empty()
            st.table(assign_members_to_themes(members=members, themes=themes))


if __name__ == "__main__":
    interface()

