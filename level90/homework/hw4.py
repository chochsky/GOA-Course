import re

def domain_name(url):
    # Use regex to match the domain name
    match = re.search(r'^(?:https?://)?(?:www\.)?([^./]+)', url)
    return match.group(1) if match else None
