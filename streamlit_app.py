
import os
import tempfile
import streamlit as st
import pandas as pd
import time    
from datetime import datetime, timedelta

from dataset_explorer import app
#pyinstaller --onefile --additional-hooks-dir=./hooks run.py --clean
# streamlit run C:/Users/e-um/Documents/Workspace/group-audit-dataset-explorer/streamlit_app.py --server.enableXsrfProtection false
st.set_page_config(page_title="dataset-explorer")

def read_and_save_file():
    clear()
    for file in st.session_state["file_uploader"]:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            #tf.write(file.getbuffer())
            bd = file.read()
            tmp.write(bd)
            file_path = tmp.name
            st.write(file_path)

        with st.session_state["ingestion_spinner"], st.spinner(f"Ingesting {file_path}"):
            #ingest(file_path, file.name)
            st.write("bonjour")
            app.main(file_path, "Basic")#input_mode)
        #st.write("bonjour1")
        #app.main(file_path, "Advanced")#input_mode)

        #os.remove(file_path)
        
def clear():
    st.session_state["options"] = []
    st.session_state["ingestion_spinner"] = st.empty()

def init():
    if len(st.session_state) == 0:
        st.session_state["options"] = []
        st.session_state["ingestion_spinner"] = st.empty()
        

### MAIN ###
def main():
    
    init() ### INITIALIZATION ###  
    
    col1, col2 = st.sidebar.columns([0.10, 0.90], gap="medium")
    with col1:
        st.write("image")
        #st.image(config.LOGO_PATH, width=50)
    with col2:
        st.title("Lorem Ipsum")       
    st.sidebar.divider()
    
    st.subheader("Upload document(s)")
    st.caption(" ")

    st.file_uploader(
        "Upload documents",
        type=["csv", "xlsx", "xls"],
        key="file_uploader",
        on_change=read_and_save_file,
        label_visibility="collapsed",
        accept_multiple_files=True,
    )

if __name__ == "__main__":
    main()