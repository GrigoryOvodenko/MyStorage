from fastapi import FastAPI, HTTPException, status
from fastapi.responses import PlainTextResponse,UJSONResponse
from models import SaveDataClass,GetDataClass,DelDataClass
import CommonFunctions
import datetime


import os
app = FastAPI()
namefile = "storage.txt"
namefilelog = "logjournal.txt"
commonfunctions =CommonFunctions.CommonCls(namefile,namefilelog)
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
            commonfunctions.deletedata(indfound,key)
            commonfunctions.insdata( key, value)
        else:
            # we record new
            commonfunctions.insdata(key,value)
    else:
        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Another transaction is opened",
                        )

    return [{'success':True}]

@app.post("/getdata")
async def getdata(getdataclass:GetDataClass):
    getdataclass_dict = getdataclass.dict()
    # в случае если транзакций открытых нет
    if flag == False:
        print(getdataclass_dict)
        print(namefile)
        #!check
        key = getdataclass_dict['key']
        fl,indfound,valuefound = commonfunctions.get_my(key)
        print("fl check:",fl)
        if fl == False:

            print("NO:",key,valuefound)
            commonfunctions.writelog( f"GET SUCCESS key:{key} value:{valuefound}-TIME {str(datetime.datetime.now())}")
        else:
            # value is not found by key
            commonfunctions.writelog(f"GET FAILED key:{key}-TIME {str(datetime.datetime.now())}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Value is not found",
            )

    else:
        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Another transaction is opened",
                        )

    return [{'success': True,'value':valuefound}]



@app.post("/deldata")
async def deldata(deldataclass:DelDataClass):
    deldataclass_dict = deldataclass.dict()
    # в случае если транзакций открытых нет
    if flag == False:
        print(deldataclass_dict)
        print(namefile)
        #!check
        key = deldataclass_dict['key']
        fl,indfound,valuefound = commonfunctions.get_my(key)
        print("fl check del:",fl)
        print(fl,indfound,valuefound)

        if fl == False:
            # we will delete because we have data and insert new
            print("NO:",key,valuefound)
            commonfunctions.writelog( f"DELETE SUCCESS key:{key} value:{valuefound}-TIME {str(datetime.datetime.now())}")
            commonfunctions.deletedata(indfound, key)
        else:
            # value is not found by key
            commonfunctions.writelog(f"DELETE FAILED key:{key}-TIME {str(datetime.datetime.now())}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Key is not found",
            )

    else:
        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Another transaction is opened",
                        )

    return [{'success': True}]



