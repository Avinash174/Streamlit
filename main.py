import streamlit as sl
import pandas as pd
tabel=pd.DataFrame({"column1":[1,2,3,4,5],"column2":[6,7,8,9,10]})

sl.title("Welcom In Streamlit App")
sl.subheader("This is my first stramlit App")
sl.header("This headder")
sl.text("this is Text")
sl.markdown("**This Bold** This Normal Text")
sl.markdown("# Hello This H1 Heading")
sl.markdown("## Hello This H2 Heading")
sl.markdown("[Google](https://www.google.in)")
sl.markdown("---")
sl.caption("Hi I am Caption")
sl.latex(r"\begin{pmatrix} a & b \\ c & d \end{pmatrix}")
json={"a":"1,2,3,4","b":"5,6,7,8"}
sl.json(json)
code=""" 
print("Hello All)
def hello():
    return hello()
"""
sl.code(code,language="python")

sl.write("### this h3 tag")
sl.metric(label="Wind Speed", value="120 ms⁻¹", delta="1.4 ms⁻¹")
sl.table(tabel)
sl.dataframe(tabel)
sl.image("biryani.jpg",width=80,caption="Biryani",)
sl.audio("mixkit-tech-house-vibes-130.mp3",start_time=0)
sl.video("Bacteria_blue.mp4",)