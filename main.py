from fastapi import FastAPI
from routers import checkups, facilities, nfc, params, routes, users
import uvicorn
from db import database

# https://www.youtube.com/watch?v=qduT62Bygyw

app = FastAPI(title='Electronic journal of inspections')
app.include_router(checkups.router, prefix='/checkups', tags=['checkups'])
app.include_router(facilities.router, prefix='/facilities', tags=['facilities'])
app.include_router(nfc.router, prefix='/nfc', tags=['nfc'])
app.include_router(params.router, prefix='/params', tags=['params'])
app.include_router(routes.router, prefix='/routes', tags=['routes'])
app.include_router(users.router, prefix='/users', tags=['users'])

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
def shutdown():
    await database.disconnect()


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)