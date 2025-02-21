import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🧠")
st.title("Growth Mindset Project")
st.header("🧠Welcome to the Growth Mindset Challenge")
st.write("This interactive web app is designed to inspire and encourage a growth mindset. Explore, learn, and embrace challenges as opportunities to grow.💡")

st.header("🌱Quote Of The Day is")
st.write("Every challenge is an opportunity to grow. Embrace the struggle, learn from mistakes, and keep pushing forward!🌱")

st.header("What's Your Today Challange❓")
user_input = st.text_input("Enter your challenge for today")

if user_input:
    st.success(f"Your challenge for today is: {user_input}.Believe in your potential—every step you take brings you closer to success!🚀")
else:
    st.warning("Enter your challenge for today❓")

st.header("Reflect On Your Learning")
reflection = st.text_area("What did you learn today❓")

if reflection:
    st.success(f"Great💪 Reflection: {reflection} ")
else :
    st.info("Your past mistakes are not failures—they are lessons that shape your future success. Learn, grow, and keep moving forward! 🔥")
    

st.header("🌟Celebrate Your Achievements")
achievement = st.text_area("What did you achieve today❓")

if achievement:
    st.success(f"Congratulations! You achieved: {achievement} ")

else :
    st.info("Celebrate your progress, no matter how small. Every step you take is a step closer to your goals!🎉")

st.write("_ _ _")
st.write("Believe in yourself, and youre already halfway there. 💡🚀 Trust your journey, embrace the challenges, and keep growing!")
st.write("©️ 2024 Growth Mindset Challenge. All Rights Reserved.Created By Muhammad Usaid Khan")