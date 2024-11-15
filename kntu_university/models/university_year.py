from odoo import fields, models

class UniversityYear(models.Model):
    _name = "university.year"
    _description = "University year"

    name = fields.Char(string="Name")
    class_ids = fields.One2many("university.classes", inverse_name="year_id", string="Classes")
    active = fields.Boolean(string="Active",default=True)

