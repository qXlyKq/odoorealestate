from odoo import fields, models

class UniversityPlan(models.Model):
    _name = "university.plan"
    _description = "University plan for learning year"

    name = fields.Char(string="Name", store=True, compute='_compute_name')
    year_id = fields.Many2one("university.year",string="Learning Year", related='class_id.year_id', store=True)
    class_id = fields.Many2one("university.classes",string="Class")
    active = fields.Boolean(string="Active",default=True)
    count = fields.Integer(string="Student count")


    def _compute_name(self):
        return self.year_id.name