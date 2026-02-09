import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_INN_HUMAN_SILVER_PER_NIGHT
from data import COST_INN_HORSE_COPPER_PER_NIGHT

##################### O03 #####################

def copper2silver(amount:int) -> float:
    return amount / 10
def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return copper2silver(amount) /5

def platinum2gold(amount:int) -> float:
   return amount * 25

def getPersonCashInGold(personCash: dict) -> float:
    copper = personCash.get("copper", 0)
    silver = personCash.get("silver", 0)
    gold = personCash.get("gold", 0)
    platinum = personCash.get("platinum", 0)

    total_gold = copper2gold(copper) + silver2gold(silver) + gold + platinum2gold(platinum)
    return total_gold

##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    total_copper=(people*COST_FOOD_HUMAN_COPPER_PER_DAY +
                  horses * COST_FOOD_HORSE_COPPER_PER_DAY) *(JOURNEY_IN_DAYS * 2)
    total_gold =total_copper/100
    return total_gold

##################### O06 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    nieuw_lijst = []

    for item in list:
        if key in item:
            if item[key] == value:
                nieuw_lijst.append(item)

    return nieuw_lijst 

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, "adventuring", True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, "shareWith", True) 

def getAdventuringFriends(friends:list) -> list:
    adventuring_people = getAdventuringPeople(friends)
    sharing_adventuring_friends = getShareWithFriends(adventuring_people)
    return sharing_adventuring_friends

##################### O07 #####################
def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    cost_silver_voor_horse = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS

    weeks = math.ceil(JOURNEY_IN_DAYS / 7)
    cost_gold_voor_tent = tents * COST_TENT_GOLD_PER_WEEK * weeks

    total_cost = cost_gold_voor_tent + silver2gold(cost_silver_voor_horse)

    return total_cost
##################### O08 #####################

def getItemsAsText(items: list) -> str:
    teksten = []
    
    for i in items:
        hoeveelheid = i["amount"]
        eenheid = i["unit"]
        naam = i["name"]
        
        if eenheid:
            tekst = f"{hoeveelheid}{eenheid} {naam}"
        else:
            tekst = f"{hoeveelheid} {naam}"
        
        teksten.append(tekst)

    if len(teksten) > 1:
        eind_resultaat = ", ".join(teksten[:-1]) + " & " + teksten[-1]
    else:
        if teksten:
            eind_resultaat = teksten[0]
        else:
            eind_resultaat = ""

    return eind_resultaat

def getItemsValueInGold(items: list) -> float:
    totaal_goud = 0.0

    for i in items:
        aantal = i["amount"]
        prijs = i["price"]["amount"]
        type_prijs = i["price"]["type"]

        if type_prijs == "copper":
            waarde_in_goud = copper2gold(prijs)
        elif type_prijs == "silver":
            waarde_in_goud = silver2gold(prijs)
        elif type_prijs == "platinum":
            waarde_in_goud = platinum2gold(prijs)
        else:
            waarde_in_goud = prijs

        totaal_goud += aantal * waarde_in_goud

    return float(totaal_goud)

##################### O09 #####################
def getCashInGoldFromPeople(people: list) -> float:
    totaal_goud = 0.0
    for persoon in people:
        totaal_goud += getPersonCashInGold(persoon["cash"])
    return round(totaal_goud, 2)

##################### O10 #####################

def getInterestingInvestors(investors: list) -> list:
    resultaat = []
    for inv in investors:
        if "profitReturn" in inv and inv["profitReturn"] <= 10: # Neem alleen die investeerders mee waarbij de waarde van profitReturn kleiner of gelijk is aan 10.
            resultaat.append(inv)
    return resultaat



def getAdventuringInvestors(investors: list) -> list:
    """
    Geeft alle investeerders terug die interessant zijn en mee op avontuur gaan.
    """
    return [
        inv for inv in getInterestingInvestors(investors)
        if inv.get("adventuring", False)
    ]


def getTotalInvestorsCosts(investors: list, gear: list) -> float:
    """
    Bereken de totale kosten van alle avontuurlijke investeerders:
    - eten: 1 mens + 1 paard
    - huur: 1 tent + 1 paard
    - gear: items

    Retourneer 0.0 als er geen avontuurlijke investeerders zijn of gear lijst leeg is.
    """
    adventurers = getAdventuringInvestors(investors)

    if not adventurers or not gear:
        return 0.0

    cost_per_adventurer = (
        getJourneyFoodCostsInGold(1, 1) +
        getTotalRentalCost(1, 1) +
        getItemsValueInGold(gear)
    )

    total_cost = cost_per_adventurer * len(adventurers)

    return round(total_cost, 2)


##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    max_nights = 0
    while True:
        cost = getJourneyInnCostsInGold(max_nights + 1, people, horses)
        if cost > leftoverGold:
            break


        max_nights += 1
    return max_nights

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    total_silver = nightsInInn * people * COST_INN_HUMAN_SILVER_PER_NIGHT
    total_copper = nightsInInn * horses * COST_INN_HORSE_COPPER_PER_NIGHT
    total_gold = silver2gold(total_silver) + copper2gold(total_copper)
    return round(total_gold, 2)

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    cuts = []
    if not investors:
        return cuts
    for inv in investors:
        if inv.get("profitReturn", 100) <= 10:
            cut = profitGold * (inv["profitReturn"] / 100)
            cuts.append(math.floor(cut * 100) / 100)
    return cuts

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    if fellowship <= 0:
        return 0.0
    total_investors_cut = sum(investorsCuts) if investorsCuts else 0.0
    remaining = profitGold - total_investors_cut
    if remaining <= 0:
        return 0.0
    if fellowship == 0:
        return 0.0
    cut_per_adventurer = remaining / fellowship
    return round(cut_per_adventurer, 2)
##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()