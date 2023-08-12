# DESCRIPTION:
# Complete the function/method so that it returns the url with
#anything after the anchor (#) removed.
#
# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"

import re
def remove_url_anchor(url):
    result = re.search(r'#\D{,40}', url)
    if not result:
        return url
    r = result[0]
    url = url.replace(r,'')
    return url