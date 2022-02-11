Utile ?
# Pour github
DIRECT_TEMPLATES = (('index', 'blog', 'tags', 'categories', 'archives'))
PAGINATED_DIRECT_TEMPLATES = (('output',))
TEMPLATE_PAGES = {'home.html': 'index.html',}

$ pelican content -o output -s pelicanconf.py
$ ghp-import output -b gh-pages
$ git push origin gh-pages

git checkout gh-pages / master


