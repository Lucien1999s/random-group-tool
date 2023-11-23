import streamlit as st
import random
import time

MEMBERS = "蔣志薇,袁鈺婷(Chubby),張興禹(Gini),李欣怡(Millie),劉濡慧,夏雅鈴(Reene),馬少嬪(Ivy),唐小玲(Shirley),李宛臻(Alyssa),朱映潔(阿朱),彭詩涵,胡涵云(Irene),葉峯谷,葉佳威(Wesley),楊丞碩(Owen),呂德芬(Eva),陳伊婷(Amber),王呈隆(Steven),王子禾(Eddie),黃敬淳(小米),李佳穎(Jenny),黃詩蓓(Kana),駱弘凱(Calvin),蔡亞珊(Coral),李韻晨(Zoe),吳宜臻(Lily),陳宣懿,施佩儀,徐暘甯(Iris),姜雅馨,蔡瓅萱,林子洵(Sharon),楊千儀(Ariel),陳柏任(呆呆),劉又瑋,林詣翔(小翔),林鑛(Kuang),王涵秋(Aki),吳育承,婁方貞,金志丞(Staney),温紹郁(Mark),孟令三(Sam),李家輝(火鍋),張博仲(Ben),張沛瑀(Patty),李秉翰(Henry),蔡協哲(Johnny),賴威宇(Morty),郭佩沂(Joyce),王品懿(Ivy),何瑋宸(Neil),林則廷(Lucien),洪俊翰(Keith),林哲緯(Mason),刁彥瑜(Emily),呂嘉瑋(Joe),林幸蓉(小莎),畢柏瑋(Bboy),謝文瑜(Wendy),陳為方(Henry),陳昭雄(Allan)"
THEMES = ["走進你的時間", "盲婚試愛：交換誓詞之後：第 4 季", "別被狼女所欺騙", "69 兩頭勾：影集版", "維琴河：第 5 季","橘郡豪宅：第 2 季", "從前從前謀殺案", "一切始於一見鍾情", "性愛自修室：第 4 季", "盲婚試愛：第 5 季", "盜賊之歌", "魔鬼的計謀", "亨利·休格的神奇故事", "D.P：逃兵追緝令：第 2 季", "驅魔麵館：第 2 季","下流正義：第 2 季", "慾罷不能：第 5 季", "火燒御手洗家", "獵魔士：第 3 季","認賊作爸媽", "19/20 成年初體驗", "厚片女孩的生存之道", "BASTARD！！暗黑破壞神：第 2 季", "今生也請多指教", "歡迎來到王之國", "Behind Your Touch", "Destined with You","人選之人 - 造浪者", "末日騎士", "FUBAR", "慈母殺心", "夏洛特王后：柏捷頓家族前傳","日落豪宅：第6季", "愛你的凱蒂", "最後通牒：酷兒的愛", "相撲聖域", "愛在山林間", "模仿犯", "格殺福順", "離婚律師申晟瀚", "路德探長：落日之殤","有吉弘行爆笑助攻", "太陽召喚：第2 季", "魔術師的大象", "性／生活：第2季", "一射千金：Pornhub的故事","PLUTO 冥王", "維京傳奇：英靈神殿", "安眠書店", "我們厄蕭家", "外灘探秘", "獵魔士", "雨傘學院", "愛x 死 x 機器人", "SweetTooth：鹿角男孩","我們的星球", "Formula1：飆速求生", "性愛自修室", "好想做一次", "維琴河","戀愛修課", "盲婚試愛", "下流正義", "日落豪宅", "TheCircle：美國","睡魔", "換屋假期", "戀愛大戰", "名偵探柯南：犯人・犯澤先生", "衝吧烈子：第5 季", "今際之國的闖關者 第2季", "First Love 初戀", "媽，別鬧了！", "她和她的她","村裡來了個暴走女外科", "鬼滅之刃 遊郭篇", "安雅與魔女", "那年，我們的夏天", "我沒有談的那場戀愛", "戀慕", "紙房子", "艾蜜莉在巴黎", "獵魔士", "毒梟", "俗女養成記", "天橋上的魔術師", "火神的眼淚", "鋒迴路轉：抽絲剝繭","超時空亞當計畫", "千萬別抬頭", "紅色追緝令", "緝魂", "當男人戀愛時", "無赦", "犬山記", "星期三 第二季", "紙房子 外傳", "京城生物", "安眠書店 第四季", "黑暗榮耀 第二季", "魷魚遊戲 第二季", "Sweet Home 第二季", "性／生活 第二季", "模仿犯", "母女姐妹花 第二季", "紙房子 外傳影集 柏林", "伊藤潤二狂熱：日本恐怖故事","無人島的Diva", "我的女神室友斗娜", "今夜一起為愛鼓掌", "乩身", "商魂", "非殺人小說"]


def assign_members_to_themes(members, themes):
    """Assign members to themes"""
    if len(themes) > len(members):
        return "錯誤，主題的數量不能比成員數量多！"
    num_members_per_theme = len(members) // len(themes)
    theme_dict = {}
    random.shuffle(members)
    for i in range(len(themes)):
        theme_dict[themes[i]] = members[
            i * num_members_per_theme : (i + 1) * num_members_per_theme
        ]
    remaining_members = members[len(themes) * num_members_per_theme :]
    random.shuffle(remaining_members)
    for i, member in enumerate(remaining_members):
        theme_dict[themes[i]].append(member)
    return theme_dict

def random_themes(sample_num):
    return random.sample(THEMES, sample_num)

def interface():
    """Show streamlit interface"""

    st.markdown(
        "<h1 style='text-align: center; color: orange;'>🎁 聖誕禮物主題分配 🎁</h1>",
        unsafe_allow_html=True,
    )
    st.markdown("<div style='font-size: 20px;'>參與人員</div>", unsafe_allow_html=True)

    members = st.text_area("", value=MEMBERS)

    selected_value = st.slider('填補主題數', min_value=5, max_value=20, value=10)
    if st.button("隨機填補主題"):
        st.session_state.default_value = '\n'.join(random_themes(sample_num=selected_value))

    if "default_value" not in st.session_state:
        st.session_state.default_value = ""

    st.markdown(
        "<div style='font-size: 20px;'>主題名稱(每行一個主題)</div>", unsafe_allow_html=True
    )
    themes_input = st.text_area("",value=st.session_state.default_value)

    if st.button("隨機分組"):
        if not themes_input:
            st.error("Man ~ you didn't 輸入主題")
        else:
            themes = themes_input.split("\n")
            members = members.split(",")
            gif_placeholder = st.empty()
            gif_placeholder.image("angry-birds.gif")
            time.sleep(2)
            gif_placeholder.empty()
            st.table(assign_members_to_themes(members=members, themes=themes))

if __name__ == "__main__":
    interface()
