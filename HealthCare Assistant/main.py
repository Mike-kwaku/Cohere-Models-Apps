import cohere 
import streamlit as st
import os
import textwrap 
import json  

# Set up Cohere client
co = cohere.Client(os.environ["COHERE_API_KEY"]) # Get your API key: https://dashboard.cohere.com/api-keys

def gen_advice(healthcare, temperature):
  """
  Generate a health advice given a healthcare topic
  Arguments:
    healthcare(str): 
    temperature(str): the Generate model `temperature` value
  Returns:
    response(str): 
  """
  prompt = f"""
Generate a healthcare advice given healthcare topic. Return the healthcare advice and without additional commentary.

## Examples
Healthcare: Digestive Health
Advice: Drink plenty of fluids (water, sports drinks, fruit juice) to keep from getting dehydrated. Avoid alcohol, caffeine, and dairy.

Healthcare: Eye Health
Advice: Exercise regularly. Use protective eyewear during activities that may be dangerous to your eyes, such as yard work, sports or home repairs.

Healthcare: Ear Health
Advice: Limit your exposure to loud noises. Wear protective headgear or earplugs when the noise gets too loud.  

Healthcare: Brain Health
Advice: Try to manage stress, focus on the present, Take a break if you need to, and take some time off to reduce stress

## Your Task
Healthcare: {healthcare }
Advice:"""

# Call the Cohere Chat endpoint
  response = co.chat( 
    message=prompt,
    model='command-r', 
    temperature=temperature,
    preamble="")
  
  return response.text

st.title("🚀 Healthcare Consult")

form = st.form(key="user_settings")
with form:
  st.write("Enter Healthcare topic [Example: Ear Infections, Depression, Digestive Problems] ")
  # User input - Healthcare
  Healthcare_input = st.text_input("Healthcare", key = "Healthcare_input")

  # Create a two-column view
  col1, col2 = st.columns(2)
  with col1:
      # User input - The number of healthcare advice to generate
      num_input = st.slider(
        "Number of advice", 
        value = 3, 
        key = "num_input", 
        min_value=1, 
        max_value=10,
        help="Choose to generate between 1 to 10 advices")
  with col2:
      # User input - The 'temperature' value representing the level of creativity
      creativity_input = st.slider(
        "Creativity", value = 0.5, 
        key = "creativity_input", 
        min_value=0.1, 
        max_value=0.9,
        help="Lower values generate more “predictable” output, higher values generate more “creative” output")  
  # Submit button to start generating ideas
  generate_button = form.form_submit_button("Generate Healthcare advice")

  if generate_button:
    if Healthcare_input == "":
      st.error("Healthcare topic field cannot be blank")
    else:
      my_bar = st.progress(0.05)
      st.subheader("Healthcare advice:")

      for i in range(num_input):
          st.markdown("""---""")
          Healthcare_advice = gen_advice(Healthcare_input, creativity_input)
          st.write(Healthcare_advice)
          my_bar.progress((i+1)/num_input)
