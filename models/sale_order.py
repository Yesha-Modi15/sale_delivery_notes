from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_notes = fields.Text(string="Delivery Notes")
    location_id = fields.Many2one(
        "stock.location",
        string="Location",
        store=True,
        default=lambda self: self._default_location_id(),
    )

    @api.model
    def _default_location_id(self):
        warehouse_id = self.env.context.get("default_warehouse_id")
        warehouse = self.env["stock.warehouse"].browse(warehouse_id) if warehouse_id else False
        if not warehouse:
            warehouse = self.env["stock.warehouse"].search(
                [("company_id", "=", self.env.company.id)],
                limit=1,
            )
        return warehouse.lot_stock_id.id if warehouse and warehouse.lot_stock_id else False

    @api.onchange("warehouse_id")
    def _onchange_warehouse_id_set_location(self):
        self.location_id = self.warehouse_id.lot_stock_id