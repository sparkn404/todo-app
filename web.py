# streamlit run web.py from Terminal

import streamlit as st
import functions


def add_todo():
    todo_to_add = st.session_state["new_todo"] + "\n"
    todos.append(todo_to_add)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my subheader")
st.write("This is a write function")

for todo in todos:
    st.checkbox(todo)

st.text_input(label='Add a todo:', placeholder='Add a todo:',
              on_change=add_todo, key='new_todo')

st.session_state
