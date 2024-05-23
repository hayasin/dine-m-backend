import requests

def send_mail_via_mailgun(api_key, domain_name, from_email, recipients, subject, text):
    url = f"https://api.mailgun.net/v3/{domain_name}/messages"
    auth = ("api", api_key)
    data = {
        "from": from_email,
        "to": recipients,
        "subject": subject,
        "text": text
    }
    
    response = requests.post(url, auth=auth, data=data)
    return response

# Example usage
api_key = '5d60e75b99a19ef23db6d4507d72a523-86220e6a-641505a1'  # Replace 'YOUR_API_KEY' with your actual Mailgun API key
domain_name = 'sandboxeb547aa62249414cac58aa5f201256ff.mailgun.org'  # Replace 'YOUR_DOMAIN_NAME' with your Mailgun domain
from_email = 'Excited User <postmaster@sandboxeb547aa62249414cac58aa5f201256ff.mailgun.org>'  # Replace YOUR_DOMAIN_NAME in the email
recipients = ['recipient-1@example.com', 'recipient-2@example.com']  # List of email recipients
subject = 'Hello there!'
text = 'Testing some Mailgun awesomeness!'

response = send_mail_via_mailgun(api_key, domain_name, from_email, recipients, subject, text)
print("Status Code:", response.status_code)
print("Response Body:", response.text)
