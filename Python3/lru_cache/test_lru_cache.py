"""
Brian Taylor Vann
https://github.com/taylor-vann
"""

import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_lru_cache_not_none(self):
        self.assertIsNotNone(LRUCache)


    def test_lru_cache_count_is_correct(self):
        cache = LRUCache(20)
        self.assertEqual(cache._count, 20)


    def test_lru_cache_contains_one(self):
        cache = LRUCache(2)
        cache.insert(5)

        self.assertIn(5, cache)


    def test_lru_cache_insert_two_contains_last(self):
        cache = LRUCache(2)
        cache.insert(5)
        cache.insert(4)

        self.assertIn(4, cache)


    def test_lru_cache_insert_three_doesnt_contain_first(self):
        cache = LRUCache(2)

        cache.insert(5)
        cache.insert(4)
        cache.insert(3)

        self.assertNotIn(5, cache)


    def test_lru_cache_insert_none_remove_one(self):
        cache = LRUCache(3)

        cache.insert(5)
        cache.insert(4)
        cache.insert(3)
        cache.remove(4)

        self.assertNotIn(4, cache)


    def test_lru_cache_insert_three_remove_uninserted(self):
        cache = LRUCache(3)

        cache.insert(5)
        cache.insert(4)
        cache.insert(3)
        cache.remove(6)

        self.assertNotIn(6, cache)


    def test_lru_cache_insert_none_remove_one(self):
        cache = LRUCache(3)

        cache.remove(4)

        self.assertNotIn(4, cache)


    def test_lru_cache_insert_three_update_one(self):
        cache = LRUCache(3)

        cache.insert(5)
        cache.insert(4)
        cache.insert(3)
        cache.update(4, 6)

        self.assertNotIn(4, cache)


    def test_lru_cache_insert_three_update_old_doesnt_exist(self):
        cache = LRUCache(3)

        cache.insert(5)
        cache.insert(4)
        cache.insert(3)
        cache.update(4, 6)

        self.assertIn(6, cache)


    def test_lru_cache_insert_three_update_uninserted(self):
        cache = LRUCache(3)

        cache.insert(5)
        cache.insert(4)
        cache.insert(3)
        cache.update(2, 6)

        self.assertNotIn(6, cache)


if __name__ == "__main__":
    unittest.main()
