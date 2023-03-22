{
    "name": "Website Sale Demo",
    "summary": """
        Website Sale Demo
        """,
    "category": "",
    "version": "15.0.1.0.0",
    "author": "Odoo PS",
    "website": "https://www.odoo.com",
    "license": "OEEL-1",
    "depends": ["website_sale"],
    "data": [
        "views/templates.xml",
    ],
    "assets": {
        "website_sale_demo.assets_qweb": [
            "website_sale_demo/static/src/xml/**/*.xml",
        ],
        "web.assets_frontend": [
            "website_sale_demo/static/src/js/**/*.js",
        ],
    },
}
