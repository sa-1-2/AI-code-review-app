import streamlit as st
from openai import OpenAI
import os
import base64

def get_openai_respone(prompt):
    f = open('.openai_api_key.txt')
    OPENAI_API_KEY = f.read()
    client = OpenAI(api_key = OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {
                "role": "user",
                "content": "You are helpful agent and reviews code in python, provide me correct code and explain the mistakes done in the code"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content


st.header("AI code review App")
input= st.text_area("Enter your python code here: ", key="input")
submit = st.button("Generate")

if submit:
    response = get_openai_respone(input)

    st.subheader("Code Review")
    st.write("Bug Report:")
    st.write(response[response.find("1.")-1:])

    st.write("Corrected code:")
    st.write(response[response.find("```"):response.find("Mistakes")]) 


st.sidebar.markdown("<h3>If you like this app. You can follow me on</h3>", unsafe_allow_html=True)

linkedin, github,discord,m,n = st.sidebar.columns(5)
with linkedin:
    st.markdown(
        """<a href="https://www.linkedin.com/in/sanchit-singla/">
        <img src="data:image/png;base64,{}" width="40">
        </a>""".format(base64.b64encode(open("images/linkedin.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True)

with github:
    st.markdown(
        """<a href="https://github.com/sa-1-2/">
        <img src="data:image/png;base64,{}" width="40">
        </a>""".format(base64.b64encode(open("images/github.PNG", "rb").read()).decode()
        ),
        unsafe_allow_html=True)

with discord:
    st.markdown(
        """<a href="https://discordapp.com/users/753842907966079046">
        <img src="data:image/png;base64,{}" width="40">
        </a>""".format(base64.b64encode(open("images/discord.png", "rb").read()).decode()
        ),
        unsafe_allow_html=True)
   
st.sidebar.write("")
st.sidebar.write("BY: Sanchit Singla")

st.sidebar.write("")
st.sidebar.write()
email_address = "sanchitsingla1403@gmail.com"
st.sidebar.markdown("""<p>You can report Bug at Email</p><a href="mailto:{}"><img src="data:image/png;base64,{}" width="40"><p>sanchitsingla1403@gmail.com</p>
        </a>""".format(email_address, base64.b64encode(open("images/gmail.png", "rb").read()).decode()), unsafe_allow_html=True)
