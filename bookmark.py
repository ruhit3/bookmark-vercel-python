from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import json

with open("bookmarks.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

bmap = dict()

# header = {
#     'User-Agent':
#     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
# }

output_file_path = "Output.txt"
with open(output_file_path, "w+", encoding="utf8") as text_file:
    for tag in soup.find_all('a'):
        url = tag['href']

        # check if connection available
        # req = Request(url, headers=header)
        # try:
        #     response = urlopen(req)
        #     if response.getcode() != 200:
        #         print(url + ' '+ str(response.getcode()))
        # except Exception as e:
        #     print('Could not reach: ' + url + '\n')

        o = urlparse(url)
        hostname = o.hostname

        if hostname in bmap.keys():
            blist = bmap.get(hostname)
            blist.append(url)
            bmap.update({hostname: blist})
        else:
            bmap.update({hostname: [url]})

        # text_file.write("%s\n%s\n%s\n\n" % (tag.contents[0], url, o.hostname))

print(len(bmap))

with open('bookmarks.json', 'w+', encoding="utf8") as fp:
    json.dump(bmap, fp, sort_keys=True)
