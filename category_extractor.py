import pywikibot
site = pywikibot.Site()
repo = site.data_repository()
item = pywikibot.ItemPage(repo, 'Q3765867')

item.get()
if item.claims:
    if 'P31' in item.claims:  # instance of
        print(item.claims['P31'][0].getTarget())
        cat = item.claims['P31'][0].getTarget()
        cat.get()
        print(cat.labels["en"])
