# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from datetime import timedelta

import pytz

from openerp import Model, fields, api, _
from openerp.exceptions import Warning

class ResPartner(Model):
    _inherit = 'res.partner'
    test_id = fields.Many2one('all.test', string='Test Model',
        readonly=False,
        help="Test Field")

class TestTags(Model):
    _name = 'all.test.tags'
    name = fields.Char('Name of Tag')

class AllTest(Model):
    _name = "all.test" 
    active = fields.Boolean("Active Testing", default=True, help="Activate or Deactivate a record")
    name = fields.Char("Name of the Recordset", required=True)
    date = fields.Date("Date Recordset", required=True, help="Date")
    int_test = fields.Integer("Integr Field", help="Integer Test")
    sequence = fields.Integer("Sequence Field", help="Integer Test")
    date_time = fields.Datetime("Date Recordset", required=True, help="Date")
    user_id = fields.Many2one('res.users', string='Responsible User',
        default=lambda self: self.env.user,
        readonly=False,
        help="MAny2One Field")
    signature = fields.Text('Signature', related='user_id.signature',
        store=True, readonly=False)
    partner_ids = fields.One2many('res.partner', 'test_id', string='Partners')
    tags = fields.Many2many('all.test.tags', help="SOme tags")

    @api.one
    def copy(self, default):
        """ Reset the state and the registrations while copying an event """
        default['name'] =  self.name+'Guarever'
        return super(AllTest, self).copy(default)
