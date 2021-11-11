import frappe
from frappe import _
from erpnext.accounts.utils import get_fiscal_year


@frappe.whitelist(allow_guest=True)
def get_sub_parameter_value(sub_parameter_name):
    result = frappe.db.sql("""select * from `tabInstaller Scoring Sub Parameter Value and Score` where parent='"""+sub_parameter_name+"""' """,as_dict=True)
    return result

@frappe.whitelist(allow_guest=True)
def get_sub_parameter_score(sub_parameter_value):
    result = frappe.db.sql("""select * from `tabInstaller Scoring Sub Parameter Value and Score` where sub_parameter_value='"""+sub_parameter_value+"""' """,as_dict=True)
    return result
