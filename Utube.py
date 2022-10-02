from logging import PlaceHolder
import streamlit as st

from pytube import YouTube
url = st.text_input('Utube', placeholder="Enter your url here")

if url:
    try:
        yt = YouTube(url)
        st.text("Video title")
        st.write(yt.title)
        streams1=yt.streams
        audio = st.checkbox('only audio',key="disabled")
        if audio:
            streams1=streams1.filter(only_audio=True)
        videoFormat = st.selectbox(
            'Select video formart',
            ('3gpp', 'mp4', 'webm'),
            disabled=st.session_state.disabled)
        if videoFormat:
            streams1=streams1.filter(file_extension=videoFormat)
        streams=[]
        for i in (streams1):
            a=f"{i}"
            a=a[9:-1]
            streams.append(a)

       
        option = st.selectbox(
            "Select stream",
            streams,
            )
        if option:
            if st.button("download"):
                b=option.split(" ")
                c=b[0].replace("itag=",'')
                c=int(c.replace('"',''))
                stream = yt.streams.get_by_itag(c)
                with st.spinner('Downloading...'):
                    stream.download()
                st.success("File downloaded")
    except:
        st.write("Enter valid url")

