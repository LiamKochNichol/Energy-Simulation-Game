text_100_a ='Welcome to “A Greener Grid”! In this game, you will learn about the implementation of renewable energy onto a grid and'
text_100_b = 'the benefits and drawbacks of such solutions.'

text_101_a = 'The game interface contains 3 main layouts: this text box, which will guide you through the game and give'
text_101_b = 'useful tooltips, the system screen, which will give you a representation of your network. and the informational screen,'
text_101_c = 'which will display useful numbers and graphs from power flow simulations.'

text_102_a = 'Loads are modeled on the visual interface as a down pointing arrow. Loads in a system consume power. You can think of'
text_102_b = 'loads as anything that requires power to run. Computers, houses, cities, factories are all examples of loads, the last two'
text_102_c = 'around the scale of loads considered in transmission systems.'

text_103_a = 'Generators are denoted by a G symbol on the visual interface. These represent conventional dispatchable generators such'
text_103_b = 'as coal, oil, or natural gas plants which burn fuel to generate electricity while producing carbon emissions. Their outputs'
text_103_c = 'can be controlled and adjusted on demand.'

text_104_a = 'Connective elements give the means to transmit electricity across distances. Denoted in short, thick lines are buses,'
text_104_b = 'points/nodes where generators and loads are connected. Linking the buses are transmission lines which carry power across'
text_104_c = 'the system.'

text_105_a = 'The concept of power balance is core to running an energy system. It states that the amount of power generated (supply)'
text_105_b = 'must equal the amount consumed (demand) at all times.'

text_106_a = 'The grid operates at a frequency of 50Hz (Europe) or 60Hz (US). This frequency must remain stable. If power supply'
text_106_b = 'exceeds demand, the frequency rises, and power plants disconnect themselves from the system to avoid failure.'

text_107_a = 'If power demand exceeds supply, the frequency decreases. Rolling blackouts occur, where only some consumers have'
text_107_b = 'power. If this continues, power plants will begin switching off, causing system-wide blackouts which are very difficult to'
text_107_c = 'recover from.'

text_108_a = 'The numbers next to the generators and loads show their current power values in megawatts [MW], which is the unit'
text_108_b = 'commonly used in utility-scale systems. The large number in red shows the power imbalance that is currently in the'
text_108_c = 'system.'

text_109_a = 'Now it\'s your turn! The sliders control the two generators in the system, each of which has a maximum capacity of'
text_109_b = '100MW. Adjust the sliders such that the net power imbalance in zero. When you are ready, click Run!'

text_110_a = 'You ran your system without balancing the power first! The system suffered a blackout. Remember, always keep your'
text_110_b = 'system in balance. The imbalance number will turn green when this is achieved. When you are ready, click the Retry'
text_110_c = 'button and try again.'

text_111_a = 'Success! Sufficient power has been delivered to the consumer. The power flows of each line are now shown. The path of'
text_111_b = 'energy depends on properties of the transmission line. We will discuss this in much more detail in a following module.'

text_112_a = 'Congratulations, you have completed module one of the game. You should now be familiar with power balance and basic'
text_112_b = 'power system diagrams. In the next modules we will build upon this system with additional details and considerations.'

text_200_a = 'Welcome to level 2 of “A Greener Grid”! We will begin adding complexity to the basic system introduced in module 1.'
text_200_b = ''
text_200_c = ''

text_201_a = 'Last time, we adjusted two generator to supply the load and achieved power balance. You were able to split the 150MW'
text_201_b = 'demand however you wanted between the two generators. In reality, utilities must consider the cost of energy when'
text_201_c = 'planning generator dispatch.'

text_202_a = 'The cost of power depends a variety of factors. Some factors include the type of energy source, location, capital and'
text_202_b = 'maintenance costs, life cycle, and market rates.'

text_203_a = 'The problem of “Economic Dispatch” seeks to find how much each generator should provide to satisfy demand'
text_203_b = 'while keeping costs at a minimum.'

text_204_a = 'Optimizing a large system can be very complex and is done by sophisticated programs and techniques. The problem also'
text_204_b = 'needs to be solved frequently since the system’s state changes in real time. In our case we will stick to this simple system.'

text_205_a = 'Costs of power are now displayed above each generator. Your tasks will be to minimize cost while maintaining power'
text_205_b = 'balance! Move the sliders around to adjust generator output and click the Run button when you are ready.'

text_206_a = 'You ran your system without balancing the power first! The system suffered a blackout. Remember, always keep your'
text_206_b = 'system in balance. When you are ready, click the Retry button and try again.'

text_207_a = 'Your configuration balances the load, but isn’t the most cost-efficient… Click the retry button and try again.'

