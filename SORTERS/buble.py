def bubble_sort(nums):
    swapped = True
    while swapped:
         swapped = False
         for i in range(len(nums) - 1):
             if nums[i] > nums[i + 1]:
                 # Меняем элементы
                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
                 # Устанавливаем swapped в True для следующей итерации
                 swapped = True