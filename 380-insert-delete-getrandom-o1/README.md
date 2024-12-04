## Problem: Insert Delete GetRandom O(1)

### Description:
Design a data structure that supports the following operations:
1. **insert(val)**: Inserts the item `val` into the set if not already present. Returns `true` if the item was inserted, `false` otherwise.
2. **remove(val)**: Removes the item `val` from the set if present. Returns `true` if the item was removed, `false` otherwise.
3. **getRandom()**: Returns a random element from the set. It is guaranteed that at least one element exists when this method is called. Each element must have the same probability of being returned.

### Approach:
- To perform all the operations in **O(1)** time complexity, we need to:
  1. **Insertion and Removal**: Use a combination of a list and a hashmap.
      - Use a list (`lst`) to store the elements for easy random access.
      - Use a hashmap (`index_map`) to store the index of each element in the list for quick lookups, which allows us to remove elements efficiently without having to search through the list.
  2. **getRandom()**: Simply use `random.choice()` to select a random element from the list.

### Operations:
1. **insert(val)**:
   - If the element is not in the hashmap, add it to both the list and the hashmap.
2. **remove(val)**:
   - If the element is in the hashmap, remove it from both the list and the hashmap, ensuring the removal is done efficiently without affecting the random access property.
3. **getRandom()**:
   - Use `random.choice()` on the list to get a random element.

### Time and Space Complexity:
- **Time Complexity**:
  - `insert(val)`: O(1)
  - `remove(val)`: O(1)
  - `getRandom()`: O(1)
- **Space Complexity**: O(n), where `n` is the number of elements in the set.