text_208_a = 'Success! You used the least amount of costs while delivering power to the consumer. Of course, The problem isn’t as'
text_208_b = 'simple as always maximizing your cheapest generators. We will discuss this in more detail in the next module.'

text_209_a = 'Economic dispatch isn’t the only problem to consider cost. Since starting up generators have a cost too,'
text_209_b = '“Unit Commitment” decides which generator should turn on at any time. To avoid being too confusing, we will focus on'
text_209_c = 'economic dispatch moving forward.'

text_210_a = 'Congratulations, you have complete module two of the game. You should now understand the problem of economic'
text_210_b = 'dispatch, and the factors that goes into minimizing the cost of power systems operation. The next module will discuss'
text_210_c = 'transmission lines in more detail.'

text_300_a="Welcome to module 3 of “A Greener Grid”! In the section we will examine transmission lines in more detail."
text_300_b=""

text_301_a="You may be used to electricity flowing through a wire to a load and back to the source, but transmission lines"
text_301_b="actually often use three wires! This is called a three-phase power. It is used because it can transmit more power for the"
text_301_c="same amount of material."

text_302_a="You have seen resistors in circuits with a ‘resistance’ property. In fact, electrical resistance exists in all materials, even"
text_302_b="conductors like wires. Normally the impacts are small, but in long transmission lines that connect cities and provinces the"
text_302_c="effects can add up."

text_303_a="Transmission lines also have a property called ‘inductance’, like inductors from circuits, Inductance is a property that"
text_303_b="opposes the change in current of a conductor and arises because the transmission wires interact with each other. In power"
text_303_c="systems their effects are much greater than resistance."

text_304_a="Both the resistance and inductance of a transmission line depend on the material and the length of the line. They can be"
text_304_b="approximated by a resistor and inductor, like those you saw in circuits."
text_304_c=""

text_305_a="We did not take resistance into account in the past modules. In reality, some power is lost in transmission. To supply"
text_305_b="150MW to the load, the generators must supply a bit more than 150MW to account for the line power losses!"
text_305_c=""

text_306_a="Here is what the solution to module 2 would have looked like if there was resistance in the lines. Note that more power"
text_306_b="from the generators (151.7MW vs. 150MW) and a higher minimum cost ($1767 vs. $1750) are needed to run the system."

text_307_a="If we want to be super accurate, we should account for line resistance. However, in some applications it is ignored since"
text_307_b="it simplifies the problem, and their effects are small. We will ignore resistance in these modules, but remember that it"
text_307_c="exists!"

text_308_a="You may have wondered how the power flow in each line was calculated in the previous modules. We did not show the"
text_308_b="line inductances back then. Here they are now. Notice that when the generators supply equal power, more power flows"
text_308_c="through lines with a smaller inductance, and vice versa."

text_309_a="Take a look at the following system. Which line will have the most amount of power flowing through it? Click on your"
text_309_b="answer."

text_310_a="That was not the correct answer. Please try again. The information on the right may help you."

text_311_a="You are correct!"

text_312_a="Just like smaller wires, transmission lines can only allows so much power to flow through at any time. They will burn"
text_312_b="down and fail if power flow exceeds their maximum, or their ‘ratings’."
text_312_c=""

text_313_a="This imposes another constraint to the power flow problem. In addition to power balance and economic dispatch, utilities"
text_313_b="must be wary to not violate the ratings of any transmission line!"
text_313_c=""

text_314_a="Line ratings are now displayed next to each line. The predicted power flow in each line will also be updated as you move"
text_314_b="the sliders. Additional information have been added to the information screen."
text_314_c=""

text_315_a="Your goal is to minimize cost while satisfying power balance and line limits! Good luck!"

text_316_a="You didn’t maintain power balance! Even with all these other considerations, the priority should be to supply the correct"
text_316_b="total power to the system. Click Retry to try again."

text_317_a="A transmission line was overloaded by your dispatch! This caused it to be unusable in the system, making it impossible to"
text_317_b="safely supply power to the load. Click on Retry to try again."
text_317_c=""

text_318_a="Good job on satisfying power balance and keeping flows within line limits! However, this isn’t the most cost-effective"
text_318_b="dispatch. Can you find a configuration that satisfies the constraints while minimizing cost? Click Retry to try again."
text_318_c=""

text_319_a="Well done! You found the minimum cost dispatch while satisfying the system constraints. As you may tell, There are a lot"
text_319_b="of factors to consider when running a power grid!"

text_320_a="Congratulations, you have completed module 3. Through these 3 modules, you have learned the basics of power"
text_320_b="systems operation. We will next introduce renewable energy to show their benefits and limitations."
text_320_c=""

