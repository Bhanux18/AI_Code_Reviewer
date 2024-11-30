import streamlit as st
import google.generativeai as genz
from dotenv import load_dotenv
import os
load_dotenv()

# Creating a layout titles for streamlit
st.title("AI - Code :red[Reviewer] Application !")
st.write("-"*30)    
query_text=st.text_area("**Please Input Your Code Here..**",placeholder="Code it or Paste it ..")

# Defining AI functionalities
#genz.configure(api_key=os.getenv("api_key"))
api="AIzaSyBNgkWZQdHQ1f4_YCJUOzKUzRcYbYKvn2Q"
genz.configure(api_key=api)
ai_role="""Act like an expert programmer in python and R.Review the given code for simple correct & clean code.
           show errors,bugs and suggest code improvements in consise ways .
           Represent code in formats like without defining a function and with defining a function.
           Lastly,show the numerical example"""


if st.button("🔍 :blue[**Review_Code**] "):
    if query_text:
        try:           

            model=genz.GenerativeModel(model_name = "models/gemini-1.5-flash",system_instruction=ai_role)
            st.write("-"*30)
            #st.write(query_text)
            response=model.generate_content(query_text)
            st.html("<h3><i> Here Comes , The Modified Code..🧑‍💻<h3>")
            st.write(response.text)
            st.write("-"*30)
            st.download_button("🔻Download",response.text)   
            
    
        except Exception as e:
            st.error(f"An error has occured: {e}")

    else:
        st.warning("Please Input Your Code !")

