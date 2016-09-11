# -*- coding: utf-8 -*-
"""
Auth* related model.

This is where the models used by the authentication stack are defined.

It's perfectly fine to re-use this definition in the inviteExportmail application,
though.

"""
import os
from datetime import datetime
from hashlib import sha256
__all__ = ['SysMUser', 'SysMUserExport' ]

from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Unicode, Integer, DateTime, BigInteger
from sqlalchemy.orm import relation, synonym

from inviteexportmail.model import DeclarativeBase, metadata, DBSession

class SysMUser(DeclarativeBase):
 

    __tablename__ = 'sys_m_user'

    id_user = Column('ID_USER',BigInteger, autoincrement=True, primary_key=True)
    username = Column('USERNAME', Unicode(255), unique=True, nullable=False)
    firstname = Column('FIRST_NAME', Unicode(255) )
    lastname = Column('LAST_NAME', Unicode(255) )
    
    userexport= relation('SysMUserExport');
    

    def __repr__(self):
        return '<SysMUser: name=%s>' % repr(self.username)

    def __unicode__(self):
        return self.username
    
    
    @classmethod
    def getById(cls,id):
        return DBSession.query(cls).get(id)
        
class SysMUserExport(DeclarativeBase):
 

    __tablename__ = 'SYS_M_USER_EXPORT'

    id_user = Column('ID_USER', BigInteger,ForeignKey('sys_m_user.ID_USER' ), index=True, primary_key=True)
    users = relation('SysMUser',   backref='sys_m_user_export_id_user')
    
    status_export = Column('STATUS_EXPORT', Unicode(1), unique=True, nullable=False)
    total_export = Column('TOTAL_EXPORT', Unicode(255) )
    
    
    def __init__(self,id_user=None,status_export="W",total_export="1"): 
        self.id_user = id_user
        self.status_export = status_export
        self.total_export = total_export

    #def __repr__(self):
    #    return '<SysMUserExport: name=%s>' % repr(self.users.username)

    #def __unicode__(self):
    #    return self.users.username
    
    def update (self):
        DBSession.merge (self)
        DBSession.flush() 
        
    def save (self):
        DBSession.add(self)
        DBSession.flush() 
        
    @classmethod
    def getById(cls,id):
        sql = "SELECT ID_USER,STATUS_EXPORT, TOTAL_EXPORT FROM SYS_M_USER_EXPORT WHERE ID_USER =:idUser"
        result = DBSession.execute(sql,{'idUser' : id});
        
        for row in result:
            return SysMUserExport(id_user=row[0],status_export=row[1],total_export=row[2])
        
        return None
        #return DBSession.query(cls).filter(cls.id_user == str(id)).first()
