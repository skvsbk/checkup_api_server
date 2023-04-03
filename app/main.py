import hashlib

from fastapi import FastAPI
import uvicorn
from app.routers import checkup_headers, checkup_details, facilities, nfc, plants, roles, rolutelinks, routes, users
from app.routers import valparams
from app.models.database import get_db
from app.utils import users_crud, roles_crud
from app.schemas import role, user


app = FastAPI(title='Electronic journal of inspections')


app.include_router(checkup_headers.router, prefix='/checkup_headers', tags=['checkup_headers'])
app.include_router(checkup_details.router, prefix='/checkup_details', tags=['checkup_details'])
app.include_router(facilities.router, prefix='/facilities', tags=['facilities'])
app.include_router(nfc.router, prefix='/nfc', tags=['nfc'])
app.include_router(plants.router, prefix='/plants', tags=['plants'])
app.include_router(roles.router, prefix='/roles', tags=['roles'])
app.include_router(rolutelinks.router, prefix='/rolutelinks', tags=['rolutelinks'])
app.include_router(routes.router, prefix='/routes', tags=['routes'])
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(valparams.router, prefix='/valparams', tags=['valparams'])


@app.on_event('startup')
async def startup():

    db = get_db().__next__()
    roles_for_app = roles_crud.get_all(db=db, limit=100, skip=0)
    if len(roles_for_app) == 0:
        # create all roles at first start
        role_admin = roles_crud.create_role(role=role.RoleCreate(name='admin'), db=db)
        roles_crud.create_role(role=role.RoleCreate(name='user_webapp'), db=db)
        roles_crud.create_role(role=role.RoleCreate(name='user_mobapp'), db=db)

        # create user 'admin' at first start
        admin_password = hashlib.md5("admin".encode('utf-8')).hexdigest()
        user_db = user.UserCreate(name='admin', login='admin', password=admin_password, role_id=role_admin.id, active=1)
        users_crud.create_user(user=user_db, db=db)


@app.on_event('shutdown')
async def shutdown():
    # await database.disconnect()
    pass

if __name__ == '__main__':
    uvicorn.run('app.main:app', port=8000, host='0.0.0.0', reload=True)
