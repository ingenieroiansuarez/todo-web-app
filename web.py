import streamlit as st
from streamlit import checkbox
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader('this is a simple to-do app')
st.write("this is a simple to-do app that allows you to add,"
         " edit, and complete tasks.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ",
              placeholder="Enter a todo",
              on_change=add_todo, key="new_todo")
