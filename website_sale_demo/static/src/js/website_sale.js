/** @odoo-module **/

import { WebsiteSale } from "website_sale.website_sale"

WebsiteSale.include({
    addToCart: function(params) {
        // Convert pdf to data uri
        const toDataURL = url => fetch(url)
            .then(response => response.blob())
            .then(blob => new Promise((resolve, reject) => {
                const reader = new FileReader()
                reader.onloadend = () => resolve(reader.result)
                reader.onerror = reject
                reader.readAsDataURL(blob)
            }))
        return new Promise(async (resolve, reject) => {
            var self = this
            var _super = this._super.bind(this);
            try {
                // Instead of hardcoding the path, you should get it from file input field
                params.data_uri = await toDataURL('/website_sale_demo/static/src/sample.pdf')
                params.filename = 'sample.pdf'
                const result = await _super.apply(self, arguments)
                resolve(result)
            } catch(error) {
                reject(error)
            }
        })
    },
})
