import streamlit as st
import random

def randstr(length):
    return ''.join([chr(random.randint(12354, 12435)) for _ in range(length)])


st.title('単語ランダム生成')

number = st.number_input(label='何文字の単語を生成しますか？', value=3)

if st.button('生成'):
    st.write(randstr(number))
