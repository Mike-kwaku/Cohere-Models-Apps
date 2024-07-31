import cohere
import os
import streamlit as st

co = cohere.Client(os.environ["COHERE_API_KEY"])
cohere_model='command-r'

def generate_ans(qstn):

  response = co.generate(model=cohere_model,prompt=qstn)

  bot_ans = response.generations[0].text
  bot_ans = bot_ans.replace("\n\n--","").replace("\n--","").strip()

  return bot_answer


# The front end code starts here

st.title("Question & answer bot with Cohere")

st.write("Enter your question here: [Example: Who is the PM of UK] ")

qstn_input = st.text_input("Question", key = "qstn_input")

form = st.form("my form")
with form:     
 generate_button = st.form_submit_button("Answer Question")

 if generate_button:
    if qstn_input == "":
      st.error("Question field cannot be blank")
    else:
      my_bar = st.progress(0.05)
      st.subheader("Answer from bot:")

      for i in range(1):
          st.markdown("""---""")
          ans = generate_ans(qstn_input)
          st.markdown("##### " + ans)
          st.write(ans)
          my_bar.progress((i+1)/1)

