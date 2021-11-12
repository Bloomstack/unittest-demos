from faker import Faker
fake = Faker()

def get_doc(doctype, docname):
    fake.seed_instance(docname)
    return { "name": docname, "doctype": doctype, "first_name": fake.first_name(), "last_name": fake.last_name()}

def get_all(doctype):
    fake.seed_instance(0)
    result = []
    for i in range(0, 10):
        result += [{ "name": i, "doctype": doctype, "first_name": fake.first_name(), "last_name": fake.last_name()}]

    return result

