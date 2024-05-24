def bubble_sort(arr):
    n=len(arr)

    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        print(f"第{i+1}次的排序結果是{arr}")

        if not swapped:
            break

my_list=[33,67,8,13,54,119,3,84,25,41]

bubble_sort(my_list)

print("排序後的數列:")
for num in my_list:
    print(num,end=" ")