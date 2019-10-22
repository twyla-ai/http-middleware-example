import uvicorn
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import UJSONResponse as JSONResponse
from twyla.chat.templates.buttons import Buttons, UrlButton
from twyla.chat.templates.text import TextTemplate

app = Starlette(debug=False)


@app.exception_handler(HTTPException)
async def http_exception(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        TextTemplate("Something went wrong while processing your request.").asdict(),
        status_code=exc.status_code,
    )


@app.exception_handler(404)
async def not_found(request: Request, exc: HTTPException) -> JSONResponse:
    buttons = Buttons(
        text="These are not the droids you are looking for. What would you like to do?"
    )
    buttons.add(UrlButton(title="Visit Canvas", url="https://canvas.twyla.ai"))
    buttons.add(UrlButton(title="Visit Google", url="https://google.com"))
    return JSONResponse(buttons.asdict(), status_code=exc.status_code)


# note that the prefix "/api" is important here as this is the same as the path
# zeit forwards to the app
@app.route("/")
@app.route("/api/hello")
async def hello(request: Request):
    return JSONResponse(TextTemplate("Hello there, I am up and running.").asdict())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
