from langchain import HuggingFaceHub
import streamlit as st
import os
from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv

load_dotenv()

def main():
    st.set_page_config("Language Translation")
    st.title("Language Translation")
    st.divider()
    your_lang = st.selectbox("Choose Your Language: ",
                        ['German', 'Spanish', 'French', 'Italian', 'English'])
    choice_lang = st.selectbox("Choose Language To Translate To: ",
                        ['German', 'Spanish', 'French', 'Italian', 'English'])

    txt = st.text_input("Enter Your Sentence", "Type Here ...")

    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl",
                         model_kwargs={"temperature": 0.01, "max_length": 60})


    submit = st.button("Translate")

    # access_token = "hf_..."

    # model = AutoModel.from_pretrained("private/model", token=access_token)

    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

    if submit:
        translation = llm(f'translate this sentence from {your_lang} to {choice_lang}: {txt}')

        st.write(translation)


if __name__ == '__main__':
    main()