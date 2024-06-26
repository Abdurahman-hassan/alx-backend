#!/usr/bin/python3
""" 100-lfu_cache """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache defines:
      - Caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.queue = []
        self.count = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.count[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    min_count = min(self.count.values())
                    keys = [k for k in self.count if self.count[k] == min_count]
                    for k in self.queue:
                        if k in keys:
                            break
                    self.queue.remove(k)
                    del self.cache_data[k]
                    del self.count[k]
                    print("DISCARD: {}".format(k))
                self.cache_data[key] = item
                self.count[key] = 1
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.count[key] += 1
            if key in self.queue:
                self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None

    def print_cache(self):
        """ Print the cache
        """
        for k in self.cache_data:
            print("{}: {}".format(k, self.cache_data[k]))
