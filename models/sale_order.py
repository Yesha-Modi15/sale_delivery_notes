import logging
from odoo import api, fields, models

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Custom fields
    delivery_notes = fields.Text(string="Delivery Notes")
    location_id = fields.Many2one(
        "stock.location",
        string="Location",
        store=True,
        default=lambda self: self._default_location_id(),
    )

    # Default location logic
    @api.model
    def _default_location_id(self):
        _logger.info("=== _default_location_id started ===")

        # Get warehouse from context
        warehouse_id = self.env.context.get("default_warehouse_id")
        _logger.info("Context default_warehouse_id: %s", warehouse_id)

        warehouse = self.env["stock.warehouse"].browse(warehouse_id) if warehouse_id else False
        _logger.info("Warehouse after browse: %s", warehouse.name if warehouse else "None")

        # Fallback: first warehouse in the company
        if not warehouse:
            warehouse = self.env["stock.warehouse"].search(
                [("company_id", "=", self.env.company.id)],
                limit=1,
            )
            _logger.info("Warehouse after search by company: %s", warehouse.name if warehouse else "None")

        # Return stock location
        location_id = warehouse.lot_stock_id.id if warehouse and warehouse.lot_stock_id else False
        _logger.info("Returning location_id: %s", location_id)
        return location_id

    # Onchange to update location when warehouse changes
    @api.onchange("warehouse_id")
    def _onchange_warehouse_id_set_location(self):
        self.location_id = self.warehouse_id.lot_stock_id