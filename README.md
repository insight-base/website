# website
InsightBase Solutions start-up site

## Setup

- Create virtual environment `py -m venv fastapi-env`
- Activate venv `fastapi-env\Scripts\activate`
- Install **FastAPI** `pip install "fastapi[standard]"`
- Create main.py file
- Run the app `fastapi dev main.py` for dev mode that incl auto reload the server  or `fastapi run main.py` for production mode with optimized performance.

**Important features:** add `/docs` on url which automatic API documentation - interactive UI generated automatically. Another different way - modern looking `/redoc`.