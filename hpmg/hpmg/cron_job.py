from datetime import datetime 
import frappe

def job_offer_due():
    today_str = datetime.now().strftime("%Y-%m-%d")
    job_offer_list = frappe.get_all('Job Offer', filters={'status': 'Offer Sent'}, fields=["*"])
    for job_offer in job_offer_list:
        if today_str > job_offer["due_date"]:
            frappe.set_value("Job Offer",job_offer["name"],"workflow_state","Candidate Withdrew")
            frappe.db.commit()
