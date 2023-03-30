from odoo import http

from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleProductDesign(WebsiteSale):

    @http.route(['/shop/cart/update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def cart_update_json(
        self, product_id, line_id=None, add_qty=None, set_qty=None, display=True,
        product_custom_attribute_values=None, no_variant_attribute_values=None, **kw
    ):
        if data_uri := kw.get('data_uri'):
            attachment_header, attachment = data_uri.split("base64,", 1)
            kw.update({
                'attachment_header': attachment_header,
                'attachment': attachment,
                'filename': kw.get('filename')
            })
            return super(WebsiteSaleProductDesign, self).cart_update_json(
                product_id, False, add_qty, set_qty, display,
                product_custom_attribute_values, no_variant_attribute_values, **kw
            )
        return super(WebsiteSaleProductDesign, self).cart_update_json(
            product_id, line_id, add_qty, set_qty, display,
            product_custom_attribute_values, no_variant_attribute_values, **kw
        )
