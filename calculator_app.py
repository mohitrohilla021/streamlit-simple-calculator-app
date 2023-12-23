# Importing packages
import streamlit as st

# Header display in the App
st.header('Basic Calculator APP')

# Operation selection
list_of_operation = ['Addition', 'Subtraction', 'Multiplication', 'Division']
operation = st.selectbox('Choose an operation', options=list_of_operation)

# Number inputs
input_1 = st.sidebar.number_input('Input 1')
input_2 = st.sidebar.number_input('Input 2')

# Performing operation based upon the input
if operation == 'Addition':
    st.write('Result of '+str(input_1)+' '+operation+' with '+str(input_2)+' is:', input_1+input_2)
elif operation == 'Subtraction':
    st.write('Result of '+str(input_1)+' '+operation+' with '+str(input_2)+' is:', input_1-input_2)
elif operation == 'Multiplication':
    st.write('Result of '+str(input_1)+' '+operation+' with '+str(input_2)+' is:', input_1*input_2)
elif operation == 'Division':
    if input_2==0:
        raise ValueError('Attempt to division by Zero, not allowed in maths!!!')
    st.write('Result of '+str(input_1)+' '+operation+' with '+str(input_2)+' is:', input_1/input_2)

st.write('Thanks for using the service')
