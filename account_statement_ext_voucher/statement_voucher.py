# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Joel Grand-Guillaume
#    Copyright 2011-2012 Camptocamp SA
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
from openerp.osv.orm import Model, fields


class AccountVoucher(Model):
    
    _inherit = 'account.voucher'

    def _get_period(self, cr, uid, context=None):
        """If perdiod not in context, take it from the move lines"""
        if context is None: context = {}
        if not context.get('period_id') and context.get('move_line_ids'):
            res = self.pool.get('account.move.line').browse(cr, uid , context.get('move_line_ids'))[0].period_id.id
            context['period_id'] = res
        return super(AccountVoucher, self)._get_period(cr, uid, context)

    def create(self, cr, uid, values, context=None):
        import pdb
        pdb.set_trace()
        """If no period defined in values, ask it from moves."""
        if values.get('period_id') == False and context.get('move_line_ids'):
            values['period_id'] = self._get_period(cr, uid, context)
        return super(AccountVoucher, self).create(cr, uid, values, context)
