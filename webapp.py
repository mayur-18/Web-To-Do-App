import streamlit as st
import functions

todos = functions.getdata()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todo(todos)


def complete(checkbox):
    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st._rerun()


st.title("To-Do App")
st.subheader("Schedule Your Tasks")
st.write("Lets begin!!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key= todo)
    complete(checkbox)

st.text_input(label=" ", placeholder="Add the todos",
              on_change=add_todo, key='new_todo')

