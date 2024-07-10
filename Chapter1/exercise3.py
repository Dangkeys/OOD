# โรงเรียนดังประจำจังหวัดแห่งหนึ่ง จะมีการจัดการเลือกตั้งหาประธานนักเรียนคนใหม่ขึ้นในทุกๆปี โดยในปีนี้มีผู้เข้าแข่งขันสูงถึง 20 คน 
# โดยกฤษฎาได้รับมอบหมายให้เป็นผู้นับคะแนนเลือกตั้งในปีนี้ แต่กฤษฎารู้สึกขี้เกียจนับคะแนนขึ้นมา จึงได้ไหว้วานให้คุณช่วยเขียนโปรแกรม 
# ในการหาว่าผู้เข้าแข่งขันคนใดได้รับคะแนนสูงที่สุด

# ข้อควรระวัง หากมีการเลือกเลขที่ไม่ตรงกับผู้เข้าแข่งขัน (1-20) จะนับว่าเป็นบัตรเสีย และถ้าหากทุกใบเป็นบัตรเสียจะถือว่าไม่มีผู้ชนะ


print('*** Election ***')
number_of_voter = input('Enter a number of voter(s) : ')
candidate_list = [int(x) for x in input('').split()]
candidate_dict = {candidate: candidate_list.count(candidate) for candidate in candidate_list if candidate >= 1 and  candidate <= 20 }


winner = ' '.join([str(x) for x in sorted([winner for winner in candidate_dict if candidate_dict[winner] == max(candidate_dict.values())])])

print(winner if winner else '*** No Candidate Wins ***')