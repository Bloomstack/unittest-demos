from frappe import get_all, get_doc

class IamComplex:

    def __init__(self):
        pass

    def method1(self):
        return "I am method 1"

    def method2(self):
        return "I am method 2"

    def fetch_some_doc_and_do_work(self):
        """Imagine this method is doing some really hard processing here..."""
        doc = get_doc("Contact", 1234)

        # ... do some hard processing ...

        return True if doc.get("first_name") == "Tammy" \
            and doc.get("last_name") == "Alexander" else False

    def fetch_and_count_data(self):
        """Imagine this method fetches a list of doctypes only to count its result"""

        result = get_all("Customer")

        return len(result)