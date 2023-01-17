from app.utils.users import UserUtils, RoleUtils
from app.models.database import database

def get_user_utils() -> UserUtils:
    return UserUtils(database)

def get_role_utils() -> RoleUtils:
    return RoleUtils(database)