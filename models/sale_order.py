# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import format_datetime


class SaleOrder(models.Model):
    _inherit = "sale.order"

    document_seal = fields.Image('Document Seal', copy=False, attachment=True,
                                 max_width=1024, max_height=1024,compute='_compute_document_seal')


    def _compute_document_seal(self):
        for each in self:
            each.document_seal = False
