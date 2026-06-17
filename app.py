import streamlit as st

from ingest import ingest_video
from rag import ask_question

st.set_page_config(
    page_title="YouTube RAG",
    page_icon="🎥"
)

st.title("🎥 YouTube Video RAG")

st.write(
    "Chat with any YouTube video transcript."
)

# session state

if "processed" not in st.session_state:
    st.session_state.processed = False

if "messages" not in st.session_state:
    st.session_state.messages = []


# sidebar

with st.sidebar:

    st.header("Video")

    youtube_url = st.text_input(
        "Paste YouTube URL"
    )

    if st.button("Process Video"):

        if youtube_url:

            with st.spinner(
                "Processing video..."
            ):

                count = ingest_video(
                    youtube_url
                )

                st.session_state.processed = True

            st.success(
                f"Processed {count} chunks"
            )


# chat

if st.session_state.processed:

    for message in st.session_state.messages:

        with st.chat_message(
            message["role"]
        ):
            st.markdown(
                message["content"]
            )

    prompt = st.chat_input(
        "Ask about the video..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner(
            "Thinking..."
        ):

            answer = ask_question(
                prompt
            )

        with st.chat_message(
            "assistant"
        ):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

else:

    st.info(
        "Process a YouTube video first."
    )