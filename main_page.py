from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")

@app.get("/", response_class=HTMLResponse)
def read_index():
    with open("login.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)

@app.get("/homepage", response_class=HTMLResponse)
def read_homepage():
    with open("homep.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)

@app.get("/gotobuild", response_class=HTMLResponse)
def read_homepage():
    with open("gotobuild.html", "r") as file:
        content = file.read()
    return HTMLResponse(content=content)

@app.get("/createown",response_class=HTMLResponse)
def read_createpage():
    with open("createown.html", "r") as file:
        content=file.read()
    return HTMLResponse(content=content)

@app.get("/crefriends",response_class=HTMLResponse)
def read_createpage():
    with open("crefriends.html", "r") as file:
        content=file.read()
    return HTMLResponse(content=content)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
