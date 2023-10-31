from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

import uvicorn


async def homepage(request):
    return JSONResponse({'hello': 'world'})


async def empty_route(request):
    return JSONResponse({'new route': 'this route does nothing'})

async def contact(request):
    contact_page = """
    <html>
    <head>Contact Us</head>
    <body>
        <p>send an email to: example@hotmail.com</p>
    </body>
    </html>
    """
    return HTMLResponse(content=contact_page)


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/empty', empty_route),
    Route('/contact', contact)
])

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
