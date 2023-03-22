/** @odoo-module **/

import { App } from './App'
import publicWidget from 'web.public.widget'
import { startWebClient } from './start'

publicWidget.registry.WebsiteSaleDemo = publicWidget.Widget.extend({
    selector: '#demoApp',
    start: function () {
        const self = this;
        return this._super().then(() => {
            startWebClient(App, self)
        })
    }
})

export default publicWidget.registry.WebsiteSaleDemo
