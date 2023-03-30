from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    attachment = fields.Binary("Attachment")
    filename = fields.Char("File Name")
