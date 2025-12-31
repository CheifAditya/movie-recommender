from fastapi import FastAPI
from pydantic import BaseModel
from src.recommender import recommend 

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from fastapi import Form

#register templates
templates = Jinja2Templates(directory="src/templates")
#Creating FastAPI instance
app = FastAPI(title= "Movie Recommender API")

app.mount("/static",StaticFiles(directory="src/static"),name="static")

class MovieRequest(BaseModel):
    movie : str
    top_n : int = 5

#Landing Page Route
@app.get("/",response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/recommend")
def get_recommendations(request: MovieRequest):
    return recommend(request.movie,request.top_n)

#UI recommendation route
@app.post("/recommend-ui",response_class=HTMLResponse)
def recommend_ui(request:Request,movie_name: str = Form(...)):
    recommendations = recommend(movie_name)

    return templates.TemplateResponse("index.html",{"request":request,"movies":recommendations,"search_movie":movie_name,"not_found":not recommendations})

