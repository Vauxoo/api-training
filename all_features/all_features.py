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

class AllTest(Model):
    _name = "all.test" 
    name = fields.Char("Name of the Recordset", required=True)
    date = fields.Date("Date Recordset", required=True)
    user_id = fields.Many2one('res.users', string='Responsible User',
        default=lambda self: self.env.user,
        readonly=False, states={'done': [('readonly', True)]})
