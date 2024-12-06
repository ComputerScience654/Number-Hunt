#นายศรัณย์กร ณชัยธนาทรัพย์ /465415241016, นายอัครพนธ์ ตางาม /465415241018 /CSS

import random

target = random.randint(1, 10)
count = 0

print("เกมทายตัวเลขระหว่าง 1 ถึง 10")
print("คุณมีโอกาสทายทั้งหมด 3 ครั้ง")
print("---------------------------------")

while True:
    if count < 3:
        try:
            num = int(input(f"ครั้งที่ {count + 1}: กรุณาใส่ตัวเลขของคุณ: "))

            if num < 1 or num > 10:
                print("กรุณาใส่ตัวเลขระหว่าง 1 ถึง 10")
                print("---------------------------------")
                continue

            if num > target:
                print("สูงไปนะ ลองทายใหม่!")
            elif num < target:
                print("ต่ำไปนะ ลองทายใหม่!")
            else:
                print()
                print("-- YOU WIN --")
                print(f"คุณทายถูกในครั้งที่ {count + 1}")
                break

            print("---------------------------------")
            count += 1

        except ValueError:
            print("กรุณาใส่ตัวเลขเท่านั้น!")
            print("---------------------------------")
            continue

    else:
        print("เสียใจด้วย คุณทายครบ 3 ครั้งแล้ว")
        print(f"เฉลย! ตัวเลขที่ถูกต้องคือ {target}")
        print("---------------------------------")
        break

