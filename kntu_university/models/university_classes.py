from odoo import fields, models

class UniversityClasses(models.Model):
    _name = "university.classes"
    _description = "University Classes"

    name = fields.Char(string="Name")
    year_id = fields.Many2one("university.year", string="Learning Year")
    plan_ids = fields.One2many("university.plan", inverse_name="class_id",string="Plans")
    active = fields.Boolean(string="Active",default=True)

