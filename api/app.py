import aiohttp
import uvicorn
from starlette.applications import Starlette
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import UJSONResponse as JSONResponse
from twyla.chat.templates.buttons import Buttons, UrlButton, PostBackButton
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


@app.route("/api/todo")
async def todo_buttons(_: Request) -> JSONResponse:
    async with aiohttp.ClientSession() as client:
        async with client.get("https://jsonplaceholder.typicode.com/todos") as resp:
            data = await resp.json()
        buttons = Buttons(text="Select Item")
        for item in data[: min(len(data), 3)]:
            i = item.get("id")
            buttons.add(PostBackButton(title=f"Item {i}", payload="x_todo_item_{i}_x"))
        return JSONResponse(buttons.asdict())


@app.route("/api/todo/{item}")
async def todo_item(request: Request) -> JSONResponse:
    item = request.path_params.get("item")

    async with aiohttp.ClientSession() as client:
        async with client.get(
            f"https://jsonplaceholder.typicode.com/todos/{item}"
        ) as resp:
            data = await resp.json()

        return JSONResponse(TextTemplate(payload=data.get("title")))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
