from fastapi import FastAPI
import uvicorn
from app.routers import checkups, facilities, nfc, valparams, routes, users, roles
from app.models.database import engine, Base, get_db
from app.utils import users_crud, roles_crud
from app.schemas import role, user


app = FastAPI(title='Electronic journal of inspections')
app.include_router(checkups.router, prefix='/checkups', tags=['checkups'])
app.include_router(facilities.router, prefix='/facilities', tags=['facilities'])
app.include_router(nfc.router, prefix='/nfc', tags=['nfc'])
app.include_router(valparams.router, prefix='/params', tags=['params'])
app.include_router(routes.router, prefix='/routes', tags=['routes'])
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(roles.router, prefix='/roles', tags=['roles'])


@app.on_event('startup')
async def startup():

    db = get_db().__next__()
    roles = roles_crud.get_all(db=db, limit=100, skip=0)
    if roles == []:
        # create roles at first start
        role_admin = roles_crud.create_role(role=role.RoleCreate(name='admin'), db=db)
        roles_crud.create_role(role=role.RoleCreate(name='user_webapp'), db=db)
        roles_crud.create_role(role=role.RoleCreate(name='user_mobapp'), db=db)

        # create user 'admin' at first start
        user_db = user.UserCreate(name='admin', login='admin', password='admin', role_id=role_admin.role_id, active=1)
        users_crud.create_user(user=user_db, db=db)




@app.on_event('shutdown')
async def shutdown():
    # await database.disconnect()
    pass

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='0.0.0.0', reload=True)
