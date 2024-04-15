# -*- coding: utf-8 -*-
{
    'name': 'Combo Products',
    'version': '15.0.1.0.0',
    'category': 'pos/product',
    'summary': """This module is used to create POS Combo product and create
     POS Order with Combo Product.""",
    'sequence': 15,
    'depends': ['point_of_sale', 'stock', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_product_view.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_combo_product/static/src/js/pos_combo_popup.js',
            'pos_combo_product/static/src/js/pos_product_screen.js',
            'pos_combo_product/static/src/css/style.css',
            'pos_combo_product/static/src/js/pos_product_add.js',
        ],
        'web.assets_qweb': [
            'pos_combo_product/static/src/xml/pos_combo_product_popup.xml',
            'pos_combo_product/static/src/xml/pos_product_combo.xml',
            'pos_combo_product/static/src/xml/pos_orderline_combo_product.xml',
            'pos_combo_product/static/src/xml/pos_receipt.xml'

        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
