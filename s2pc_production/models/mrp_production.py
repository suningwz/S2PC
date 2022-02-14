from odoo import fields, models, api
from datetime import timedelta, datetime


class ModelName(models.Model):
    _inherit = 'mrp.production'
    mrp_team = fields.Many2one('mrp.team', string="Equipe de production")
    current_date = fields.Date(string="To days date", default=datetime.now())
    date_planned_start_related = fields.Datetime(string="Infos date prevue", related="date_planned_start",
                                                 readonly=True)
    workorder_ids_state = fields.Char(string="Opération en cours", compute="get_state_workoderids")
    consumption_warning_ids = fields.Many2many('mrp.consumption.warning')

    @api.depends('workorder_ids')
    def get_state_workoderids(self):
        for rec in self.workorder_ids:
            if rec.state == "progress":
                self.workorder_ids_state = rec.name
            else:
                self.workorder_ids_state = ""

    def get_workorder(self):
        record = self.env['mrp.consumption.record']
        print('rec avant')
        for rec in record:
            print(rec)
        return True

    def get_component(self):
        component_adjustement = self.env['mrp.consumption.warning.line']
        for rec in component_adjustement:
            print(rec)
        return True

    @api.onchange('move_raw_ids')
    def onchange_move(self):
        print("move_raw_ids on change")
        for rec in self.move_raw_ids:
            print(rec.name)

    def _action_generate_consumption_wizard(self, consumption_issues):
        ctx = self.env.context.copy()
        lines = []
        for order, product_id, consumed_qty, expected_qty in consumption_issues:
            print("mandalo append")
            lines.append((0, 0, {
                'mrp_production_id': order.id,
                'product_id': product_id.id,
                'consumption': order.consumption,
                'product_uom_id': product_id.uom_id.id,
                'product_consumed_qty_uom': consumed_qty,
                'product_expected_qty_uom': expected_qty
            }))
            print("eto ao zao")
            self.env['mrp.consumption.record'].create({
                'mrp_production_id': order.id,
                'product_id': product_id.id,
                'consumption': order.consumption,
                'product_uom_id': product_id.uom_id.id,
                'product_consumed_qty_uom': consumed_qty,
                'product_expected_qty_uom': expected_qty
            })
            print("eto ah zao vita create")
        ctx.update({'default_mrp_production_ids': self.ids, 'default_mrp_consumption_warning_line_ids': lines})
        action = self.env["ir.actions.actions"]._for_xml_id("mrp.action_mrp_consumption_warning")
        action['context'] = ctx
        return action
