import argparse
import urllib.request


def argparser():
    parser = argparse.ArgumentParser(description='Instant Translator')
    parser.add_argument('phrase', metavar='p', type=str,
                        help='phrase to translate')
    parser.add_argument('to_lang', metavar='tl', type=str, default='ru',
                        help='language the pharase will be translated to')
    parser.add_argument('from_lang', metavar='fl', type=str, default='auto',
                        help='language the phrase will be tranlated from')
    args = parser.parse_args()
    return args


def translate(to_translate, to_language="pt", language="auto"):
    agents = {'User-Agent': "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}
    link = "http://translate.google.com/m?hl=%s&sl=%s&q=%s" % (to_language, language, to_translate.replace(" ", "+"))
    request = urllib.request.Request(url=link, headers=agents)
    page = urllib.request.urlopen(request).read().decode('utf-8')
    return page.split('class="t0">')[1].split('</div>')[0]


args = argparser()
print(translate(args.phrase, args.to_lang, args.from_lang))
