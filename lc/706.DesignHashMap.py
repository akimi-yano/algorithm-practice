# 706. Design HashMap
# Easy

# 1416

# 155

# Add to List

# Share
# Design a HashMap without using any built-in hash table libraries.

# To be specific, your design should include these functions:

# put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

# Example:

# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);          
# hashMap.put(2, 2);         
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1 
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found) 

# Note:

# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.

# This solution works:

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = [-1 for _ in range(1000000)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        
        self.storage[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.storage[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.storage[key] = -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# This solution works - optimization using buckets:

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_keys = 0
        self.buckets = [[]]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # if we have 50% capacity filled, resize
        if self.num_keys >= len(self.buckets):
            new_buckets = [[] for _ in range(len(self.buckets) * 2)]
            for bucket in self.buckets:
                for k, v in bucket:
                    new_bucket_index = k % len(new_buckets)
                    new_bucket = new_buckets[new_bucket_index]
                    new_bucket.append((k, v))
            self.buckets = new_buckets
        
        # put this key into the bucket
        bucket_index = key % len(self.buckets)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.num_keys += 1

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket_index = key % len(self.buckets)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket_index = key % len(self.buckets)
        bucket = self.buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i], bucket[-1] = bucket[-1], bucket[i]
                bucket.pop()
                self.num_keys -= 1
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)