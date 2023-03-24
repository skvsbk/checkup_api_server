from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.valparams import ValParamsDB


class ValChecksDB(Base):
    __tablename__ = 'val_checks'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Float)
    param_id = Column(Integer, ForeignKey('val_params.id'), index=True)
    check_id = Column(Integer, ForeignKey('checks.id'), index=True)

    units = relationship('ValParamsDB', backref='val_checks')
