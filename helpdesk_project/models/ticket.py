from odoo import models, api, fields, _

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project')

    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task')

    @api.onchange('task_id')
    def _onchange_task_id(self):
        if self.task_id and self.task_id.project_id:
            self.project_id = self.task_id.project_id
        else:
            self.project_id = False

    @api.onchange('project_id')
    def _onchange_project_id(self):
        if self.project_id:
            domain = {'task_id': [('project_id', '=', self.project_id.id)]}
        else:
            domain = {}
        return {'domain': domain}

    def link_project_view(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Project',
            'view_mode': 'tree',
            'res_model': 'project.project',
            'domain': [('id', '=', self.project_id.id)],
        }

    def link_task_view(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Task',
            'view_mode': 'form',
            'res_model': 'project.task',
            'domain': [('id', '=', self.task_id.id)],
        }
