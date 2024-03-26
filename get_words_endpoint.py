import json
import boto3
import random

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SerbianLanguageGame')


def lambda_handler(event, context):
    try:
        response = table.scan()
        words = [item['Word'] for item in response['Items']]
        translations = [item['Translation'] for item in response['Items']]


        word, translation = random.choice(list(zip(words, translations)))


        options = set([translation])
        while len(options) < 4:
            options.add(random.choice(translations))
        options = list(options)
        random.shuffle(options)


        question = {
            'word': word,
            'options': options
        }


        return {
            'statusCode': 200,
            'body': json.dumps(question)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }