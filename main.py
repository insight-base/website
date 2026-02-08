from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


# creating app instance 
app = FastAPI()

templates = Jinja2Templates(directory="templates")


posts: list[dict] = [
    {
        "id": 1,
        "author": "Eddwin Cheteni",
        "title": "Descriptive Analytics",
        "content": "Understand what happened with clean dashboards and clear narratives."
        "date_posted": "February 07, 2026",
    },
    {
        "id": 2,
        "author": "Eddwin Cheteni",
        "title": "Diagnostic Analytics",
        "content": "Learn why it happened using root-cause analysis and statistical testing."
        "date_posted": "February 07, 2026",
    },
    {
        "id": 3,
        "author": "Eddwin Cheteni",
        "title": "Predictive Analytics",
        "content": "Anticipate what is likely to happen with machine learning and time-series models."
        "date_posted": "February 07, 2026,
    },
    {
        "id": 4,
        "author": "Eddwin Cheteni",
        "title": "Prescriptive Analytics",
        "content": "Decide what to do next with optimization, simulations, and scenario planning."
        "date_posted": "February 07, 2026",
    }
]
# creating a home route that respond to get request at the root URL
@app.get("/", include_in_schema=False) # to hide schema not to display on api docs
@app.get("/posts", response_class=HTMLResponse, include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts})


@app.get("/api/posts")
def get_posts():
    return posts