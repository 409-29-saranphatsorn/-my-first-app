import itertools

def solve_24(numbers):
    """
    ฟังก์ชันค้นหาวิธีการคำนวณให้ได้ผลลัพธ์เท่ากับ 24
    """
    operators = ['+', '-', '*', '/']
    solutions = set()

    # ลองสลับหลักของตัวเลขทั้งหมด
    for nums in set(itertools.permutations(numbers)):
        # ลองสลับเครื่องหมายทั้ง 4 ตัว
        for ops in itertools.product(operators, repeat=3):
            # รูปแบบวงเล็บต่าง ๆ ที่เป็นไปได้
            patterns = [
                f"(({nums[0]} {ops[0]} {nums[1]}) {ops[1]} {nums[2]}) {ops[2]} {nums[3]}",
                f"({nums[0]} {ops[0]} ({nums[1]} {ops[1]} {nums[2]})) {ops[2]} {nums[3]}",
                f"{nums[0]} {ops[0]} (({nums[1]} {ops[1]} {nums[2]}) {ops[2]} {nums[3]})",
                f"{nums[0]} {ops[0]} ({nums[1]} {ops[1]} ({nums[2]} {ops[2]} {nums[3]}))",
                f"({nums[0]} {ops[0]} {nums[1]}) {ops[1]} ({nums[2]} {ops[2]} {nums[3]})"
            ]

            for expr in patterns:
                try:
                    # คำนวณค่าจากนิพจน์ (หลีกเลี่ยงการหารด้วยศูนย์)
                    if abs(eval(expr) - 24) < 1e-6:
                        solutions.add(expr)
                except ZeroDivisionError:
                    continue

    return list(solutions)

def main():
    # โจทย์ทั้ง 4 ข้อตามที่กำหนด
    puzzles = [
        {"id": 1, "numbers": [1, 7, 4, 5]},
        {"id": 2, "numbers": [6, 2, 0, 8]},
        {"id": 3, "numbers": [5, 7, 3, 9]},
        {"id": 4, "numbers": [2, 6, 6, 3]}
    ]

    print("=" * 45)
    print("      เฉลยเกม 24 สำหรับชุดตัวเลขทั้ง 4 ข้อ")
    print("=" * 45)

    for item in puzzles:
        nums = item["numbers"]
        print(f"\nข้อ {item['id']}. ตัวเลข: {nums}")
        results = solve_24(nums)

        if results:
            print(f"  พบ {len(results)} วิธีคำนวณ ตัวอย่างเช่น:")
            for solution in results[:3]:  # แสดงตัวอย่าง 3 วิธีแรก
                print(f"   • {solution} = 24")
        else:
            print("  ❌ ไม่มีวิธีคำนวณให้ได้ 24")

if __name__ == "__main__":
    main()
