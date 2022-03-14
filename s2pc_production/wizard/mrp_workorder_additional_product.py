# -*- coding: utf-8 -*-=

from odoo import models


class MrpWorkorderAdditionalProduct(models.TransientModel):
    _inherit = "mrp_workorder.additional.product"

    def add_product(self):
        wo = self.workorder_id
        move = False
        if self.type == 'component':
            test_type = self.env.ref('mrp_workorder.test_type_register_consumed_materials')
            move = self.env['stock.move'].create(
                wo.production_id._get_move_raw_values(
                    self.product_id,
                    self.product_qty,
                    self.product_id.uom_id,
                    operation_id=wo.operation_id.id,

                )
            )
        else:
            test_type = self.env.ref('mrp_workorder.test_type_register_byproducts')
            move = self.env['stock.move'].create(
                wo.production_id._get_move_finished_values(
                    self.product_id.id,
                    self.product_qty,
                    self.product_id.uom_id.id,
                    operation_id=wo.operation_id.id,
                )
            )

        check = {
            'workorder_id': wo.id,
            'component_id': self.product_id.id,
            'product_id': wo.product_id.id,
            'company_id': self.company_id.id,
            'team_id': self.env['quality.alert.team'].search([], limit=1).id,
            'finished_product_sequence': wo.qty_produced,
            'test_type_id': test_type.id,
            'qty_done': self.product_qty,
        }
        if move:
            move.write({'restricted_workorder_id': wo and wo.id})
            move._action_confirm()
            check.update({'move_id': move.id})
        additional_check = self.env['quality.check'].create(check)

        if wo.current_quality_check_id:
            additional_check._insert_in_chain('before', wo.current_quality_check_id)
            wo._change_quality_check(position='previous')
        else:
            last_check = wo.check_ids.filtered(
                lambda c: not c.next_check_id and
                          c.finished_product_sequence == wo.qty_produced and
                          c != additional_check
            )
            additional_check._insert_in_chain('after', last_check)
            wo._change_quality_check(position='last')
