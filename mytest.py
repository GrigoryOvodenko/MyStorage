import requests
import random


# for i in range(0,1000):
#     val = random.randint(1, 100000000000)
#     k = "ty" + str(random.randint(1, 10000000000))
#     print(i,i/1000)
#     x = requests.post(f"http://127.0.0.1:8000/putdata/",json={'key':k,'value':val})
#
#
#     if x.status_code !=200:
#         print(x)
#ty9694910498
#put data
#y = requests.post(f"http://127.0.0.1:8000/putdata/",json={'key':"ty53079386917765",'value':88})


y2 = requests.post(f"http://127.0.0.1:8000/getdata/",json={'key':"ty1357159654"})
print(y2.status_code)