


import pandas as pd

import streamlit as st

import plotly.express as px



from streamlit_pandas_profiling import st_profile_report

from pandas_profiling import ProfileReport

st.set_page_config(page_title="Runs Scored by Players",
                   page_icon=":bar_chart:",
                   layout="wide")
st.title("Runs Scored by Cricketers in the World")
df=pd.read_csv("most_runs_in_cricket.csv")


input_col,pie_col=st.columns(2)
data=df.groupby(["Player"])
af=data[["Player","Runs"]].head().sort_values(by="Runs",ascending=False).head(10)

af.columns=['Player','Runs']
jf=af.sort_values(by="Runs",ascending=False)
top_n=input_col.text_input("How many of the Players would you like to see?",10)
top_n=int(top_n)
jf=jf.head(top_n)
jf=jf.head(top_n)

print(jf)
fig=px.pie(jf,values="Runs",names="Player")
pie_col.write(fig)
af=data[["Player","100"]].head().sort_values(by="100",ascending=False).head(10)


ax = px.bar(af,x = 'Player', y = "100", color = 'Player', title='Centuries by Players')
st.title("Statistics Report")
st.header("Data")

#profile = ProfileReport(df)
profile = ProfileReport(df)



st.dataframe(df)

st_profile_report(profile)

