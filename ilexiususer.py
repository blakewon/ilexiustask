from odoo import api, models, fields, http

class ilexiusUser(models.Model):
    _inherit = 'res.users' 
    alphanumeric_id = fields.Char(string="Alphanumeric ID",required=False, readonly= False)
    login_success_count = fields.Integer(string="Successful Logins", compute='compute_logins')

    def compute_logins(self):
        cr = self.env.cr
        for record in self:
            cr.execute("SELECT * FROM res_users_log WHERE create_uid = %s;" % (record.id))
            record.login_success_count += cr.rowcount



