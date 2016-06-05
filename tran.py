import httplib, urllib2, argparse, re

def argparser():
    parser = argparse.ArgumentParser(description='Instant Translator')
    parser.add_argument('phrase', metavar='p', type=str,
                        help='phrase to translate')
    args = parser.parse_args()
    return args.phrase

def translate(to_translate, to_language="ru", language="auto"):
	agents = {'User-Agent':"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
	before_trans = 'class="t0">'
	link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_language, language, to_translate.replace(" ", "+"))
	request = urllib2.Request(link, headers=agents)
	page = urllib2.urlopen(request).read()
	result = page[page.find(before_trans)+len(before_trans):]
	result = result.split("<")[0]
	return result

def parse_item(item, depth = 0):
    if type(item) is str:
        if len(item) == 0:
            return ''
        return "{}{}\n".format("\t" * depth, item)
    result = ''
    for sub_item in item:
        result += parse_item(sub_item, depth + 1)
    return result

phrase = argparser()

response = translate(phrase)

print(response)
