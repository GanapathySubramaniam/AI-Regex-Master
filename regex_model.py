import google.generativeai as genai
import streamlit as st


def configure_model():
    api_key = "AIzaSyDcFVi9W-gJY4gdR8nsnd5oAlQgi0fYQYU"
    genai.configure(api_key=api_key)

    model_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=model_config,
        system_instruction=(
            "You are a regex pattern expert, proficient in understanding and crafting regex "
            "strings. Your task is to translate the user's natural language requirements into "
            "precise regex patterns. After formulating the regex, provide a comprehensive explanation "
            "detailing its components and functionality, along with examples demonstrating the regex's "
            "ability to match relevant scenarios. Conclude by illustrating its application through a "
            "Python code snippet.\n\nUser query:\nConvert the following natural language description "
            "into a regex pattern:\nMy requirements are:"
        ),
    )
    return model

# Initialize the session state
def initialize_session():
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    if 'chat' not in st.session_state:
        st.session_state['chat'] = configure_model().start_chat(history=st.session_state['history'])

def llm_response(prompt):
    response = st.session_state.chat.send_message(prompt, stream=False)
    return response


def main():
    st.header('Regex Master\n ---')
    
    initialize_session()
    with st.sidebar:
        data=st.text_area('Specify the Data')

    pattern= st.chat_input('Specify the type of pattern')

    if data and pattern:
        try:
            prompt=f"Data:\n {data} \n Pattern: {pattern}"
            response=llm_response(prompt)
            st.write(response.text)
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
