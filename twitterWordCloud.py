from os import path
import matplotlib.pyplot as plt
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS
from np_extractor import NPExtractor
import json
from ConfigParser import SafeConfigParser
from getUserTimeline import get_users

# load config file
config = SafeConfigParser()
script_dir = path.dirname(__file__)
config_file = path.join(script_dir, 'config/settings.cfg')
config.read(config_file)

# tell script where to put the JSON files returned
logfile = config.get('files','logfile')
listfile = config.get('files','listfile')
outfolder = config.get('files','outfolder')

# get usernames
users = get_users(listfile)

# add stop words
STOPWORDS.add('https')

# create a word cloud for each user
for user in users:

    # get image masks for different users
    # from http://masterkoyo.deviantart.com/art/Template-Donald-Trump-35925789
    # from https://openclipart.org/detail/211473/jeb-bush-outlines
    # from http://www.spstencils.com/shop/politics/hilary-clinton-stencil/
    image_mask = None
    try:
        image_mask = imread(path.join(script_dir, ".".join([user,'jpg'])))
        print user
    except IOError:
        print 'Cannot open file '+ user + '.jpg under directory ' + script_dir

    # Read json
    filename = ".".join([user,'json'])
    f = open(path.join(outfolder, filename))    

    try:
        tweets = json.loads(f.read())
    except ValueError as err:
        print ('%s in %s' % (err, filename))
    f.close()

    text = ''
    for tweet in tweets:
        text += ' ' + tweet['text']
    np_extractor = NPExtractor(text)
    result = np_extractor.extract()

    # make word cloud
    wordcloud = WordCloud(background_color = 'white', max_words = 500, max_font_size = 80, mask = image_mask, relative_scaling = .5, stopwords = STOPWORDS)
    wordcloud.generate(' '.join(result))
    # wordcloud.generate(text)

    # store pic
    picname = "_".join([user,'wc.png'])
    wordcloud.to_file(path.join(outfolder, picname))


