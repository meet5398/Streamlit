import random
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt  # it is also an library for graph
import matplotlib as mlt

data = pd.DataFrame(
    np.random.randn(100,3),
    columns=['a','b','c']
)

st.dataframe(data)

#below code are used to print or display graph
#line chart
st.line_chart(data,width=500)

#area_chart
st.area_chart(data)

#bar_chart
st.bar_chart(data)

#scatter chart for this we will have to import matplotlib
plt.scatter(data['a'],data['b'])
plt.title("scatter")
st.pyplot()
#in normal python code we need to write plt.show but here we need to write st.pyplot

#above code for plotting has now expired so we need to use below code for it
fig, ax = plt.subplots()
ax.scatter(data['a'],data['b'])
st.pyplot(fig)



#below graph is altair_chart
chart= alt.Chart(data).mark_square().encode(x = 'a', y='b',tooltip=['a','b'])
#using tooltip you can point to any where in graph and you will come to know value of a and b
st.altair_chart(chart,use_container_width=True)
#using use_container_true we can use full width for the graph



st.graphviz_chart('''
digraph{
university -> college
college    -> student
student    ->  assignment
student   ->  college
assignment -> university
}
''')


#for allocating location on map using lattitude and longitude
city=pd.DataFrame({
   'cities' : ["cigago",'baroda'],
    'lat'    : [41.868171,22.307159],
    'lon'    : [-87.667458,73.181221]
})
st.map(city)

#for image upload
st.image("smarty.jpeg", width=300)

#for audio and video upload
st.audio("music.mp3")
st.video("video.mp4")
