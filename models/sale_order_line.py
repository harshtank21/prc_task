from odoo import models, fields, api


class SaleOrderLines(models.Model):
    _inherit = "sale.order.line"
    _description = "task"


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "task"

    def order_sale_wizard(self):
        warning = {
            'name': 'Wizard',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order.wizard',
            'view_id': self.env.ref('prc_task.sale_order_wizard_form_view').id,
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'new',
        }
        return warning