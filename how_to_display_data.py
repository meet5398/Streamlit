import streamlit as st
import pandas as pd
import numpy as np
import time

a = [1,2,3,4,5,6,7,8,]
n=np.array(a)
nd=n.reshape((2,4))
dic = {
    "name" :[ "meet","ronak"],
    "age"  : ["21","23"],
    "city" : ["kodinar","baroda"]
}
data = pd.read_csv("tmdb_5000_credits.csv")
print(data)

#below code are used to print data on web page as mentioned above
st.dataframe(a)
st.dataframe(nd)
st.dataframe(data)
st.dataframe(dic)

#we can chage the height and width of dataframe using below code
st.dataframe(data,width=1000,height=400)

st.table(nd) #another methode to print into table form,here we will not get scroll bar

st.json(dic) #print in object formate

#now let's see using write function
st.write(a) #it will be in simple form as it is


