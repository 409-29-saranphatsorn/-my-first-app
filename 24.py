import itertools

def solve_24(numbers):
    operators = ['+', '-', '*', '/']
    solutions = set()

    for nums in set(itertools.permutations(numbers)):
        for ops in itertools.product(operators, repeat=3):
            patterns = [
                f"(({nums[0]} {ops[0]} {nums[1]}) {ops[1]} {nums[2]}) {ops[2]} {nums[3]}",
                f"({nums[0]} {ops[0]} ({nums[1]} {ops[1]} {nums[2]})) {ops[2]} {nums[3]}",
                f"{nums[0]} {ops[0]} (({nums[1]} {ops[1]} {nums[2]}) {ops[2]} {nums[3]})",
                f"{nums[0]} {ops[0]} ({nums[1]} {ops[1]} ({nums[2]} {ops[2]} {nums[3]}))",
                f"({nums[0]} {ops[0]} {nums[1]}) {ops[1]} ({nums[2]} {ops[2]} {nums[3]})"
            ]

            for expr in patterns:
                try:
                    if abs(eval(expr) - 24) < 1e-6:
                        solutions.add(expr)
                except ZeroDivisionError:
                    continue

    return list(solutions)

# ส่วนสั่งรันแสดงผล
puzzles = [
    {"id": 1, "numbers": [1, 7, 4, 5]},
    {"id": 2, "numbers": [6, 2, 0, 8]},
    {"id": 3, "numbers": [5, 7, 3, 9]},
    {"id": 4, "numbers": [2, 6, 6, 3]}
]

for item in puzzles:
    nums = item["numbers"]
    print(f"ข้อ {item['id']} ตัวเลข {nums}:")
    ans = solve_24(nums)
    if ans:
        print(f"  -> {ans[0]} = 24")
    else:
        print("  -> ไม่มีคำตอบ")
