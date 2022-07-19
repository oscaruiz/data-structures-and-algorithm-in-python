"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
#Code based on http://code.doncharlie.xyz/quick-sort

def quicksort(array):
    quick_sort_recursive(array, 0, len(array)-1)
    return array

# Quick Sort algorithm
def quick_sort_recursive(array, low, high):
  # Low and high serve as indexes in the list
  if low < high:
      # Get the partition index using partition function below
      p_index = partition(array, low, high)

      # Call quick_sort from low to pivot index, and from pivot index + 1 to high
      quick_sort_recursive(array, low, p_index - 1)
      quick_sort_recursive(array, p_index + 1, high)

# Partition function
def partition(array, low, high):
  # Use last item as pivot
  pivot = array[high]
  i = low
  for j in range(low, high):
      # Move lower items to left of pivot
      if array[j] < pivot:
          array[i], array[j] = array[j], array[i]
          i += 1
  # Move pivot to its right position
  pivot_index = i
  array[pivot_index], array[high] = array[high], array[pivot_index]
  return pivot_index

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)