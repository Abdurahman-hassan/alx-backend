#!/usr/bin/python3
""" 3-lru_cache """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache defines:
      - Caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first = self.queue.pop(0)
                    del self.cache_data[first]
                    print("DISCARD: {}".format(first))
                self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
