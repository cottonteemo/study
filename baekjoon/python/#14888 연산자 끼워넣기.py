import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
plus, minus, multiply, divide = map(int, sys.stdin.readline().split())
process = [plus, minus, multiply, divide]
l = []
temp = []

def recursive(idx):
    global result
    global l
    global temp

    if idx == 0:
        result = nums[idx]
        temp.append(result)
        recursive(idx + 1)

    else:
        if idx == n:
            l.append(result)
            return

        for i in range(4):
            if process[i] == 0:
                continue

            process[i] -= 1
            if i == 0:
                result = result + nums[idx]
            if i == 1:
                result = result - nums[idx]
            if i == 2:
                result = result * nums[idx]
            if i == 3:
                if result < 0 and nums[idx] > 0:
                    result = (- result // nums[idx]) * -1
                else:
                    result = result // nums[idx]
            temp.append(result)
            recursive(idx + 1)
            process[i] += 1
            result = temp[idx - 1]
            del temp[idx]

recursive(0)
print(max(l))
print(min(l))