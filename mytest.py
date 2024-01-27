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
y = requests.post(f"http://127.0.0.1:8000/putdata/",json={'key':"ty53079386914",'value':45})