{
    "name": "Website Sale Demo",
    "summary": """
        Website Sale Demo
        """,
    "category": "",
    "version": "16.0.1.0.0",
    "author": "Odoo PS",
    "website": "https://www.odoo.com",
    "license": "OEEL-1",
    "depends": ["website_sale"],
    "data": [
        "views/sale_order_views.xml",
        "views/templates.xml",
    ],
    "assets": {
        "web.assets_frontend": [
            "website_sale_demo/static/src/js/**/*.js",
        ],
    },
}
