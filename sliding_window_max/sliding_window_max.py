'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Your code here

    window = []
    max_nums = []
    for i in range(len(nums)):
        while window and nums[window[-1]] <= nums[i]:
            window.pop()
        # add the index of the current number to que
        window.append(i)
        # if the index in the front of the que is outside of the window, remove it
        if window[0] == i - k:
            window = window[1:]
        # once current index is at the end of window, add the first item in window
        if i >= k - 1:
            max_nums.append(nums[window[0]])
    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
