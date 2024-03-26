import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SerbianLanguageGame')


def lambda_handler(event, context):
        words_to_add = {
                'cat': 'mačka',
                'dog': 'pas',
                'goodbye': 'doviđenja',
                'kiss': 'poljubac',
                'book': 'knjiga',
                'friend': 'prijatelj',
                'house': 'kuća',
                'water': 'voda',
                'food': 'hrana',
                'apple': 'jabuka',
                'cherry': 'trešnja',
                'pear': 'kruška',
                'orange': 'narandža',
                'peach': 'breskva',
                'strawberry': 'jagoda',
                'watermelon': 'lubenica',
                'grape': 'grožđe',
                'cheese': 'sir',
                'chicken': 'piletina',
                'pork': 'svinjetina',
                'egg': 'jaje',
                'salt': 'so',
                'sugar': 'šećer',
                'oil': 'ulje',
                'coffee': 'kafa',
                'tea': 'čaj',
                'beer': 'pivo',
                'ice cream': 'sladoled',
                'airplane': 'avion',
                'train': 'voz',
                'store': 'prodavnica',
                'building': 'zgrada',
                'country': 'zemlja',
                'number': 'broj',
                'color': 'boja',
                'day': 'dan',
                'week': 'sedmica',
                'year': 'godina',
                'weather': 'vreme',
                'sun': 'sunce',
                'rain': 'kiša',
                'wind': 'vetar',
                'red': 'crvena',
                'square': 'trg',
                'umbrela': 'kišobran',
                'milk': 'mleko',
        }


        for word, translation in words_to_add.items():
                table.put_item(
                        Item={
                                'Word': word,
                                'Translation': translation
                        }
                )

        return {
                'statusCode': 200,
                'body': 'Items added to the DynamoDB table.'
        }