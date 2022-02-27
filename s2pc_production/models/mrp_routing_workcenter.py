# -*- coding: utf-8 -*-
import json

from odoo import fields, models, api, _
from datetime import timedelta, datetime
from odoo.tools import date_utils


class MrpRoutingWorkingCenter(models.Model):
	_inherit = 'mrp.routing.workcenter'

	restricted_bom_line_ids = fields.One2many('mrp.bom.line', 'restricted_operation_id')
