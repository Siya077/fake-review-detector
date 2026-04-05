import streamlit as st
import re

# simple clean function
def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', str(text))
    text = text.lower()
    return text

# simple logic (replace with ML later)
def predict_review(text):
    text = clean_text(text)

    fake_words = ["amazing", "best", "perfect", "buy now"]

    for word in fake_words:
        if word in text:
            return "⚠️ Fake Review (CG) ❌"

    return "✅ Real Review (OR)"

# UI
st.title("🛒 Fake Review Detection System")

review = st.text_area("Enter Review")

if st.button("Check Review"):
    if review.strip() == "":
        st.warning("Please enter a review!")
    else:
        result = predict_review(review)

        if "Fake" in result:
            st.error(result)
        else:
            st.success(result)
