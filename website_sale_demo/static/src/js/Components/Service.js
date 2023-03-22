/** @odoo-module **/

const { Component } = owl

export class Service extends Component {
    async willStart() {
        this.partners = await this.env.services.rpc('/web/dataset/search_read', {
            model: 'res.partner',
            domain: [['is_company', '=', true]],
            fields: ['id', 'name'],
        });
        console.log(this.partners);
    }
}

Service.template = "DemoService"
