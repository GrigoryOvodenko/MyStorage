from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from models import SaveDataClass, DelDataClass
import CommonFunctions
import datetime

import transactionmodule

app1 = FastAPI()
transactionconstr = transactionmodule.TransactionCls()

commonfunctions = CommonFunctions.CommonCls()
commonfunctions.create_files()


@app1.post("/putdata")
async def putdata(savedataclass: SaveDataClass):
    savedataclass_dict = savedataclass.dict()
    flag = savedataclass_dict["flag"]

    # в случае если транзакций открытых нет
    if flag == False:
        #!check
        key = savedataclass_dict["key"]
        value = savedataclass_dict["value"]
        fl, indfound, valuefound = commonfunctions.get_my(key)

        if fl == False:
            # we will delete because we have data and insert new
            commonfunctions.deletedata(indfound, key, valuefound)
            commonfunctions.insdata(key, value)
        else:
            # we record new
            commonfunctions.insdata(key, value)

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Another transaction is opened",
        )

    return [{"success": True}]


@app1.post("/deldata")
async def deldata(deldataclass: DelDataClass):
    deldataclass_dict = deldataclass.dict()
    # в случае если транзакций открытых нет
    flag = deldataclass_dict["flag"]

    if flag == False:
        key = deldataclass_dict["key"]
        fl, indfound, valuefound = commonfunctions.get_my(key)

        if fl == False:
            # we will delete because we have data and insert new

            commonfunctions.writelog(
                f"delete success key:{key} value:{valuefound}-time {str(datetime.datetime.now())}"
            )
            commonfunctions.deletedata(indfound, key, valuefound)

        else:
            # value is not found by key
            commonfunctions.writelog(
                f"delete failed key:{key}-time {str(datetime.datetime.now())}"
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Key is not found",
            )

    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Another transaction is opened",
        )

    return [{"success": True}]


@app1.post("/commitransaction")
async def commitransaction():
    flgcommit = transactionconstr.commit_transaction()
    return [{"success": flgcommit}]


@app1.post("/rollbackapp")
async def rollbackapp():
    transactionconstr.rollbacktrans()
