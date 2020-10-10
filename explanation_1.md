# LRU Cache

I have decided to go with an OrderedDict structure because it has constant lookup time of O(1) given the key of the item stored in the dictionary. When getting/using an item from the dictionary it will be moved to the end. When inserting a new item it will be added as the last item in the dictionary. If the capacity is reached the first item is removed.

Space complexity -> O(n), n = capacity
Time complexity -> O(1) for both get and add methods
