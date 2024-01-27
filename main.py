from fastapi import FastAPI, HTTPException, status
from fastapi.responses import PlainTextResponse,UJSONResponse
from models import SaveDataClass,GetDataClass
import CommonFunctions


import os
app = FastAPI()
namefile = "storage.txt"
namefilelog = "logjournal.txt"
commonfunctions =CommonFunctions(namefile,namefilelog)
commonfunctions.create_file()
commonfunctions.create_file()
flag =False
# сохранить значение по ключу
@app.post("/putdata")
async def putdata(savedataclass:SaveDataClass):
    savedataclass_dict = savedataclass.dict()

    # в случае если транзакций открытых нет
    if flag == False:


        #!check
        key = savedataclass_dict['key']
        value = savedataclass_dict['value']
        fl,indfound,valuefound = commonfunctions.get_my(key)
        print("fl check:",fl,key,value,indfound)
        if fl == False:
            # we will delete because we have data and insert new
            print("NO:")
            commonfunctions.deletedata(indfound)
            commonfunctions.insdata( key, value)
        else:
            # we record new
            print("YES:")
            commonfunctions.insdata(key,value)
    else:
        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Another transaction is opened",
                        )

    return [{}]

@app.post("/getdata")
async def getdata(getdataclass:GetDataClass):
    getdataclass_dict = getdataclass.dict()
    # в случае если транзакций открытых нет
    if flag == False:
        print(getdataclass_dict)
        print(namefile)
        #!check
        key = getdataclass_dict['key']

# @app.post("/schedulerpoint", response_class=PlainTextResponse)
# async def taskmanager(scheduler: Scheduler):
#     scheduler_dict = scheduler.dict()
#
#     result_dict = {key: [] for key in scheduler_dict.keys()}
#     sch_dict_numb1 = {key: i for i, key in enumerate(scheduler_dict.keys())}
#     sch_dict_numb2 = {i: key for i, key in enumerate(scheduler_dict.keys())}
#
#     flag = 0
#     lsttypes = []  # check duplicates types
#     setdaytoday = set()
#     current_day = ""
#     for k in scheduler_dict.keys():
#         stime = ""
#         if flag == 1:
#             if len(scheduler_dict[k]) == 0:
#                 raise HTTPException(
#                     status_code=status.HTTP_400_BAD_REQUEST,
#                     detail=f"""validation failed(interval not closed {current_day}
# {sch_dict_numb2[sch_dict_numb1[current_day]+1]})""",
#                 )
#
#             for ind, elem in enumerate(scheduler_dict[k]):
#                 type_ = elem["type"]
#                 value_ = elem["value"]
#
#                 if value_ > 86399 or value_ < 0:
#                     raise HTTPException(
#                         status_code=status.HTTP_400_BAD_REQUEST,
#                         detail=f"validation failed value must be 0<value<=86399",
#                     )
#
#                 CommonFunctions.checkdoubles(type_, lsttypes)
#                 lsttypes.append(type_)
#                 if type_ != "open" and type_ != "close":
#                     raise HTTPException(
#                         status_code=status.HTTP_400_BAD_REQUEST,
#                         detail=f"validation failed type must be open or close",
#                     )
#
#                 if ind == len(scheduler_dict[k]) - 1:
#                     if type_ == "open":
#                         setdaytoday.add(k)
#                 if type_ == "open":
#                     newvalueh = CommonFunctions.calcvalue(value_)
#                     stime += newvalueh + "-"
#
#                     flag = 1
#                     current_day = k
#
#                 if type_ == "close":
#                     if ind == 0:
#                         newvalueh = CommonFunctions.calcvalue(value_)
#
#                         result_dict[current_day][-1] += newvalueh
#
#                     else:
#                         newvalueh = CommonFunctions.calcvalue(value_)
#                         if ind != len(scheduler_dict[k]) - 1:
#                             stime += newvalueh + ","
#
#                         else:
#                             stime += newvalueh
#
#                         flag = 2
#
#             result_dict[k].append(stime)
#
#         else:
#             for ind, elem in enumerate(scheduler_dict[k]):
#                 type_ = elem["type"]
#                 value_ = elem["value"]
#
#                 if value_ > 86399 or value_ < 0:
#                     raise HTTPException(
#                         status_code=status.HTTP_400_BAD_REQUEST,
#                         detail=f"validation failed value must be 0<value<=86399",
#                     )
#
#                 CommonFunctions.checkdoubles(type_, lsttypes)
#                 lsttypes.append(type_)
#                 if type_ != "open" and type_ != "close":
#                     raise HTTPException(
#                         status_code=status.HTTP_400_BAD_REQUEST,
#                         detail=f"validation failed type must be open or close",
#                     )
#                 if ind == len(scheduler_dict[k]) - 1:
#                     if type_ == "open":
#                         setdaytoday.add(k)
#
#                 if type_ == "open":
#                     newvalueh = CommonFunctions.calcvalue(value_)
#                     stime += newvalueh + "-"
#
#                     flag = 1
#                     current_day = k
#
#                 if type_ == "close":
#                     newvalueh = CommonFunctions.calcvalue(value_)
#
#                     if ind != len(scheduler_dict[k]) - 1:
#                         stime += newvalueh + ","
#
#                     else:
#                         stime += newvalueh
#
#                     flag = 2
#
#             result_dict[k].append(stime)
#
#     result_string = CommonFunctions.returnfunction(result_dict, setdaytoday)
#
#     return result_string
