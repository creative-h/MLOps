import json

from random import choices

def fruit_generator(fruit):
    """Returns back random fruit"""

    fruits = ["apple", "cherry"]
    fruits.append(fruit)
    return choices(fruits)
    
    
def lambda_handler(event, context):
    # TODO implement
    fruit = event["fruit"]
    print(f"You passed in fruit {fruit}")
    chosen_fruit = fruit_generator(fruit)
    print(f"We selected this fruit for you {chosen_fruit}")
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
