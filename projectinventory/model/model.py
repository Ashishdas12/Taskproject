
from odoo import models, fields,api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    Test2 = fields.Char(string="Test2")

    def button_validate(self):

        result = super(StockPicking, self).button_validate()

        sale_order = self.sale_id
        if sale_order:
            test1_data = sale_order.Test1
            self.Test2 = test1_data

        return result
