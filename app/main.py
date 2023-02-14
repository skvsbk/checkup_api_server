from fastapi import FastAPI
import uvicorn
from app.routers import checks, checkups, facilities, nfc, plants, roles, rolutelinks, routes, users
from app.routers import valchecks, valparams, valunits
from app.models.database import get_db
from app.utils import users_crud, roles_crud
from app.schemas import role, user


app = FastAPI(title='Electronic journal of inspections')

app.include_router(checks.router, prefix='/checks', tags=['checks'])
app.include_router(checkups.router, prefix='/checkups', tags=['checkups'])
app.include_router(facilities.router, prefix='/facilities', tags=['facilities'])
app.include_router(nfc.router, prefix='/nfc', tags=['nfc'])
app.include_router(plants.router, prefix='/plants', tags=['plants'])
app.include_router(roles.router, prefix='/roles', tags=['roles'])
app.include_router(rolutelinks.router, prefix='/rolutelinks', tags=['rolutelinks'])
app.include_router(routes.router, prefix='/routes', tags=['routes'])
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(valchecks.router, prefix='/valchecks', tags=['valchecks'])
app.include_router(valparams.router, prefix='/valparams', tags=['valparams'])
app.include_router(valunits.router, prefix='/valunits', tags=['valunits'])


@app.on_event('startup')
async def startup():

    db = get_db().__next__()
    roles = roles_crud.get_all(db=db, limit=100, skip=0)
    if roles == []:
        # create all roles at first start
        role_admin = roles_crud.create_role(role=role.RoleCreate(role_name='admin'), db=db)
        roles_crud.create_role(role=role.RoleCreate(role_name='user_webapp'), db=db)
        roles_crud.create_role(role=role.RoleCreate(role_name='user_mobapp'), db=db)

        # create user 'admin' at first start
        user_db = user.UserCreate(name='admin', login='admin', password='admin', role_id=role_admin.role_id, active=1)
        users_crud.create_user(user=user_db, db=db)


@app.on_event('shutdown')
async def shutdown():
    # await database.disconnect()
    pass

if __name__ == '__main__':
    uvicorn.run('app.main:app', port=8000, host='0.0.0.0', reload=True)
