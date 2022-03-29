from odoo import fields, models, api


class MrpConsumptionWarning(models.Model):
    _name = 'mrp.consumption.warning.model'
    _inherit = 'mrp.consumption.warning'
    _description = 'Description'


class MrpConsumptionWarningLineTransient(models.Model):
    _name = 'mrp.consumption.warning.line.model'
    _description = 'description'
    _inherit = 'mrp.consumption.warning.line'
    # _description = "Line of issue consumption"
    #
    mrp_consumption_warning_id = fields.Many2one('mrp.consumption.warning.model', "Parent Wizard", readonly=True,
                                                 required=True, ondelete="cascade")


class mrpconsumption(models.Model):
    _name = 'mrp.consumption.record'
    _description = 'description'
    mrp_production_id = fields.Many2one('mrp.production', "Manufacturing Order", readonly=True, required=True,
                                        ondelete="cascade")
    consumption = fields.Selection(related="mrp_production_id.consumption")

    product_id = fields.Many2one('product.product', "Product", readonly=True, required=True)
    product_uom_id = fields.Many2one('uom.uom', "Unit of Measure", related="product_id.uom_id", readonly=True)

    product_consumed_qty_uom = fields.Float("Consumed", readonly=True)
    product_expected_qty_uom = fields.Float("To Consume", readonly=True)
