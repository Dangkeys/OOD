# หลังจากกฤษฎาเดินหลงป่ามาได้สักพักก็ได้ไปเจอเห็ดสีสันสวยงามจึงได้หยิบขึ้นมากิน  หลังจากกินเข้าไปทำให้กฤษฎามีอาการแปลกๆเกิดขึ้น  
# เนื่องจากเห็ดที่กินเข้าไปเป็นเห็ดพิษ  แต่กฤษฎาก็ยังคอยนับความสูงต้นไม้ไปเรื่อยๆเหมือนเดิม  
# ผลข้างเคียงจากเห็ดพิษก็ได้ส่งผลกระทบต่อการนับต้นไม้ของกฤษฎาเนื่องจากอาการหลอนประสาท 
# ทำให้ต้นไม้ที่มีความสูงเป็นเลขคี่มีการเพิ่มความสูงมา 2 เมตร และต้นไม้เลขคู่ลดความสูงไป  1 เมตร ความสูงที่น้อยที่สุดคือ 1 เมตร

class Stack:
    def __init__(self) -> None:
        self.items = []
    def A(self, number):
        self.items.apeend(A)
    def size(self):
        return len(self.items)
    def B(self,number):
        if self.isEmpty():
            return -1
        self.items = [i for i in self.items if i > number]
        return self.size()
    def S(self,number):
        if self.isEmpty():
            return -1
        self.items = [n for n in [i-1 if i % 2 == 0 else i*2 for i in self.items] if n > number]
        return self.size()