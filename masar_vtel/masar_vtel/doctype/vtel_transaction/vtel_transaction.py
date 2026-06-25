# Copyright (c) 2026, KCSC and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt


class VTELTransaction(Document):
	def validate(self):
		self.set_title()
		self.set_totals()

	def set_title(self):
		parts = [p for p in (self.entry_type, self.voucher_no) if p]
		self.title = " - ".join(parts) or self.name

	def set_totals(self):
		self.total_debit = sum(flt(d.debit) for d in self.accounts)
		self.total_credit = sum(flt(d.credit) for d in self.accounts)
		self.difference = flt(self.total_debit) - flt(self.total_credit)
    