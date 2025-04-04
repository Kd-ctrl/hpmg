import frappe


def send_mail(reference_doctype, reference_name, recipients, msg, title, attachments=None):
    email_args = {
        "recipients": recipients,
        "message": msg,
        "subject": title,
        "reference_doctype": reference_doctype,
        "reference_name": reference_name,
        "attachments": attachments if attachments else [],
    }
    
    frappe.enqueue(method=frappe.sendmail, queue='short', timeout=300, **email_args)


@frappe.whitelist()
def get_documents_by_location(location_name):
    try:
        all_docs = []
        # Query to fetch documents from child table
        results = frappe.db.sql("""
            SELECT parent AS name
            FROM `tabLocation List`
            WHERE location = %s
        """, (location_name,), as_dict=True)

        for each_doc in results:
           all_docs.append(frappe.get_all("Location Linking", filters = {"name":each_doc["name"]}, fields = ["*"]))
        
        return all_docs
    except Exception as e:
        frappe.log_error(f"Error fetching documents for location {location_name}: {str(e)}")
        frappe.throw(f"An error occurred: {str(e)}")

