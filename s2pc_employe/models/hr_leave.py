# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HrLeave(models.Model):
	_inherit = 'hr.leave'

	@api.model
	def get_current_user_employee_team(self):
		manager = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)])
		employees = manager.mapped('team_employee_ids')
		return employees and employees.read(['id', 'name']) or {}

	def action_hr_leave_team(self):
		view_id = self.env.ref('s2pc_employe.hr_leave_team_view_gantt')
		manager = self.env['hr.employee'].search([('user_id', '=', self.env.user.id)])
		employees = manager.mapped('team_employee_ids')
		leaves = self.search([('employee_id', 'in', employees.ids)])
		domain = []
		if leaves:
			domain.append(('id', 'in', leaves.ids))

		return {
			'type': 'ir.actions.act_window',
			'name': _('My team leaves'),
			'res_model': self._name,
			'view_type': 'form',
			'view_mode': 'gantt',
			'view_id': view_id.id,
			'target': 'current',
			'domain': domain or [('id', 'in', [])],
			'context': dict(self._context),
		}