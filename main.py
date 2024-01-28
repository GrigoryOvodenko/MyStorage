from fastapi import FastAPI, HTTPException, status
from fastapi.responses import PlainTextResponse,UJSONResponse
from models import SaveDataClass,GetDataClass,DelDataClass,ValDataClass,OpenTransDataClass
import CommonFunctions
import datetime
import requests
import transactionmodule
import os
app = FastAPI()
#app1 =FastAPI()
namefile = "storage.txt"
namefilelog = "logjournal.txt"
namefiletrans = "transactions.txt"
namefileopentransstate = "opentransact.txt"
commonfunctions =CommonFunctions.CommonCls(namefile,namefilelog,namefiletrans,namefileopentransstate)


#flag =False


@app.post("/opentransaction")
async def opentransaction(opentransdataclass:OpenTransDataClass):
    opentransdataclass_dict = opentransdataclass.dict()
    print("opentransdataclass_dict:",opentransdataclass_dict)
    # print("flag:",flag)
    with open(namefileopentransstate,"r") as fileop:
        myflag = fileop.readline()

    task = opentransdataclass_dict['task']
    if task == "putdata":
        key=opentransdataclass_dict['data']['key']
        value = opentransdataclass_dict['data']['value']
        with open(namefileopentransstate, "w") as f:
            f.write("True")
        status1 = requests.post(f"http://127.0.0.1:5000/putdata/", json={'flag':myflag,'key': key, 'value': value})
        if status1.status_code ==200:
            requests.post(f"http://127.0.0.1:5000/commitransaction/", json={})
            with open(namefileopentransstate, "w") as f:
                f.write("False")
        else:
            with open(namefileopentransstate, "w") as f:
                f.write("False")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Transaction is not closed",
            )
    elif task == "deldata":
        key = opentransdataclass_dict['data']['key']
        with open(namefileopentransstate, "w") as f:
            f.write("True")
        status1 = requests.post(f"http://127.0.0.1:5000/deldata/", json={'flag':myflag,'key': key})
        if status1.status_code == 200:
            requests.post(f"http://127.0.0.1:5000/commitransaction/", json={})
            with open(namefileopentransstate, "w") as f:
                f.write("False")
        else:
            with open(namefileopentransstate, "w") as f:
                f.write("False")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Transaction is not closed",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Type of Task is not correct",
        )



@app.post("/getdata")
async def getdata(getdataclass:GetDataClass):
        getdataclass_dict = getdataclass.dict()
    # в случае если транзакций открытых нет

        #!check
        key = getdataclass_dict['key']
        fl,indfound,valuefound = commonfunctions.get_my(key)

        if fl == False:

            commonfunctions.writelog( f"get success key:{key} value:{valuefound}-time {str(datetime.datetime.now())}")
        else:
            # value is not found by key
            commonfunctions.writelog(f"get failed key:{key}-time {str(datetime.datetime.now())}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Value is not found",
            )



        return [{'success': True,'value':valuefound}]






@app.post("/findkeys")
async def findkeys(valdataclass:ValDataClass):
        valdataclass_dict = valdataclass.dict()
    # в случае если транзакций открытых нет


        valueinp = valdataclass_dict['value']
        mykeys = commonfunctions.findkeysbyvalue(valueinp)

        if mykeys != []:


             commonfunctions.writelog( f"get all keys for value:{valueinp} success keys:{mykeys} -time {str(datetime.datetime.now())}")

        else:
            # keys are not found by value
            commonfunctions.writelog(
                f"get all keys for value:{valueinp} failed-time {str(datetime.datetime.now())}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Keys are not found",
            )


        return [{'success': True,'data':mykeys}]