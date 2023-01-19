from sqlalchemy.orm import Session
from app.models import roles

def get_all(db: Session): # self, limit: int, skip: int = 0) :
    return db.query(roles.RoleDB).all()
