import unittest
from cellxgene_gateway.cache_entry import CacheEntry
from cellxgene_gateway.cache_key import CacheKey

key = CacheKey('path/part', 'dataset', 'tmp.csv')

class TestRenderEntry(unittest.TestCase):
    def test_GIVEN_absolute_static_url_THEN_return_relative(self):
        actual = CacheEntry.for_key(key, 8000).rewrite_text_content("src:url(/static/assets/")
        expected = "src:url(static/assets/"
        self.assertEqual(actual, expected)
    def test_GIVEN_absolute_src_THEN_return_relative(self):
        actual = CacheEntry.for_key(key, 8000).rewrite_text_content('<link rel="shortcut icon" href="/static/assets/favicon.ico">')
        expected = '<link rel="shortcut icon" href="static/assets/favicon.ico">'
        self.assertEqual(actual, expected)

