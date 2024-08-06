import streamlit as st
import functions

todos = functions.get_todos()


st.title("My Todo App")
st.subheader("This is my subheader")
st.write("This is a write function")

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Add a todo:', placeholder='Add a todo:', label_visibility='hidden')
