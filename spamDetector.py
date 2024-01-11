import pickle 
import streamlit as st
from win32com.client import Dispatch



model = pickle.load(open("spam.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))



def main():
	st.title("Email Spam Classification App")
	st.subheader("Built with streamlit and Python")
	msg = st.text_input("Enter message:")

	if st.button("Predict"):
		data = [msg]
		vect = cv.transform(data).toarray()
		prediction = model.predict(vect)
		result = prediction[0]
		if result == 1:
			st.error("This is a spam")

		else:
			st.success(" Ham Yummy ")


main()