text_400_a = 'Welcome to module 4 of “A Greener Grid”! In the section we will begin an introduction on the role of renewable energy'
text_400_b = 'in power systems.'

text_401_a = 'Previously, we used solely conventional generators, which use carbon-based resources to power turbines. Next we will'
text_401_b = 'examine how renewable energy changes the power flow problem.'

text_402_a = 'Wind and solar power are variable and intermittent due to their dependence on nature. The main operational difference is'
text_402_b = 'that unlike conventional generators, their output cannot be controlled.'

text_403_a = 'To plan our dispatch, forecasts are often used in place of known values. These forecasts can range from very accurate to'
text_403_b = 'wildly off depending on weather conditions.'

text_404_a = 'Shown in the figure is the Ontario wind data from August 1st to 5th, 2022. Note the high degree of variation in wind'
text_404_b = 'output and large forecast errors during Aug. 3rd.'

text_405_a = 'To show their basic effects, generator 2 is now replaced by a wind plant with the symbol “W”. The first slider can no'
text_405_b = 'longer be moved, and instead shows the forecasted wind value and an uncertainty range.'

text_406_a = 'Using what we have learned, please adjust generator 2 such that power balance is achieved. When you are ready, click the'
text_406_b = 'Run button.'

text_407_a = 'Uh oh, you did not balance the power in the system correctly. Remember that the imbalance shows on the informational'
text_407_b = 'screen. Click Retry to try again.'

text_408_a = 'Good job. The power flow results are shown on the screen. Notice that the generator value is different from the one you'
text_408_b = 'set! This is because the wind output also deviated from its forecast. This is done automatically in real power systems in a'
text_408_c = 'process named “redispatch”.'

text_409_a = 'We were lucky that the wind error did not cause issues, but you can see how this may be problematic. We have reset the'
text_409_b = 'problem with a greater wind uncertainty. Click Run and see what could potentially happen.'

text_410_a = 'In this scenario, the actual wind output fell short of the anticipated amount. Notice how we do not have enough capacity to'
text_410_b = 'run the system anymore even when we max out generator 2! A system that overly relies on variable renewable energy can'
text_410_c = 'face problems during renewable shortfalls.'

text_411_a = 'We will also show the case when the wind plant generates more than anticipated. Click Run to see.'

text_412_a = 'In this scenario, wind is generating greater than predicted. However, this has overloaded the line between bus 1 and 3.'
text_412_b = 'As previously explained, this can lead to a line outage, further disrupting the system. These are just some of the challenges'
text_412_c = 'introduced by renewable energy.'

text_413_a = 'We have been treating the load as a constant up until now. Power demand also fluctuates throughout the days and seasons.'
text_413_b = 'See the demand variation across one day in the figure. This is why electricity prices depend on which hour you use them!'

text_414_a = 'Another challenge posed by renewables is the fact that load patterns do not always match renewable output patterns. If an'
text_414_b = 'energy source generates a lot when we do not need it or little when we do, what is the point?'

text_415_a = 'Energy storage technologies alleviates these problems by allowing energy to be stored and used at another time. Increasing'
text_415_b = 'transmission capacity and generation reserves can also prevent the two cases we saw earlier.'

text_416_a = 'Of course, increasing renewable energy is a vital step towards net zero emission goals. Wind and solar energy produce'
text_416_b = 'drastically less carbon emissions compared to natural gas and coal plants.'

text_417_a = 'Despite their challenges, renewables have seen a historic growth in the past decade while costs have declined. Many'
text_417_b = 'countries are offering incentives for renewable energy projects and progress is being made globally.'

text_418_a = 'Congratulations, you have completed module 4. Hopefully you have learned a few more things about how renewable'
text_418_b = 'energy fits into the power grid, the challenges they pose, and ways of reducing their impact on system reliability.'

text_500_a = 'Welcome to module 5 of “A Greener Grid”! In the section we will dive into the different types of energy resources'
text_500_b = 'commonly used around the world, and their costs and carbon emissions.'

text_501_a = 'Canada’s goal is to become a net-zero greenhouse gas emitting country by 2050. This commitment has driven a shift in the'
text_501_b = 'energy sector away from nonrenewable resources toward previously uncompetitive higher-cost green energy. Let\'s take a'
text_501_c = 'look at some common resources.'

text_502_a = 'Coal power is the oldest type of large-scale energy resource and offers reliable power at a low cost. However, its'
text_502_b = 'Greenhouse Gas Emissions (GHG) are the highest out of any other energy resource, traditionally being between 750 and'
text_502_c = '1100 grams of CO2 per kWh of electricity produced.'

