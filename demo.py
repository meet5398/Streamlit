import streamlit as st

st.title("hello sreamlit")
st.header("parul university")
st.subheader("parul")
st.text(" I am student of parul university")
st.markdown(""""
 # h1 tag
## h2 tag
### h3 tag
:moon:<br>  
:sunglasses:
""for making bold""<br>
_for making italic_
""",True)
#moon for emoji moon
# and we can use html tag also as we have used <br>
#sunglasses for emoji sunglasses

st.latex('''a = (Σy)(Σx2) – (Σx)(Σxy)/ n(Σx2) – (Σx)2''')
st.write("harsh","python","gupta")
st.write(st)
#for printing streamlit documentation