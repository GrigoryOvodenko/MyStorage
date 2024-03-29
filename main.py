from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from models import GetDataClass, ValDataClass, OpenTransDataClass
import CommonFunctions
import datetime
import requests


app = FastAPI()

namefileopentransstate = "opentransact.txt"
commonfunctions = CommonFunctions.CommonCls()


# открыть транзакцию в зависимости от типа задачи в транзакции
@app.post("/opentransaction")
async def opentransaction(opentransdataclass: OpenTransDataClass):
    opentransdataclass_dict = opentransdataclass.dict()
    task = opentransdataclass_dict["task"]

    with open(namefileopentransstate, "r") as fileop:
        myflag = fileop.readline()

    if task == "putdata":
        commonfunctions.start_trans()
        key = opentransdataclass_dict["data"]["key"]
        value = opentransdataclass_dict["data"]["value"]
        commonfunctions.recordopentransact("True")
        status1 = requests.post(
            f"http://127.0.0.1:5000/putdata/",
            json={"flag": myflag, "key": key, "value": value},
        )
        if status1.status_code == 200:
            requests.post(f"http://127.0.0.1:5000/commitransaction/", json={})

            commonfunctions.recordopentransact("False")
        else:
            commonfunctions.recordopentransact("False")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Transaction is not closed api:opentransaction task:putdata",
            )
    elif task == "deldata":
        key = opentransdataclass_dict["data"]["key"]
        commonfunctions.recordopentransact("True")
        status1 = requests.post(
            f"http://127.0.0.1:5000/deldata/", json={"flag": myflag, "key": key}
        )
        if status1.status_code == 200:
            requests.post(f"http://127.0.0.1:5000/commitransaction/", json={})
            commonfunctions.recordopentransact("False")
        else:
            commonfunctions.recordopentransact("False")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Transaction is not closed api:opentransaction task:deldata",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Type of Task is not correct",
        )
    # переносим транзакции в постоянную область
    commonfunctions.transfertranscations()

    return JSONResponse({"success": True})


# получить данные
@app.post("/getdata")
async def getdata(getdataclass: GetDataClass):
    getdataclass_dict = getdataclass.dict()
    # в случае если транзакций открытых нет

    key = getdataclass_dict["key"]
    fl, indfound, valuefound = commonfunctions.get_my(key)

    if fl == False:
        commonfunctions.writelog(
            f"get success key:{key} value:{valuefound}-time {str(datetime.datetime.now())}"
        )
    else:
        # value is not found by key
        commonfunctions.writelog(
            f"get failed key:{key}-time {str(datetime.datetime.now())}"
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Value is not found",
        )
    return JSONResponse({"success": True, "value": valuefound})


# поиск ключей по значению
@app.post("/findkeys")
async def findkeys(valdataclass: ValDataClass):
    valdataclass_dict = valdataclass.dict()
    valueinp = valdataclass_dict["value"]
    mykeys = commonfunctions.findkeysbyvalue(valueinp)

    if mykeys != []:
        commonfunctions.writelog(
            f"get all keys for value:{valueinp} success keys:{mykeys} -time {str(datetime.datetime.now())}"
        )

    else:
        commonfunctions.writelog(
            f"get all keys for value:{valueinp} failed-time {str(datetime.datetime.now())}"
        )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Keys are not found",
        )

    return JSONResponse({"success": True, "data": mykeys})
