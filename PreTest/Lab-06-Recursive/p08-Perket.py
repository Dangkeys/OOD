""" 

“เปอร์เกต์” เป็นอาหารแสนอร่อยที่ใครๆก็รู้จักกัน และแน่นอนว่าส่วนผสมย่อมเป็นสิ่งที่ต้องพิถีพิถันอย่างยิ่ง
คุณมีส่วนผสมทั้งหมด N ชนิด แต่ละชนิดจะมีความเปรี้ยว S และความขม B เมื่อนำส่วนผสมมารวมกัน ความเปรี้ยว ลัพธ์ จะได้จากผลคูณของค่าความเปรี้ยวของทุกชนิดที่ใช้ ในขณะที่ความขมลัพธ์ จะได้จากผลบวกของความขมของ ทุกชนิดที่ใช้ ส่วนผสมที่ใช้นั้น
เปอร์เกต์ที่อร่อยที่สุดนั้น จะมีผลต่างค่าความเปรี้ยวลัพธ์และค่าความขมลัพธ์ของส่วนผสมทั้งหมดน้อยที่สุด และเรา จำเป็นต้องใช้ส่วนผสมอย่างน้อย 1 ชนิด
โจทย์ จงเขียนโปรแกรมเพื่อหาค่าผลต่างของความเปรี้ยวลัพธ์และความขมลัพธ์ของส่วนผสม ที่น้อยที่สุด

******* อธิบาย input
โดยส่วนผสมแต่ละชนิดจะแบ่งด้วย comma ( ' , ' ) โดยในแต่ละส่วนผสม จะมีจำนวนเต็มสองจำนวน S และ B คือค่าความเปรี้ยวและค่าความขมของ ส่วนผสมชนิดนั้น

******* รับประกันว่าสำหรับทุกข้อมูลนำเข้า เมื่อนำส่วนผสมทุกชนิดแล้ว จะได้ค่าความเปรี้ยวลัพธ์และความขมลัพธ์ ไม่เกิน 1,000,000,000

Enter Input : 3 10
7

Enter Input : 3 8,5 8
1

Enter Input : 1 7,2 6,3 8,4 9
1

"""

def find_sour(ingredients, index):
    if index == 0:
        return int(ingredients[index][0])
    else:
        return find_sour(ingredients, index-1) * int(ingredients[index][0])


def find_bitter(ingredients, index):
    if index == 0:
        return int(ingredients[index][1])
    else:
        return find_bitter(ingredients, index-1) + int(ingredients[index][1])


def perket(ingredients: list,index, current, bag):
    if index == len(ingredients):
        if len(current[:]) == 0:
            return
        bag.append(abs(find_sour(current[:], len(current[:])-1) - find_bitter(current[:], len(current[:])-1)))
        # print(current[:], find_sour(current[:], len(current[:])-1), find_bitter(current[:], len(current[:])-1))
        return
    
    current.append(ingredients[index])
    perket(ingredients, index+1, current, bag)
    current.pop()
    perket(ingredients, index+1, current, bag)

ingredients = [inp.split() for inp in input("Enter Input : ").split(',')]
bag = []
# print(ingredients)
perket(ingredients, 0, [], bag)
print(min(bag))