text_503_a = 'While its affordability has been valued to maintain low electricity prices, its high GHG emissions have led to a decrease'
text_503_b = 'in their use over the past decades.'

text_504_a = 'Natural gas power plants are the most used fossil fuel in electricity production, supplying 25% of the world’s electricity.'
text_504_b = 'Their emissions, while being significantly lower than coal, are still substantial, averaging between 400 and 500 grams of'
text_504_c = 'CO2 per kWh of produced electricity.'

text_505_a = 'While transitioning fully to green energy resources would be ideal, the current capacities of those resources do not allow'
text_505_b = 'for it to be possible yet. For that reason, countries are implementing Carbon Capture and Storage technologies in order to'
text_505_c = 'reduce the impact of the fossil fuel share that cannot be phased out currently.'

text_506_a = 'The main CCS consists of capturing the CO2 emitted during the electricity generation process and transport it to an area'
text_506_b = 'where it can be stored underground in geological formations. Thanks to those methods, Coal and Natural Gas emissions'
text_506_c = 'can be reduced up to 147 and 92 grams of CO2 per kWh respectively.'

text_507_a = 'Hydroelectric is the most popular renewable energy resource in Canada thanks to geographic availability. Its generation'
text_507_b = 'process is technically non-emitting, it requires reservoirs which are producing GHG due to the decomposition of organic'
text_507_c = 'material within them. This leads to a high variability in their emissions, ranging from 6 to 147 grams of CO2 per kWh.'

text_508_a = 'Nuclear Energy is a unique type of energy resource, as it is the lowest CO2 emitting resource, but produces nuclear waste,'
text_508_b = 'which needs to be isolated and stored until their radioactivity becomes harmless, which can take thousands of years. In'
text_508_c = 'addition to this, its power output is hard to control and it cannot be switched off easily.'

text_509_a = 'Wind Energy consists of arrays of large wind turbines using the wind speed in the region to convert mechanical power of'
text_509_b = 'their rotors into electrical power. Its cost per kWh of electricity is higher than most electricity production means due to'
text_509_c = 'lower efficiency.'

text_510_a = 'Since their power output is proportional to the wind speed, only specific areas are favorable for their installation, and'
text_510_b = 'battery storage systems are necessary to store the excess of electricity and release it during low wind speed intervals.'

text_511_a = 'Solar Energy harnesses the power of the daily solar irradiance. Its high variability in GHG emissions is related to the two'
text_511_b = 'types of solar energy installations: concentrated solar power and photovoltaic panels.'

text_512_a = 'Concentrated Solar Power (CSP) is a large-scale solar energy production plant which consists of a system of mirror that'
text_512_b = 'focus a solar beam on a receiver which will use the heat to power a turbine.'

text_513_a = 'Photovoltaic panels can be implemented on a residential scale or a commercial scale (solar farms). They are made of arrays'
text_513_b = 'of photovoltaic cells that capture the photon energy to create electricity. Their efficiency is low and a high amount of'
text_513_c = 'power is lost in heat which leads to an increase in the panels’ temperature, lowering their efficiency.'

text_514_a = 'This graph shows the Ontario electricity supply breakdown for the December 2022. Nuclear, due to its low emissions,'
text_514_b = 'cost, and inflexible output, is prioritized, followed by hydro and natural gas. Wind and solar are used last, as their high'
text_514_c = 'cost and variable nature makes energy planning challenging, as discussed in module 4.'

text_515_a = 'In 2022, most of Canada’s electricity supplied relied on Hydroelectric, followed by Nuclear and natural gas. Ontario has'
text_515_b = 'phased out coal entirely from their electricity production, but it is still being used in other provinces.'

text_516_a = 'Congratulations, you have completed module 5. You should now be familiar with the common types of electricity'
text_516_b = 'generation methods and their contributions to the grid.'


# module 6
text_hydro_title = 'Hydro'
text_hydro_cost = '$10/MW'
text_hydro_emissions = '10 tCO2e/MW'

text_wind_title = 'Wind'
text_wind_cost = '$10/MW'
text_wind_emissions = '10 tCO2e/MW'

text_solar_title = 'Solar'
text_solar_cost = '$10/MW'
text_solar_emissions = '10 tCO2e/MW'

text_nuclear_title = 'Nuclear'
text_nuclear_cost = '$10/MW'
text_nuclear_emissions = '10 tCO2e/MW'

text_coal_title = 'Coal'
text_coal_cost = '$10/MW'
text_coal_emissions = '10 tCO2e/MW'

text_gas_title = 'Gas'
text_gas_cost = '$10/MW'
text_gas_emissions = '10 tCO2e/MW'