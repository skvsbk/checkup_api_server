from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models.database import Base
from app.models.routes import RoutesDB
from app.models.nfc import NfcTagDB


class RouteLinksDB(Base):
    __tablename__ = 'route_links'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    route_id = Column(Integer, ForeignKey('routes.id'), index=True)
    nfc_id = Column(Integer, ForeignKey('nfc_tag.id'), index=True)
    order = Column(Integer)
    active = Column(Boolean)

    routes = relationship('RoutesDB', backref='route_links')
    nfctag = relationship('NfcTagDB', backref='route_links')
