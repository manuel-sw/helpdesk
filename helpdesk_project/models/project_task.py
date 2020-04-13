from odoo import models, api, fields, _

class ProjectTask(models.Model):
    _inherit = 'project.task'

    ticket_ids = fields.One2many(
        comodel_name='helpdesk.ticket',
        inverse_name='task_id',
        string='Tickets')

    ticket_count = fields.Integer(
        compute='_compute_ticket_count',
        string="Number of tickets")

    @api.depends('ticket_ids')
    def _compute_ticket_count(self):
        for task in self:
            task.ticket_count = len(task.ticket_ids)


    def action_new_ticket(self):
        action = self.env.ref("help_project.task_action_ticket_new").read()[0]
        action['context'] = {
            'default_task_id': self.id,
            'default_project_id': self.project_id and self.project_id.id,
        }
        return action

    def action_view_tickets(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Tickets',
            'view_mode': 'tree',
            'res_model': 'helpdesk.ticket',
            'domain': [('task_id', '=', self.id)],
        }
