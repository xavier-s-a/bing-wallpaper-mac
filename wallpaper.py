import os
import urllib2
import json
import errno


directory = '/Users/' + os.environ.get('USER') + '/Desktop/test'
if not os.path.exists(directory):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

bing_url = 'http://www.bing.com'
url = bing_url + '/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-IN'

content = json.load(urllib2.urlopen(url))
image_url = bing_url + content['images'][0]['url']
highre = image_url.replace("1080", "1200")
test = content['images'][0]['wp']
name = image_url.split('/')[-1]
nameh = highre.split('/')[-1]
if test:
 highres = nameh.replace( nameh, "BingINToday.jpg")
 response = urllib2.urlopen(highre)
 image_path = directory + '/' + highres
if not test:
 lowres = name.replace( name, "BingINToday.jpg")
 response = urllib2.urlopen(image_url)
 image_path = directory + '/' + lowres

with open(image_path, 'w') as f:
    f.write(response.read())


os.system("""osascript -e 'tell application "System Events" to tell every desktop to set picture to "{}"'""".format(image_path))


