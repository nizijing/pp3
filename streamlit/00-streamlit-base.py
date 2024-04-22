import streamlit as st

st.title("Streamlist Title")

st.header("This is header")
st.subheader("This is a subheader")

st.text("Hello Streamlit")

st.markdown("### This is a Markdown")

st.success("success")
st.info("info")
st.warning("warning")
st.error("error")
st.exception("NameError('exceptrion error')")

st.help(range)

# writing Text/Super Fxn
st.write("Text with write")
st.write(range(10))

@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())


# Image
# from PIL import Image
# img = Image.open('image.jpeg')
# st.image(img, width=300,caption="Simple Image")

# video
# vid_file = open("video.mp4", 'rb').raed()
# st.video(vid_file)

# mp3
# audio_file = open("music.mp3", "rb").read()
# st.audio(audio_file, format='audio/mp3')

if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")


status = st.radio("what is you status", ("active", "inactive"))
if status == 'active':
    st.success("you are active")
else:
    st.warning("inactive")


color = st.selectbox("what color you like", ('yellow', 'blue', 'green'))
st.write("you like ", color)


with st.container():
    cols1,cols2 = st.columns(2)
    with cols1.container():
        color2 = st.selectbox("what color you like2", ('yellow', 'blue', 'green'))
    with cols2.container():
        st.write("you like ", color2)


anaimals = st.multiselect("what analimal you like", ('dog', 'cat', 'bird'))
st.write("you like {}".format(anaimals))


level = st.slider("what is you level", 1, 5)


st.button("Simple Button")
if st.button("About"):
    st.text("you click about")


name = st.text_input("Enter you name", "Type Here...")
if st.button("submit"):
    st.success(name.title())


message = st.text_input("Enter you message", "Type Here...")
if st.button("submit message"):
    st.success(message)


import datetime
today = st.date_input("Today is", datetime.datetime.now())
the_time = st.time_input("The time is", datetime.time())


st.text("Display JSON")
st.json({"name": "zijing", "high": "170"})


st.text("Display code")
st.code("import numpy as np")

with st.echo():
    import pandas as pd
    df = pd.DataFrame()


# Progress Bar
import time
my_bar = st.progress(0)
for i in range(10):
    my_bar.progress(i + 1)


# Spinner
with st.spinner("Waiting .."):
    time.sleep(1)
st.success("Finished!")


st.balloons()


st.sidebar.header("About")
st.sidebar.text("This is sidebar text")


st.pyplot()
st.dataframe(df)
st.table(df)

