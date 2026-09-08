import itertools

# ชุดตัวเลขจากโจทย์
numbers_sets = [
    [1, 7, 4, 5],
    [6, 2, 0, 8],
    [5, 7, 3, 9],
    [2, 6, 6, 3]
]

def solve_24(nums):
    operators = ['+', '-', '*', '/']
    solutions = set()
    
    # สลับหลักตัวเลข
    for p in itertools.permutations(nums):
        # สลับเครื่องหมาย
        for o1, o2, o3 in itertools.product(operators, repeat=3):
            # รูปแบบวงเล็บต่าง ๆ
            patterns = [
                f"(({p[0]} {o1} {p[1]}) {o2} {p[2]}) {o3} {p[3]}",
                f"({p[0]} {o1} ({p[1]} {o2} {p[2]})) {o3} {p[3]}",
                f"{p[0]} {o1} (({p[1]} {o2} {p[2]}) {o3} {p[3]})",
                f"{p[0]} {o1} ({p[1]} {o2} ({p[2]} {o3} {p[3]}))",
                f"({p[0]} {o1} {p[1]}) {o2} ({p[2]} {o3} {p[3]})"
            ]
            
            for expr in patterns:
                try:
                    # คำนวณผลลัพธ์ ป้องกันปัญหาเรื่องเลขทศนิยม
                    if abs(eval(expr) - 24) < 1e-6:
                        solutions.add(expr)
                except ZeroDivisionError:
                    pass  # ข้ามกรณีหารด้วย 0
                    
    return solutions

# แสดงผลลัพธ์
for i, nums in enumerate(numbers_sets, 1):
    results = solve_24(nums)
    print(f"=== ชุดที่ {i}: {nums} (พบทั้งหมด {len(results)} วิธี) ===")
    for expr in sorted(results)[:5]:  # แสดงตัวอย่าง 5 วิธีแรก
        print(f"  • {expr} = 24")
    print()
