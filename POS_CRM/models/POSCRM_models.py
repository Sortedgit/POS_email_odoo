# -*- coding: utf-8 -*-

from odoo import models, fields, api
class poscrm(models.Model):
     _name = 'poscrm.poscrm'
     name = fields.Char()
     description = fields.Text()

class poscrm_contact_template(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'
        _order = "create_date desc"
res_partner()
