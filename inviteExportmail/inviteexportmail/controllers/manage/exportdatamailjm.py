# -*- coding: utf-8 -*-
"""Main Controller"""

from tg import expose, flash, require, url, lurl
from tg import request, redirect, tmpl_context
from tg.i18n import ugettext as _, lazy_ugettext as l_
from tg.exceptions import HTTPFound
from tg import predicates
from inviteexportmail import model
from inviteexportmail.controllers.secure import SecureController
from inviteexportmail.model import DBSession
from tgext.admin.tgadminconfig import BootstrapTGAdminConfig as TGAdminConfig
from tgext.admin.controller import AdminController

from inviteexportmail.lib.base import BaseController
from inviteexportmail.controllers.error import ErrorController

__all__ = ['ExportDataMailJMController']


class ExportDataMailJMController(BaseController):
     

    def _before(self, *args, **kw):
        tmpl_context.project_name = "inviteexportmail"

    @expose('inviteexportmail.templates.index')
    def index(self):
        """Handle the front-page."""
        
        
        sysMUser = model.SysMUser.getById(1799);
        
         
         
        sysMUserExport = model.SysMUserExport.getById(1799);
         
        if (sysMUserExport):
              
            sysMUserExport.total_export = sysMUserExport.total_export   + 1
            sysMUserExport.update()
        else:
            sysMUserExport = model.SysMUserExport(id_user=sysMUser.id_user,status_export="W",total_export="1")
            sysMUserExport.save()
         
        
        return dict(page='index')
    