# Importing packages
import streamlit as st

st.header('Basic Calculator APP')

list_of_operation = ['Addition', 'Subtraction', 'Multiplication', 'Division']

operation = st.selectbox('Choose an operation', options=list_of_operation)

input_1 = st.number_input('Input 1')
input_2 = st.number_input('Input 2')

# Performing operation
if operation == 'Addition':
    st.write('Result:', input_1+input_2)
elif operation == 'Subtraction':
    st.write('Result:', input_1-input_2)
elif operation == 'Multiplication':
    st.write('Result:', input_1*input_2)
elif operation == 'Division':
    if input_2==0:
        raise ValueError('Attempt to division by Zero, not allowed in maths!!!')
    st.write('Result:', input_1/input_2)

st.write('Thanks for using the service')
