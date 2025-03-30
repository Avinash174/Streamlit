import streamlit as st
import pandas as pd

# Create DataFrame
tabel = pd.DataFrame({"column1": [1, 2, 3, 4, 5], "column2": [6, 7, 8, 9, 10]})

# Streamlit Elements
st.title("Welcome In Streamlit App")
st.subheader("This is my first Streamlit App")
st.header("This is a header")
st.text("This is Text")
st.markdown("**This Bold** This Normal Text")
st.markdown("# Hello This H1 Heading")
st.markdown("## Hello This H2 Heading")
st.markdown("[Google](https://www.google.in)")
st.markdown("---")
st.caption("Hi I am Caption")
st.latex(r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}")

# Corrected JSON
json_data = {"a": [1, 2, 3, 4], "b": [5, 6, 7, 8]}
st.json(json_data)

# Fix the broken Python code snippet
code = """ 
print("Hello All")
def hello():
    return "hello"
"""
st.code(code, language="python")

st.write("### This is an H3 tag")
st.metric(label="Wind Speed", value="120 ms⁻¹", delta="1.4 ms⁻¹")

# Display Data
st.table(tabel)
st.dataframe(tabel)

# Display Media Files (Ensure Files Exist)
st.image("biryani.jpg", width=80, caption="Biryani")
st.audio("mixkit-tech-house-vibes-130.mp3", start_time=0)
st.video("Bacteria_blue.mp4")

# Function for Checkbox Change
def change():
    print("Change triggered")
    print(st.session_state.changer)

# Checkbox with correct on_change reference
check = st.checkbox("I agree", on_change=change, key="changer")

# Conditional Text
if check:
    st.write("I Am Great")
else:
    st.write("Bye")

# radio btn 
radio_btn=st.radio("select on option",options=['Yes','No'])
print(radio_btn)

def click():
    print("click me")
btn=st.button("click me",on_click=click)
select=st.selectbox("select me",options=['first','second','third'])
print(select)
mul_select=st.multiselect("What is your fovourate",options=['hello','hi'])
print(mul_select)
st.write(mul_select)