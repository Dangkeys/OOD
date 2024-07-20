# ณ เมืองแห่งหนึ่ง ที่มีชื่อว่า ... อืม (เอ้าผู้แต่งโจทย์คิดชื่อไม่ออก เอาเป็นว่าไม่ต้องสนใจก็ได้) จะมีบริการคมนาคมสาธารณะ 
# ซึ่งเป็นสิ่งที่น้อง ๆ พี่ ๆ อาจารย์ ๆ หรือ บุคคลอื่น ๆ ที่อาจจะคุณเคยกันหรือเคยนั้งก็มานั้นก็คือ "รถไฟฟ้า" นั้นเอง โดยแต่ละเมือง 
# จะเปรียบเหมือน Node ของ Linked List นั้นเอง ซึ่งรถไฟฟ้าจะมีทั้งขาไปขากลับนั้นเอง และ รถไฟฟ้าขาไป 
# ผ่านสถานีสุดท้ายของทางรถไฟฟ้าจะวนกลับมาสถานีแรก หรือในทางกลับกัน รถไฟฟ้าขากลับผ่านสถานีแรกก็จะวนกลับไปสถานีสุดท้ายเช่นกัน 
# เพื่อให้ "พี่โบ๊ท" ที่เป็นชาวเมืองนี้มีรถไฟฟ้านั้นไปทำงานหรือท่องเทียวในเมืองนี้ได้สะดวกขึ้น ต่อไปก็เป็นหน้าที่ของน้อง ๆ แล้วล่ะ 
# ที่จะสานฝันให้เมืองนี้และ "พี่โบ๊ท" มี ระบบรถไฟฟ้าที่ "สมบูรณ์แบบ" ที่สร้างขึ้นมาจากน้ำมือของน้องเองๆ 

# input จะเป็น
# บรรทัดแรก จะเป็น list ของ ชื่อสถาณี
# บรรทัดสอง จะเป็น สถานีต้นทาง,สถานีปลายทาง,ทิศทางของรถไฟฟ้า(ถ้าไม่ใส่ให้แสดงผลในขาที่ระยะทางสั้นที่สุด ถ้าเกิดเท่ากัน ให้แสดงผลลัพธ์ทั้งขาไปและขากลับ)
# โดย F จะเป็น รถไฟฟ้าขาไป
#   B จะเป็น รถไฟฟ้าขากลับ
# output จะเป็น
# แสดงการเดินทางของรถไฟฟ้า,จำนวนสถานีที่จะถึงปลายทาง
class Node:
    def __init__(self, data,prev = None, next = None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

class DoublyCircularList:
    def __init__(self) -> None:
        self.header = Node(None)
        self.trailer = Node(None,prev=self.header,next=self.header)
        self.header.prev = self.trailer
        self.header.next = self.trailer
        self.size = 0
    def append(self, data):
        node = Node(data)
        prev_trailer = self.trailer.prev
        prev_trailer.next = node
        node.prev = prev_trailer
        node.next = self.trailer
        self.trailer.prev = node
        self.size += 1
        # print(self)

    def __str__(self) -> str:
            log = ''
            current_node = self.header.next
            while current_node != self.trailer:
                log += str(current_node.data) + '->'
                current_node = current_node.next
            log = log.rstrip('->') if log else 'Empty'
            return log

    def add_stations(self, stations:str):
        station_list = stations.strip().split(',')
        [self.append(station) for station in station_list]

    def get_node_by_data(self, data):
        current_node = self.header.next
        while current_node.data != data:
            current_node = current_node.next
        return current_node
    
    def go_forward(self, source, destination) -> dict:
        log = 'Forward Route: '
        counter = 0
        current_node = self.get_node_by_data(source)
        destination_node = self.get_node_by_data(destination)
        
        if not current_node or not destination_node:
            return {"log": "Invalid source or destination", "counter": counter}

        while current_node != destination_node:
            if current_node == self.header or current_node == self.trailer:
                current_node = current_node.next
                continue
            log += str(current_node.data) + '->'
            current_node = current_node.next
            counter += 1
            
        log += str(current_node.data) + f',{counter}'
        return {"log": log, "counter": counter}
    
    def go_backward(self,source, destination)-> dict:
        log = 'Backward Route: '
        counter = 0
        current_node = self.get_node_by_data(source)
        destination_node = self.get_node_by_data(destination)
        if not current_node or not destination_node:
            return {"log": "Invalid source or destination", "counter": counter}
        
        while current_node != destination_node:
            if current_node == self.header or current_node == self.trailer:
                current_node = current_node.prev
                continue
            log += str(current_node.data) + '->'
            current_node = current_node.prev
            counter += 1
        log += str(current_node.data) + f',{counter}'
        return {"log":log,"counter":counter}
    
    def traveling(self,source, destination, direction=None):
        if direction == 'B':
            print(self.go_backward(source=source,destination=destination)["log"])
        elif direction == 'F':
            print(self.go_forward(source=source,destination=destination)["log"])
        elif not direction:
            go_forward = self.go_forward(source=source,destination=destination)
            go_backward = self.go_backward(source=source,destination=destination)
            
            if go_forward["counter"] > go_backward["counter"]:
                print(go_backward["log"])
            elif go_forward["counter"] < go_backward["counter"]:
                print(go_forward["log"])
            else:
                print(go_forward["log"])
                print(go_backward["log"])
    def run(self,user_input:str):
        stations, source_des_direction = [x for x in user_input.strip().split('/')]
        self.add_stations(stations)

        source_des_direction_list = source_des_direction.strip().split(',')

        if len(source_des_direction_list) == 2:
            source, destination = [x for x in source_des_direction_list]
            self.traveling(source=source,destination=destination)
        elif len(source_des_direction_list) == 3:
            source, destination, direction = [x for x in source_des_direction_list]
            self.traveling(source=source,destination=destination,direction=direction)

d_list = DoublyCircularList()
print('***Railway on route***')
user_input = input('Input Station name/Source, Destination, Direction(optional): ')
d_list.run(user_input)