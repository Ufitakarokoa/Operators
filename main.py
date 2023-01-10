# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

#Languages
spain_language="spanish"
switzerland_language="german"

#Religions
spain_religion="roman catholic"
switzerland_religion="roman catholic"

#Name Lenghts
spain_capital_name_lenght=len("Madrid")
switzerland_capital_name_lenght=len("Bern")

#Gdps
spain_gdp=1393351000000
switzerland_gdp=731502000000000

#Population growth
spain_population_growth=0.13
switzerland_population_growth=0.65

#Population
spain_population=47163418
switzerland_population=8508698

print(spain_language==switzerland_language)
print(spain_religion==switzerland_religion)
print(spain_capital_name_lenght != switzerland_capital_name_lenght)
print(switzerland_gdp<spain_gdp)
print(spain_population_growth and switzerland_population_growth <= 1)
print (spain_population >= 10000000) or (switzerland_population >= 10000000)
print(spain_population >= 10000000 and switzerland_population <= 10000000) or (switzerland_population>= 10000000 and spain_population <= 10000000)
