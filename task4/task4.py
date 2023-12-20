import sys
def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = 0
    for num in nums:
        moves += abs(num - median)
    return moves


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error")
    else:
        input_file = sys.argv[1]

        with open(input_file, 'r') as f:
            nums = [int(line.strip()) for line in f]

        result = min_moves(nums)
        print(result)
