import math
import cmath
from .hopter import Error_pta

#Ordinary calculations
def caculate(num):
  num_logos = ['+','-','*','/','%','|','&','^','~','>>','<<']
  for i in num_logos:
    if i in num:
      try:
        print('\033[92m'+str(eval(num)))
      except SyntaxError as e:
        Error_pta('SyntaxError','Command',str(e),num)
      except ZeroDivisionError as e:
        Error_pta('ZeroDivisonError','Command',str(e),num)
    else:
      try:
        print('\033[92m'+str(eval(num)))
      except SyntaxError as e:
        Error_pta('SyntaxError','Command',str(e),num)
      except NameError as e:
        Error_pta('NameError','Command',str(e),num)
    break

#Root number calculation
def root_caculate(num):
  try:
    if float(num) >= 0:
      print('\033[92m'+str(math.sqrt(float(num))))
    else:
      print('\033[92m'+str(cmath.sqrt(float(num))))
  except SyntaxError as e:
    Error_pta('SyntaxError','Command',str(e),'caculate √'+num)

#Absolute value calculation
def abs_caculate(num):
  try:
    print('\033[92m'+str(abs(float((answer[10:len(answer)-1])))))
  except SyntaxError as e:
    Error_pta('SyntaxError','Command',str(e),'caculate |{}|'.format(num))

#Trigonometric computation
def triangle_caculate(nums):
  symbol = ['sin','cos','tan','asin','acos','atan']
  for type in range(len(symbol)):
    if symbol[type] in nums:
      num = nums[len(symbol[type]):]
      print(num)
  try:
    if type == 0:
      print(math.sin(math.radians(float(num))))
    elif type == 1:
      print(math.cos(math.radians(float(num))))
    elif type == 2:
      print(math.tan(math.radians(float(num))))
    elif type == 3:
      print(math.asin(math.radians(float(num))))
    elif type == 4:
      print(math.acos(math.radians(float(num))))
    elif type == 5:
      print(math.atan(math.radians(float(num))))
  except SyntaxError as e:
    Error_pta('SyntaxError','Command',str(e),'triangle …')

#Other calculations