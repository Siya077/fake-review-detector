import streamlit as st
import re

# simple clean function
def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', str(text))
    text = text.lower()
    return text

def predict_review(text):
    text_clean = clean_text(text)

    if len(text_clean.split()) < 5:
        return "⚠️ Fake Review (CG) ❌"

    fake_words = ["amazing", "best", "perfect", "buy now"]

    score = sum([1 for word in fake_words if word in text_clean])

    if score >= 2:
        return "⚠️ Fake Review (CG) ❌"
    else:
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
