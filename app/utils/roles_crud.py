from sqlalchemy.orm import Session
from app.models import roles
from app.schemas.role import RoleCreate

def get_all(db: Session): # self, limit: int, skip: int = 0) :
    return db.query(roles.RoleDB).all()

def create_role(role: RoleCreate, db: Session):
    db_role = roles.RoleDB(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role
