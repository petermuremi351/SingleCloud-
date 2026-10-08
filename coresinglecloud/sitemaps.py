from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority_map = {
        'home': 1.0,
        'service': 0.9,
        'about': 0.8,
        'contact': 0.8,
        'faq': 0.5,
        'terms': 0.3,
        'privacy': 0.3,
    }
    changefreq_map = {
        'home': 'weekly',
        'service': 'weekly',
        'about': 'monthly',
        'contact': 'monthly',
        'faq': 'monthly',
        'terms': 'yearly',
        'privacy': 'yearly',
    }

    def items(self):
        return list(self.priority_map.keys())

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        return self.priority_map.get(item, 0.5)

    def changefreq(self, item):
        return self.changefreq_map.get(item, 'monthly')
