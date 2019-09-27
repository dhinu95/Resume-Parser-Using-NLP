def extract_email_addresses(string):
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)
print('Mail id: ',extract_email_addresses(textinput))
