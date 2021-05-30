from pyRestAPI.src.repository import profile_repo
import json


def get_profiles_service():
    results = profile_repo.fetch_profiles()
    return {'profiles': results}


def get_profile_service(mailId):
    results = profile_repo.fetch_profiles()
    input_dict = json.loads(results)
    output = [x for x in input_dict if x['mailId'] == mailId]
    return output


def get_one_profile(mailId):
    result = profile_repo.fetch_profile(mailId)
    return result


def insert_profile_service(data):
    profile_repo.insert_profile_repo(data)
    return 1
