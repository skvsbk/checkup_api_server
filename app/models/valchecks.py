from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.valparams import ValParamsDB


class ValChecksDB(Base):
    __tablename__ = 'val_checks'

    valcheck_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Float)
    note = Column(String(256))
    param_id = Column(Integer, ForeignKey('val_params.param_id'), index=True)
    check_id = Column(Integer, ForeignKey('checks.check_id'), index=True)

    units = relationship('ValParamsDB', backref='val_checks')
