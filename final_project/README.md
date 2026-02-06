uv init
uv sync
#venv-.venv/Scripts/activate
uv add pandas
#terminal -python ingestion/ingest_to_sqlite.py
#groq model
uv add dotenv
uv add langchain_groq
pip install -r requirements.txt
run: python run.py
streamlit run run.py


