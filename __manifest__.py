# -*- coding: utf-8 -*-
{
    "name": "Sale Delivery Notes",
    "version": "18.0.1.0.0",
    "summary": "Adds delivery notes on sales orders",
    "description": "Extends Sales Orders with an optional multi-line Delivery Notes field.",
    "category": "Sales/Sales",
    "author": "Custom",
    "license": "LGPL-3",
    "depends": ["sale", "sale_stock", "purchase", "account"],
    "data": [
        "views/sale_order_views.xml",
        "views/purchase_order_views.xml",
        "report/sale_quotation_report.xml",
        "report/sale_report_action.xml",
        "report/purchase_report.xml",
        "report/invoice_report.xml",
    ],
    "installable": True,
    "application": False,
}
