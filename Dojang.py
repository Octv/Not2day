import streamlit as st

st.set_page_config(
    page_title="정수 인사",
    page_icon="🤖",
    layout="wide"
    # initial_sidebar_state="auto"  
)

if "counter1" not in st.session_state:
    st.session_state.counter1 = 1

if "counter2" not in st.session_state:
    st.session_state.counter2 = 2

if "counter3" not in st.session_state:
    st.session_state.counter3 = 3

button1 = st.button("카운트 1: 1부터 시작해 1씩 증가")

button2 = st.button("카운트 2: 2부터 시작해 2씩 증가")

button3 = st.button("카운트 3: 3부터 시작해 3씩 증가")

if button1:
    st.session_state.counter1 += 1

if button2:
    st.session_state.counter2 += 2

if button3:
    st.session_state.counter3 += 3

st.write("카운트 1:", st.session_state.counter1)

st.write("카운트 2:", st.session_state.counter2)

st.write("카운트 3:", st.session_state.counter3)


