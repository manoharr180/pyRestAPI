from pyRestAPI.src.shared.db_repository import fetch_many_records, fetch_one_record, insert_many_record, insert_one_record
from datetime import datetime
import pandas as pd


def fetch_profiles():
    query = "select * from Profile_Details"
    result = fetch_many_records(query)
    return result


def fetch_profile(mailId):
    query = f"select * from Profile_Details where mailId = '{mailId}'"
    headers = ["ProfileId", "FName", "LName", "mailId", "PhoneNumber", "BloodGroup", "UserName", "CreatedOn",
               "ModifiedOn", "IsActive"]
    result = fetch_one_record(query, None, headers)
    return result


def insert_profiles_repo(params):
    query = "INSERT INTO Profile_Details(FName,LName,mailId,PhoneNumber,BloodGroup,UserName,CreatedOn,ModifiedOn," \
            "IsActive) " \
            "VALUES(?,?,?,?,?,?,?,?,?)"

    df = pd.read(params, orient="index").to_json()
    df['CreatedOn'] = pd.to_datetime(df['CreatedOn'])
    df['ModifiedOn'] = pd.to_datetime(df['ModifiedOn'])
    result = df.values.tolist()

    insert_many_record(query, result)
    return 1


def insert_profile_repo(params):
    query = "INSERT INTO Profile_Details(FName,LName,mailId,PhoneNumber,BloodGroup,UserName,CreatedOn,ModifiedOn," \
            "IsActive) " \
            "VALUES(?,?,?,?,?,?,?,?,?)"

    CreatedOn = datetime.strptime(params["CreatedOn"], '%d/%m/%y')
    data = [(params["FName"]), (params["LName"]), (params["mailId"]), (params["PhoneNumber"]), (params["BloodGroup"]), (params["UserName"]), (CreatedOn), (CreatedOn), 51 ]

    insert_one_record(query, data)
    return 1
