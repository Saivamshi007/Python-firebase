from firebase import firebase
import streamlit as st


def upload():

	data={
    	'Name':name,
    	'Age':age
	}
	result=firebase.post('/pythontest-29138/New',data)
	result2=firebase.get('/pythontest-29138/New','')
	st.success(result2)


firebase=firebase.FirebaseApplication("https://pythontest-29138.firebaseio.com/",None)
st.title("Python connectivity with firebase")
name=st.text_input("Enter your name")
age=st.text_input("Enter your age")


if st.button("Upload"):
	upload()




