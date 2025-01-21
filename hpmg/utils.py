import frappe
def send_mail(reference_doctype,reference_name, recipients, msg, title, attachments=None):
    email_args = {
        "recipients":recipients,
        "message":msg,
        "subject":title,
        "reference_doctype":reference_doctype,
        "reference_name":reference_name,
    }
    
    frappe.enqueue(method = frappe.sendmail, queue = 'short', timeout = 300, **email_args)
