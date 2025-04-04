import streamlit as st
from openai_connection_api import ai_client 

st.title("SmartText Generator")

# keywords
keywords = st.text_input("Enter keywords (comma-separated):")

# usage
use_case = st.selectbox("Select the type of writing:", ["Essay", "Report", "Email", "Blog Article"])

# length
word_count = st.selectbox("Select word count range:", ["100-200", "200-400", "400-600", "600-800"])

# style
writing_style = st.selectbox("Select writing style:", ["Casual", "Formal", "Persuasive"])

# tone
tone = st.selectbox("Select tone:", ["Neutral", "Passionate", "Objective"])

# output format
output_format = st.selectbox("Select output format:", ["Plain Text", "Markdown", "HTML"])

# change tokens depending on the length
def get_max_tokens(word_range):
    if word_range == "100-200":
        return 300
    elif word_range == "200-400":
        return 600
    elif word_range == "400-600":
        return 900
    elif word_range == "600-800":
        return 1100
    else:
        return 600  # default fallback

if st.button("Generate Text"):
    if keywords.strip():
        # create a prompt
        prompt = f"""
You are a skilled writer.

Write a {use_case.lower()} using the following keywords: {keywords}.
The length must be strictly between {word_count} words. Do not stop before reaching at least the minimum number of words.

Use a {writing_style.lower()} style and a {tone.lower()} tone.
Output the result as {output_format.lower()}.

Make sure the keywords are naturally included and the content is informative and well-structured.

If needed, elaborate on your arguments or add relevant examples to meet the minimum word count.

At the end of the text, include the number of words in this format: [Word Count: ###]

"""

        message = [{"role": "user", "content": prompt}]

        try:
            max_tokens = get_max_tokens(word_count)
            
            response = ai_client.analyze_text(message, max_tokens=max_tokens)
            
            # output
            if response:
                if "error" in response:
                    st.error(f"Error: {response['error']} (Step: {response.get('step', 'Unknown')})")
                else:
                    st.subheader("Generated Text")
                    st.text_area("Output:", value=response, height=300)
            else:
                st.error("Unexpected response format.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    else:
        st.warning("Please enter at least one keyword.")
