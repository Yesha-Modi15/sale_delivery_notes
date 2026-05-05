# -*- coding: utf-8 -*-

from odoo import models


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def _get_rendering_context(self, report, docids, data):
        rendering_context = super()._get_rendering_context(report, docids, data)
        if report.report_name == 'account.report_invoice':
            rendering_context['without_payment_report'] = True
        return rendering_context
