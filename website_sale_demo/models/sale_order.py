from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_order_line_values(
        self, product_id, quantity, linked_line_id=False,
        no_variant_attribute_values=None, product_custom_attribute_values=None,
        **kwargs
    ):
        values = super()._prepare_order_line_values(
            product_id, quantity, linked_line_id,
            no_variant_attribute_values, product_custom_attribute_values,
            **kwargs
        )
        if attachment := kwargs.get('attachment'):
            values.update({
                'attachment': attachment,
                'filename': kwargs.get('filename')
            })
        return values
