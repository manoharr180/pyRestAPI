from services.profile_service import get_profiles_service, get_profile_service, get_one_profile, insert_profile_service
from flask import Response, request
import json


def get_profiles():
    results = get_profiles_service()
    return Response(json.dumps(results), 200, mimetype="application/json")


def get_profile():
    query_parameters = request.args
    mailId = query_parameters['mailId']
    # result = get_profile_service(mailId)
    print(mailId)
    result = get_one_profile(mailId)
    return Response(json.dumps(result, indent=4, sort_keys=True, default=str), 200, mimetype="application/json")


def insert_profile():
    body = request.data
    data = json.loads(body)
    result = insert_profile_service(data)
    return Response(result, 201, mimetype="application/json")
