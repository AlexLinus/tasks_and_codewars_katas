#https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python
#Extract the domain name from a URL
#import re
def domain_name(url):
    result = url.split("//")[-1].split("www.")[-1].split(".")[0]
    return result

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
domain_name("http://google.co.jp") == "google"
domain_name("www.xakep.ru") == "xakep"