""" 

อยากรู้ว่า วงเล็บ เนี้ยสามารถเข้าคู่ได้กี่แบบกัน จากจำนวนคู่ที่กำหนดให้
แค่นี้แหละ ไม่ยากเกินความสามารถน้อง ๆ

ห้ามใช้ for while loop. Only Recursion is allowed.

Enter number of pair parenthesis(es): 1
All possible parenthesis(es)
()

Enter number of pair parenthesis(es): 2
All possible parenthesis(es)
(()),()()

Enter number of pair parenthesis(es): 3
All possible parenthesis(es)
((())),(()()),(())(),()(()),()()()

Enter number of pair parenthesis(es): 4
All possible parenthesis(es)
(((()))),((()())),((())()),((()))(),(()(())),(()()()),(()())(),(())(()),(())()(),()((())),()(()()),()(())(),()()(()),()()()()

"""

def generateParenthesis(left, right, s, answer):
	# terminate
	if left == 0 and right == 0:
		answer.append(s)
	if left > right or left < 0 or right < 0:
		# wrong
		# print("err", left, right, s)
		return
	s += '('
	generateParenthesis(left - 1, right, s, answer)
	s = s[:-1]
	s += ')'
	generateParenthesis(left, right - 1, s, answer)
	s = s[:-1]


n = int(input('Enter number of pair parenthesis(es): '))
print("All possible parenthesis(es)")
ans = []
s = ""
generateParenthesis(n, n, s, ans)
print(','.join(ans))
