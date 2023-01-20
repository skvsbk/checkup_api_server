from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..models.database import Base
from ..models.routes import RoutesDB
from ..models.nfc import NfcTagDB


class RouteLinksDB(Base):
    __tablename__ = 'route_links'
    routelink_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    route_id = Column(Integer, ForeignKey('routes.route_id'), index=True)
    nfc_id = Column(Integer, ForeignKey('nfc_tag.nfc_id'), index=True)
    order = Column(Integer)
    active = Column(Boolean)

    routes = relationship('RoutesDB', backref='route_links')
    nfctag = relationship('NfcTagDB', backref='route_links')
