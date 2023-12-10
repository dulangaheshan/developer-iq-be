# Author: Dulanga Heshan
# Date Created: YYYY-MM-DD
# Date Updated: YYYY-MM-DD
# import boto3
from datetime import datetime

from boto3 import client, resource
from botocore.exceptions import NoCredentialsError
from decouple import config
import boto3
from boto3.dynamodb.conditions import Key
from datetime import datetime

# DynamoDB client and resource
client = boto3.client('dynamodb')

resource = boto3.resource('dynamodb')

RepositoriesTable = resource.Table('Repositories')
UsersTable = resource.Table('Users')
EventsTable = resource.Table('Events')


def get_all_repositories():
    response = RepositoriesTable.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = RepositoriesTable.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    return response


def get_repositories(day_id):
    print(day_id)
    filtering_exp = Key("day_id").eq(int(day_id))
    return RepositoriesTable.query(KeyConditionExpression=filtering_exp)


# def get_all_users():
#     response = UsersTable.scan()
#     data = response['Items']
#
#     while 'LastEvaluatedKey' in response:
#         response = RepositoriesTable.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
#         data.extend(response['Items'])
#     return response


def get_contributors_in_repository(repository):
    print(repository)
    filtering_exp = Key("repository").eq(repository)
    return UsersTable.query(KeyConditionExpression=filtering_exp)


def get_events(partition_key, sort_key):
    try:
        response = EventsTable.get_item(
            Key={
                'day_id': partition_key,
                'repository_name': sort_key
            }
        )

        item = response.get('Item')
        if item:
            print('Item found:', item)
        else:
            print('Item not found.')

    except NoCredentialsError:
        print('Credentials not available.')
