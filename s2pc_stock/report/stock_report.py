# -*- coding: utf-8 -*-

from odoo import tools
from odoo import api, fields, models


class StockReport(models.Model):
    _inherit = 'stock.report'

    product_turnover = fields.Float('Outgoing valuation', group_operator="sum", readonly=True, store=True)

    def _with(self):
        with_str = """
             svl_data as (SELECT sum(value) as svl_total from stock_valuation_layer), sm as (select * from stock_move)
        """
        return with_str

    def _select(self):
        select_str = """
            sm.id as id,
            sp.name as picking_name,
            sp.date_done as date_done,
            sp.creation_date as creation_date,
            sp.scheduled_date as scheduled_date,
            sp.partner_id as partner_id,
            sp.is_backorder as is_backorder,
            sp.delay as delay,
            sp.delay > 0 as is_late,
            sp.cycle_time as cycle_time,
            spt.code as picking_type_code,
            spt.name as operation_type,
            p.id as product_id,
            sm.reference as reference,
            sm.picking_id as picking_id,
            sm.state as state,
            sm.product_qty as product_qty,
            sm.company_id as company_id,
            cat.id as categ_id,
            round(sum(svl.value)/svl_data.svl_total,2) as product_turnover
        """

        return select_str

    def _from(self):
        from_str = """
            svl_data, sm
            LEFT JOIN (
                SELECT
                    id,
                    name,
                    date_done,
                    date as creation_date,
                    scheduled_date,
                    partner_id,
                    backorder_id IS NOT NULL as is_backorder,
                    (extract(epoch from avg(date_done-scheduled_date))/(24*60*60))::decimal(16,2) as delay,
                    (extract(epoch from avg(date_done-date))/(24*60*60))::decimal(16,2) as cycle_time
                FROM
                    stock_picking
                GROUP BY
                    id,
                    name,
                    date_done,
                    date,
                    scheduled_date,
                    partner_id,
                    is_backorder
            ) sp ON sm.picking_id = sp.id
            LEFT JOIN stock_picking_type spt ON sm.picking_type_id = spt.id
            LEFT JOIN stock_valuation_layer AS svl ON svl.stock_move_id = sm.id and svl.value < 0
            INNER JOIN product_product p ON sm.product_id = p.id
            INNER JOIN product_template t ON p.product_tmpl_id = t.id
            INNER JOIN product_category cat ON t.categ_id = cat.id
            WHERE t.type = 'product'
        """

        return from_str

    def _group_by(self):
        group_by_str = """
            sm.id,
            sm.reference,
            sm.picking_id,
            sm.state,
            sm.product_qty,
            sm.company_id,
            sp.name,
            sp.date_done,
            sp.creation_date,
            sp.scheduled_date,
            sp.partner_id,
            sp.is_backorder,
            sp.delay,
            sp.cycle_time,
            spt.code,
            spt.name,
            p.id,
            is_late,
            cat.id,
            svl_data.svl_total
        """

        return group_by_str

    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
                            WITH %s
                            SELECT
                                %s
                            FROM
                                %s
                            GROUP BY
                                %s
            )""" % (self._table, self._with(), self._select(), self._from(), self._group_by(),))

    # @api.model
    # def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
    #     res = super(StockReport, self).read_group(domain, fields, groupby, offset, limit, orderby, lazy)
    #     if 'product_id' not in groupby:
    #         if 'product_turnover:sum' in fields:
    #             for item in res:
    #                 if item.get('product_turnover') and item.get('__domain'):
    #                     product_number = self.search(item.get('__domain')).mapped('product_id')
    #                     item['product_turnover'] = item['product_turnover'] / len(product_number)
    #
    #     return res