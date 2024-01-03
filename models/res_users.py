# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class Users(models.Model):
    _inherit = "res.users"

    document_signature = fields.Image('Document Signature', copy=False, attachment=True,
                             max_width=1024, max_height=1024)