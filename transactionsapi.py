from fastapi import FastAPI, HTTPException, status
from fastapi.responses import PlainTextResponse,UJSONResponse
from models import SaveDataClass,GetDataClass,DelDataClass,ValDataClass,OpenTransDataClass
import CommonFunctions
import datetime
import requests
import transactionmodule
import os
app1 = FastAPI()
transactionconstr = transactionmodule.TransactionCls()
namefile = "storage.txt"
namefilelog = "logjournal.txt"
namefiletrans = "transactions.txt"
namefileopentransstate = "opentransact.txt"
commonfunctions =CommonFunctions.CommonCls(namefile,namefilelog,namefiletrans,namefileopentransstate)
commonfunctions.create_files()

@app1.post("/test")
async def test():
   return {}
@app1.post("/putdata")
async def putdata(savedataclass:SaveDataClass):
    savedataclass_dict = savedataclass.dict()
    flag=savedataclass_dict['flag']
    print("flag:",flag)
    # в случае если транзакций открытых нет
    if flag == False:


        #!check
        key = savedataclass_dict['key']
        value = savedataclass_dict['value']
        fl,indfound,valuefound = commonfunctions.get_my(key)
        print("fl check:",fl,key,value,indfound)
        if fl == False:
            # we will delete because we have data and insert new
            commonfunctions.deletedata(indfound,key,valuefound)
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
@app1.post("/deldata")
async def deldata(deldataclass:DelDataClass):
    deldataclass_dict = deldataclass.dict()
    # в случае если транзакций открытых нет
    flag=deldataclass_dict['flag']
    if flag == False:

        key = deldataclass_dict['key']
        fl,indfound,valuefound = commonfunctions.get_my(key)


        if fl == False:
            # we will delete because we have data and insert new

            commonfunctions.writelog( f"delete success key:{key} value:{valuefound}-time {str(datetime.datetime.now())}")
            commonfunctions.deletedata(indfound, key,valuefound)

        else:
            # value is not found by key
            commonfunctions.writelog(f"delete failed key:{key}-time {str(datetime.datetime.now())}")
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


@app1.post("/commitransaction")
async def commitransaction():

   flgcommit = transactionconstr.commit_transaction()
   return [{'success': flgcommit}]