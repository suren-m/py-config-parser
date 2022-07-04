class ConfigCache(object):

    def __init__(self, max_items=2):
        self._max_items = max_items
        self.reset()
        

    def reset(self):
        self._number_of_items = 0
        self._config_cache = {}       
        self._hits = 0
        self._misses = 0


    def set(self, key, value):
        if self._number_of_items == self._max_items:
            self._config_cache.popitem() # Todo: remove least recently used item instead
        self._config_cache[key] = value
        self._number_of_items += 1

            
    def get(self, key):
        return self._config_cache[key]

    
    def has_key(self, key):
        return True if key in self._config_cache else False


    def increment_hits(self):
        self._hits += 1


    def increment_misses(self):
        self._misses += 1


    def get_hits_and_misses(self):
        return (self._hits, self._misses)
    

    def clear_cache(self):
        self.reset()

cache_obj = ConfigCache()
cache_obj.clear_cache()

def get_cache_obj():
    return cache_obj

def cache(fn):
    def wrapper(self, key):       

        if cache_obj.has_key(key):            
            data = cache_obj.get(key)
            cache_obj.increment_hits()
            return data
        else:                            
            data = fn(self, key)       
            cache_obj.set(key, data)
            cache_obj.increment_misses()
            return data

    return wrapper

