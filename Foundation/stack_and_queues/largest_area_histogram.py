from operator import le


def largest_area_histogram(arr):

    right_boundry = [len(arr)]*len(arr)  # next smaller element to right
    left_boundry = [-1]*len(arr)  # next smaller element to left

    def fill_right_boundries(arr, right):
        # for on the right
        # travel reverse
        stack = [len(arr)-1]
        for i in range(len(arr)-2, -1, -1):
            while(len(stack) > 0 and arr[i] < arr[stack[-1]]):
                stack.pop()
            if len(stack) > 0:
                right[i] = stack[-1]
            stack.append(i)

    def fill_left_boundries(arr, left):
        stack = [0]
        for i in range(1, len(arr)):
            while(len(stack) > 0 and arr[i] < arr[stack[-1]]):
                stack.pop()
            if len(stack) != 0:
                left[i] = stack[-1]
            stack.append(i)

    fill_right_boundries(arr,right_boundry)
    fill_left_boundries(arr,left_boundry)
    max_area = 0
    for i in range(len(arr)):
        width = right_boundry[i]-left_boundry[i]-1
        height = arr[i]
        area = width * height
        if area > max_area:
            max_area=area
    print(max_area)
    
largest_area_histogram([6,2,5,4,5,1,6])