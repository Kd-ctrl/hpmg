import frappe
from hpmg.utils  import send_mail
import json

@frappe.whitelist()
def doc_notification(list):
    json_list = json.loads(list)
    for each_json in json_list:
        parent_doc_name = each_json.parent_name
        child_name = each_json.child_name
        doc_status = each_json.new_status
        doc_name =  each_json.document_name
        recepient = each_json.job_applicant,
        
        send_mail("Job Offer",parent_doc_name, recepient, f"Your {doc_name} Document has been {doc_status}", f"Reg: Submitted Document {doc_name}")
        
