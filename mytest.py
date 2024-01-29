import requests
import random

import time

# for i in range(0,400):
#     val = random.randint(1, 100000000000)
#     k = "ty" + str(random.randint(1, 10000000000))
#     print(i,i/1000)
#     x = requests.post(f"http://127.0.0.1:5000/putdata/",json={'flag':False,'key':k,'value':val})

#
#     if x.status_code !=200:
#         print(x)
# ty9694910498
# put data
# y1 = requests.post(f"http://127.0.0.1:8000/putdata/",json={'key':"143434",'value':'990sdfj','flag':False})
# print(y1.json())
# #
# y2 = requests.post(f"http://127.0.0.1:8000/getdata/",json={'key':"143434"})
# print(y2.json())
# # #
# y3= requests.post(f"http://127.0.0.1:8000/deldata/",json={'key':"143434"})
# print(y3.json(),y3.status_code)
# # #
# y4= requests.post(f"http://127.0.0.1:8000/findkeys/",json={'value':'99'})
# print(y4.json(),y4.status_code)

# y5= requests.post(f"http://127.0.0.1:8000/opentransaction/",json={'task':'putdata','data':{'key':"5sf143434",'value':'97'}})
# print(y5.json(),y5.status_code)
# #deldata
y6 = requests.post(
    f"http://127.0.0.1:8000/opentransaction/",
    json={"task": "deldata", "data": {"key": "ty7173709552"}},
)
print(y6.json(), y6.status_code)
# time.sleep(15)
# y7=requests.post("http://127.0.0.1:5000/rollbackapp")
# print(y7.status_code,y7.json())
