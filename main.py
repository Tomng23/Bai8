import streamlit as st

col1, col2, col3, col4, col5 = st.columns(5)
col6, col7 = st.columns([2,1])

with col1:
    b1 = st.button('Con Mèo')
with col2:
    b2 = st.button('Con Chó')
with col3:
    b3 = st.button('Con Gà')
with col4:
    b4 = st.button('Con Bò')
with col5:
    b5 = st.button('Con Lợn')   

if b1:
    with col6:
        st.write('Audio')
        audio = open('audio/cat_audio.mp3','rb')
        st.audio(audio, format='audio.mp3')

        st.write('Video')
        video = 'https://www.youtube.com/watch?v=8RlnjSbyBpk'
        st.video(video, format='video/mp4')
    with col7:
        image = 'image/cat.png'
        st.image(image, caption='*Con mèo*')
        st.write('Mèo dành khoảng 70% cuộc đời để ngủ. Đó là khoảng 13–16 giờ mỗi ngày!')
if b2:
    with col6:
        st.write('Audio')
        audio = open('audio/dog_audio.mp3','rb')
        st.audio(audio, format='audio.mp3')

        st.write('Video')
        video = 'https://www.youtube.com/watch?v=nRBwxQ_xXe8'
        st.video(video, format='video/mp4')
    with col7:
        image = 'image/dog.png'
        st.image(image, caption='*Con Chó*')
        st.write('Khứu giác của chó tốt hơn ít nhất 40 lần so với con người. Chúng thậm chí có thể phát hiện bệnh tật!')

if b3:
    with col6:
        st.write('Audio')
        audio = open('audio/chicken_audio.mp3','rb')
        st.audio(audio, format='audio.mp3')

        st.write('Video')
        video = 'https://www.youtube.com/watch?v=bCsBGLfUbZg'
        st.video(video, format='video/mp4')
    with col7:
        image = 'image/chicken.png'
        st.image(image, caption='*Con Gà*')
        st.write('Gà có khả năng nhận diện hơn 100 khuôn mặt khác nhau của người hoặc động vật.')

if b4:
    with col6:
        st.write('Audio')
        audio = open('audio/cow_audio.mp3','rb')
        st.audio(audio, format='audio.mp3')

        st.write('Video')
        video = 'https://www.youtube.com/watch?v=KjmuBo8xoCU'
        st.video(video, format='video/mp4')
    with col7:
        image = 'image/cow.png'
        st.image(image, caption='*Con Bò*')
        st.write('Bò có những người bạn thân và sẽ bị căng thẳng khi bị tách khỏi nhau.')

if b5:
    with col6:
        st.write('Audio')
        audio = open('audio/pig_audio.mp3','rb')
        st.audio(audio, format='audio.mp3')

        st.write('Video')
        video = 'https://www.youtube.com/watch?v=iUbTO-VODX0'
        st.video(video, format='video/mp4')
    with col7:
        image = 'image/pig.png'
        st.image(image, caption='*Con Lợn*')
        st.write('Lợn thông minh hơn chó và có thể học cách chơi trò chơi điện tử!')
        