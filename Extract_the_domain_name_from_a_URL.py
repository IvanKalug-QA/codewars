# DESCRIPTION:
# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
#
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    for i in ['http://www.', 'http://', 'https://', 'www.']:
        if i in url:
            return url.replace(i,'').split('.')[0]
    return url.split('.')[0]