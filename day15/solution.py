import copy
import itertools
import re
import sys

LIMIT_CALORIES = True
CALORIE_COUNT = 500
INGREDIENT_CAP = 100


def computeValue(foodSet, foodList):
    singleFoodTotals = [map(lambda x: x * count, foodSet[name]) for name, count in foodList.items()]
    pairedFoodTraits = zip(*singleFoodTotals)
    foodTraits = [reduce(lambda x, y: x + y, traitSet, 0) for traitSet in pairedFoodTraits]
    if LIMIT_CALORIES:
        foodTraits =  foodTraits[:-1] if foodTraits[-1] == CALORIE_COUNT else [0]
    total = reduce(lambda x, y: max(x * y, x), foodTraits, 1)
    allPositive = reduce(lambda x, y: x and y, [v > 0 for v in foodTraits], True)
    return total, copy.deepcopy(foodList)

def nextIngredient(foodSet, foodList, ingredientCount, validFoods):
    if ingredientCount is INGREDIENT_CAP:
        return computeValue(foodSet, foodList)
    else:
        maxSet = {}
        maxValue = 0
        for food in validFoods:
            foodList[food] += 1
            useFoods = validFoods[validFoods.index(food):]
            thisValue, thisSet = nextIngredient(foodSet, foodList, ingredientCount + 1, useFoods)
            if maxValue < thisValue:
                # print 'Replacing ', maxSet, ':', maxValue, ' with ', thisSet, ':', thisValue
                maxValue = thisValue
                maxSet = thisSet
            foodList[food] -= 1
        return maxValue, maxSet

with open('input.txt', 'rb') as f:
    foodSet = {}
    ingredients = {}
    regex = (
        '(?P<food>.*): capacity (?P<capacity>.*), durability (?P<durability>.*), '
        'flavor (?P<flavor>.*), texture (?P<texture>.*), calories (?P<calories>.*)'
    )
    for line in f.read().strip().split('\n'):
        segment = re.match(regex, line)
        foodSet[segment.group('food')] = (
            int(segment.group('capacity')), int(segment.group('durability')),
            int(segment.group('flavor')), int(segment.group('texture')),
            int(segment.group('calories')) if LIMIT_CALORIES else 0
        )
        ingredients[segment.group('food')] = 0

    bestValue, bestSet = nextIngredient(foodSet, ingredients, 0, ingredients.keys())
    print bestValue, bestSet
