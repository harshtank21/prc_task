from odoo import api, fields, models


class SaleOrderWizad(models.TransientModel):
    _name = 'sale.order.wizard'

    start_date = fields.Date(
        string="Start Date"
    )
    end_date = fields.Date(
        string="End Date"
    )

    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        return res


    def submit_action_button(self):
        print(self._context)