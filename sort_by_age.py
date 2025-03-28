def sort_by_age(people):
    """Sort a list of (name, age) tuples by age in ascending order."""
    return sorted(people, key=lambda x: x[1])

# Example usage:
people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
print(sort_by_age(people))
# Output: [("Bob", 20), ("Alice", 25), ("Charlie", 30)]