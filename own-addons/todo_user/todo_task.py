# -*- coding: utf-8 -*-

from openerp import models, fields, api

class TodoTask(models.Model):
    _inherit = 'todo.task'
    name = fields.Char('What needs to be done?')
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')

    @api.one
    def do_toggle_done(self):
        if self.user_id != self.env.uid:
            raise Exception('Only responsible can do this!')
        else:
            return super(TodoTask, self).do_toggle_done()

    @api.multi
    def do_clear_done(self):
        domain = [('is_done', '=', True), '|', ('user_id', '=', self.env.uid), ('user_id', '=', False)]
        done_recs = self.search(domain)
        done_recs.write({'active': False})
        return True
