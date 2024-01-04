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

    def _find_mail_template(self, force_confirmation_template=False):
        template_id = super(SaleOrder,self)._find_mail_template(force_confirmation_template=force_confirmation_template)
        if template_id == self.env['ir.model.data']._xmlid_to_res_id('sale.mail_template_sale_confirmation', raise_if_not_found=False):
            template_id = self.env['ir.model.data']._xmlid_to_res_id('sale_order_report_sealed.mail_template_sale_confirmation_with_seal', raise_if_not_found=False)
        elif template_id == self.env['ir.model.data']._xmlid_to_res_id('sale.email_template_edi_sale', raise_if_not_found=False):
            template_id = self.env['ir.model.data']._xmlid_to_res_id('sale_order_report_sealed.email_template_edi_sale_with_seal', raise_if_not_found=False)
        return template_id
