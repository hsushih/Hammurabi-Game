import random, string

def print_intro():
    
    print ''' Congrats, you are the newest ruler of ancient Samaria, elected for a ten year term
of office. Your duties are to distribute food, direct farming, and buy and sell land
as needed to support your people. Watch out for rat infestations and the resultant
plague! Grain is the general currency, measured in bushels. The following will help
you in your decisions:

* Each person needs at least 20 bushels of grain per year to survive.
* Each person can farm at most 10 acres of land.
* It takes 2 bushels of grain to farm an acre of land.
* The market price for land fluctuates yearly.

Rule wisely and you will be showered with appreciation at the end of your term. Rule
poorly and you will be kicked out of office!'''

def Hammurabi():
    starved = 0
    immigrants = 5.0
    population = 100
    harvest = 3000 # total bushels harvested
    bushels_per_acre = 3 # amount harvested for each acre planted
    rats_ate = 200 # bushels destroyed by rats
    bushels_in_storage = 2800
    acres_owned = 1000
    cost_per_acre = 19 # each acre costs this many bushels
    plague_deaths = 0
    
    print print_intro()
    
    
    for year in xrange(1,11):


        print '''O great Hammurabi! You are in year %d of your ten year rule.'''  %year
        print '''In the previous year''' , starved, ''' people starved to death.'''  
        print '''In the previous year %d people entered the kingdom.''' %immigrants
        print '''population is now %d.''' %population
        print '''We harvested %d bushels at %d bushels per acre.'''%(harvest, bushels_per_acre)
        print '''Rats destroyed %d bushels, leaving %d bushels in storage.'''%(rats_ate,bushels_in_storage)
        print '''The city owns %d acres of land.'''% acres_owned
        print '''Land is currently worth %d bushels per acre.'''%cost_per_acre
        print '''There were %d deaths from the plague.'''%plague_deaths

            
        # functions
        
       
        acres_bought = ask_to_land(bushels_in_storage,cost_per_acre)
        bushels_spent_3= acres_bought * cost_per_acre
        if acres_bought == 0:
            acres_sell=ask_to_sell_land(acres_owned)
            acres_owned=acres_owned - acres_sell
            bushels_spent_2= acres_sell * cost_per_acre
            bushels_in_storage = bushels_in_storage + bushels_spent_2
            print ''' currently you have ''', int(bushels_in_storage), ''' in storage '''
            

        acres_owned = acres_owned + acres_bought 
        bushels_spent = ask_to_feed(bushels_in_storage)
        bushels_in_storage=bushels_in_storage - bushels_spent  -bushels_spent_3
        print ''' currently you have ''', int(bushels_in_storage), ''' in storage '''
        
        harvest = ask_to_cultivate(acres_owned,population,bushels_in_storage) * getHarvest()
            
        # parameters    
        starved = numStarving( population,bushels_spent )
        
        plague_deaths= isPlague(population)

        if bushels_in_storage < 1000 :
            rats_ate = 0
        else :
            rats_ate = bushels_in_storage * doRatsInfest()
        
        
        bushels_per_acre= getHarvest()
        cost_per_acre = priceOfLand()
        
        immigrants= numImmigrants(acres_owned, bushels_in_storage, population, starved)
        population= population - plague_deaths + immigrants


        

        if bushels_in_storage < -1000 :
            print ''' you have wasted too much '''
            quit()
        else:
            bushels_in_storage=bushels_in_storage  + harvest - rats_ate

        # summary
        
        print ''' you have let ''' , starved, ''' people starve to death '''
        print ''' you have got ''' ,acres_owned, ''' acres land '''
        print '''you have successfully completed the 10 year term Congradulations'''

        if starved >= 50 :
            print '''you have been kicked out loser'''
            quit (Hammurabi)
        
    
        
                  

def ask_to_land(bushels,cost_per_acre):
    '''  Ask user how many bushels you wish to spend buying land.'''
    acres= input(" how many acres will you buy?")
    while acres *cost_per_acre > bushels:
        print " 0 great Hammurabi, we have", bushels, " bushels of grain!"
        acres= input("How many acres will you buy?")
    return acres

def ask_to_sell_land(acres):
    " Ask user how much land you wish to sell"
    acres_sell=input(' how many acres do you wish to sell')
    while acres_sell > acres:
        print " you only have", acres, "acres"
        acres_sell=input(" how much land you wish to sell")
    return acres_sell

def ask_to_feed(bushels):
    ''' Ask user how many bushels you want to use for feeding.'''
    bushels_feeds=input(" how many bushels youu want to use for feeding")
    while bushels_feeds > bushels:
        print " you only have", bushels,"bushels"
        bushels_feeds=input( " how many bushels you want to use for feeding")
    return bushels_feeds

def ask_to_cultivate(acres, population, bushels):
    ''' Ask user how much land you want to plant seed in'''
    acres_cultivate=input( 'how much land you want to plant seed in')
    while acres_cultivate * 2> bushels:
        print " you only have", bushels, "bushels  stupid!!!! you still need to give me", eval('acres_cultivate * 2 - bushels'), " bushels"
        acres_cultivate=input(' how much land you want to seed in')
    while acres_cultivate > population * 10:
        print " the population is only", population
        acres_cultivate=input(' how much land you want to plant seed in')
    while acres_cultivate > acres :
        print " you only have" , acres, " acres "
        acres_cultivate=input(' how much land you want to plant seed in')
    return acres_cultivate
    
            
def isPlague(population):
    if random.randint(0,99)<15:
        plague_deaths = population * 0.5
    else :
        plague_deaths = 0
    return plague_deaths
    
def numStarving(population,bushels):
    bushels_needed= 20 * population

    if bushels >= bushels_needed:
        starved = 0
    elif 0.55 * population * 20 < bushels < bushels_needed:
        starved=(bushels_needed - bushels)/20
    else :
        print ''' you are the poorest ruler I have ever seen in my whole life  you have been kicked out'''
        quit(Hammurabi)
    return int (starved)
        
    
def numImmigrants(land, grainInStorage,population,numStarving):

   if numStarving == 0:
       immigrants=(20 * land + grainInStorage)/(100 * population +1)
   elif numStarving > 0:
       immigrants = 0
   return immigrants
       
       
def getHarvest():
    z=random.randint(1,8)
    return z


def doRatsInfest():
   if random.randint(0,99)>40:
       r=random.uniform(0.1,0.3)
   else :
       r = 0
   return r
   
        
    
def priceOfLand():
    price=random.randint(16,22)
    return price



if __name__==" Hammurabi" :
    Hammurabi()

