AUTHOR = 'Stéphane Manet'
SITENAME = 'Sciences & Conscience'
SITEURL = ''

# Pour github
DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
PAGINATED_DIRECT_TEMPLATES = (('blog',))
TEMPLATE_PAGES = {'home.html': 'index.html',}

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

THEME = 'themes/alpha'
THEME_STATIC_DIR = 'static'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Rss', 'solid fa-rss', 'https://cause-commune.fm/feed/podcast/sciences-et-conscience'),
          ('Youtube', 'brands fa-youtube', 'https://twitter.com/SConscienceCC'),
          ('Discord', 'brands fa-discord', 'https://twitter.com/SConscienceCC'),
          ('Twitter', 'brands fa-twitter', 'https://twitter.com/SConscienceCC'),
          ('Github', 'brands fa-github', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True