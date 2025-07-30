import streamlit as st
from pandas import read_csv
from PIL import Image

st.set_page_config(layout="wide")
st.title("The best Company")
st.write('''A team of IT individuals works collaboratively to develop, maintain, and support technology systems.
They specialize in areas like software development, cybersecurity, networking, and data management.
Each member brings unique technical skills and problem-solving abilities to the group.
Together, they ensure smooth operation of digital infrastructure and innovate solutions.
Effective communication and teamwork are key to their success in dynamic IT environments.
''')
st.header("Our Team")
col1,epm1,col2,emp2,col3=st.columns([1,0.3,1,0.3,1])

df=read_csv("data.csv",sep=",")
angle=270

with col1:
    for i,j in df[:4].iterrows():
        st.header(j["first name"]+j["last name"])
        st.write(j["role"])
        used_img=("images/"+j["image"])
        image=Image.open(used_img)
        res=image.rotate(angle,expand=True)
        st.image(res)

with col2:
    for i,j in df[5:8].iterrows():
        st.header(j["first name"]+j["last name"])
        st.write(j["role"])
        used_img = ("images/" + j["image"])
        image = Image.open(used_img)
        res = image.rotate(angle, expand=True)
        st.image(res)

with col3:
    for i,j in df[8:].iterrows():
        st.header(j["first name"]+j["last name"])
        st.write(j["role"])
        used_img = ("images/" + j["image"])
        image = Image.open(used_img)
        res = image.rotate(angle, expand=True)
        st.image(res)
