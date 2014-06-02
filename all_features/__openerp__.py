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


{
    'name': 'How a training must be given',
    'version': '0.1',
    'category': 'Test',
    'summary': 'Just for learning purpose avery commit has a concept to show',
    'description': """
Module to validate v8 new api features
======================================

A models with all type of fields.

- Char
- Text
- Date
- Datetime
- Selection
- html
- one2many
- many2one
- Related
- Property
- Function Recordable simple result.
- Funtion Recordable multiple result.

All orm methods

- read
- write
- create
- search
- default
- contrains
- with_context
""",
    'author': 'OpenERP SA',
    'depends': [
        'base_setup',
        'board',
        'email_template', 
        ],
    'data': [
    ],
    'demo': [
        'all_test_demo.xml',
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
