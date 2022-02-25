# -*- coding: utf-8 -*-
import json

from odoo import fields, models, api, _
from datetime import timedelta, datetime
from odoo.tools import date_utils


class ModelName(models.Model):
	_inherit = 'mrp.production'
	mrp_team = fields.Many2one('mrp.team', string="Equipe de production")
	current_date = fields.Date(string="To days date", default=datetime.now())
	date_planned_start_related = fields.Datetime(string="infos date prevue", related="date_planned_start", readonly=True)
	quality_widget = fields.Text('Quality widget', compute='_compute_quality_widget')

	def get_selection_label(self, object, field_name, field_value):
		return _(dict(self.env[object].fields_get(allfields=[field_name])[field_name]['selection'])[field_value])

	@api.depends('workorder_ids.check_ids', 'workorder_ids.quality_alert_ids')
	def _compute_quality_widget(self):
		for production in self:
			quality_vals = {}
			quality_vals['work_check'] = {}
			quality_vals['work_alert'] = {}
			quality_vals['header_check'] = ['Opération', 'Poste de travail', 'Contrôlé par', 'Point de contrôle', 'Etat', 'Notes']
			quality_vals['header_alert'] = ['Opération', 'Nom', 'Poste de travail', 'Responsable', 'Cause première', 'Etape', 'Description']
			for work in production.workorder_ids:
				if work.check_ids:
					quality_vals['work_check'][work.name] = []
					check_vals = {}
					for check in work.check_ids:
						check_vals.update(id=check.id)
						check_vals.update(measure_on=self.get_selection_label('quality.check', 'measure_on', check.measure_on))
						check_vals.update(workcenter_id=check.workcenter_id.name)
						check_vals.update(point_id=check.point_id.name)
						check_vals.update(additional_note=check.additional_note)
						check_vals.update(quality_state=self.get_selection_label('quality.check', 'quality_state', check.quality_state))
						quality_vals['work_check'][work.name].append(check_vals)
				if work.quality_alert_ids:
					quality_vals['work_alert'][work.name] = []
					alert_vals = {}
					for alert in work.quality_alert_ids:
						alert_vals.update(id=alert.id)
						alert_vals.update(name=alert.name)
						alert_vals.update(workcenter_id=alert.workcenter_id.name)
						alert_vals.update(user_id=alert.user_id.name)
						alert_vals.update(reason_id=alert.reason_id.name)
						alert_vals.update(stage_id=alert.stage_id.name)
						alert_vals.update(description=alert.description)
						quality_vals['work_alert'][work.name].append(alert_vals)
			other_check = production.check_ids.filtered(lambda check: check.id not in production.workorder_ids.mapped('check_ids').ids)
			if other_check:
				quality_vals['work_check']['Autres contrôles'] = []
				check_vals = {}
				for check in other_check:
					check_vals.update(id=check.id)
					check_vals.update(measure_on=self.get_selection_label('quality.check', 'measure_on', check.measure_on))
					check_vals.update(workcenter_id=check.workcenter_id.name)
					check_vals.update(point_id=check.point_id.name)
					check_vals.update(additional_note=check.additional_note)
					check_vals.update(quality_state=self.get_selection_label('quality.check', 'quality_state', check.quality_state))
					quality_vals['work_check']['Autres contrôles'].append(check_vals)
			other_alert = production.quality_alert_ids.filtered(
				lambda alert: alert.id not in production.workorder_ids.mapped('quality_alert_ids').ids)
			if other_alert:
				quality_vals['work_alert']['Autres alertes'] = []
				alert_vals = {}
				for alert in other_alert:
					alert_vals.update(id=alert.id)
					alert_vals.update(name=alert.name)
					alert_vals.update(workcenter_id=alert.workcenter_id.name)
					alert_vals.update(user_id=alert.user_id.name)
					alert_vals.update(reason_id=alert.reason_id.name)
					alert_vals.update(stage_id=alert.stage_id.name)
					alert_vals.update(description=alert.description)
					quality_vals['work_alert']['Autres alertes'].append(alert_vals)
			production.quality_widget = json.dumps(quality_vals, default=date_utils.json_default)
