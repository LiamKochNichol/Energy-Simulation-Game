text_100_a ='Welcome to “Energy Simulation Game”! In this game, you will learn about the implementation of renewable energy onto'
text_100_b = 'a grid and the benefits and drawbacks of such solutions.'

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

text_200_a = 'Welcome to level 2 of “Energy Simulation Game”! We will begin adding complexity to the basic system introduced in'
text_200_b = 'module 1.'
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

text_300_a="Welcome to module 3 of “Energy Simulation Game”! In the section we will examine"
text_300_b="transmission lines in more detail."

text_301_a="You may be used to electricity flowing through a wire to a load and back to the source,"
text_301_b="but transmission lines actually often use three wires! This is called a three-phase power."
text_301_c="It is used because it can transmit more power for the same amount of material."

text_302_a="You have seen resistors in circuits with a ‘resistance’ property. In fact, electrical"
text_302_b="resistance exists in all materials, even conductors like wires. Normally the impacts are"
text_302_c="small, but in long transmission lines that connect cities and provinces the effects add up."

text_303_a="Transmission lines also have a property called ‘inductance’, like inductors from circuits"
text_303_b="Inductance is a property that opposes the change in current of a conductor and arises"
text_303_c="because the transmission wires interact with each other. In power systems their effects"
text_303_d="are much greater than resistance."

text_304_a="Both the resistance and inductance of a transmission line depend on the material and "
text_304_b="the length of the line. They can be approximated by a resistor and inductor, like those "
text_304_c="you saw in circuits."

text_305_a="We did not take resistance into account in the past modules. In reality, some power is"
text_305_b="lost in transmission. To supply 150MW to the load, the generators must supply a bit"
text_305_c="more than 150MW to account for the line power losses!"

text_306_a="Here is what the solution to module 2 would have looked like if there was resistance in"
text_306_b="the lines. Note that more power (and minimal cost) is needed to run the system."

text_307_a="If we want to be super accurate, we should account for line resistance. However, in"
text_307_b="some applications it is ignored since it simplifies the problem, and their effects"
text_307_c="are small. We will ignore resistance in these modules, but remember that it exists!"

text_308_a="You may have wondered how the power flow in each line was calculated in the previous"
text_308_b="modules. We did not show the line inductances back then. Here they are now. Notice"
text_308_c="that more power flows through lines with a smaller inductance, and vice versa."

text_309_a="Take a look at the following system. Which line will have the most amount of power"
text_309_b="flowing through it? Click on your answer."

text_310_a="That was not the correct answer. Please try again."

text_311_a="Correct!"

text_312_a="Just like smaller wires, transmission lines can only allows so much power to flow"
text_312_b="through at any time. They will burn down and fail if power flow exceeds their maximum,"
text_312_c="or their ‘ratings’."

text_313_a="This imposes another constraint to the power flow problem. In addition to power balance"
text_313_b="and economic dispatch, utilities must be wary to not violate the ratings of any "
text_313_c="transmission line!"

text_314_a="Line ratings are now displayed next to each line. The predicted power flow in each line"
text_314_b="will also be updated as you move the sliders. Additional information have been added to "
text_314_c="the information screen."

text_315_a="Your goal is to minimize cost while satisfying power balance and line limits! Good luck!"

text_316_a="You didn’t maintain power balance! Even with all these other considerations, the priority"
text_316_b="should be to supply the correct total power to the system. Click Retry to try again."

text_317_a="A transmission line was overloaded by your dispatch! This caused it to be unusable in "
text_317_b="the system, making it impossible to safely supply power to the load. Click on Retry to try"
text_317_c="again."

text_318_a="Good job on satisfying power balance and keeping flows within line limits! However, this"
text_318_b="isn’t the most cost-effective dispatch. Can you find a configuration that satisfies "
text_318_c="constraints while minimizing cost? Click Retry to try again."

text_319_a="Well done! You found the minimum cost dispatch while satisfying the system constraints."
text_319_b="As you may tell, There are a lot of factors to consider when running a power grid!"

text_320_a="Congratulations, you have completed module 3. Through these 3 modules, you have"
text_320_b="learned the basics of power systems operation. We will next introduce renewable energy"
text_320_c="to show their benefits and limitations."

text_321_a="Line ratings are now displayed next to each line. The predicted power flow in each line"
text_321_b="will also be updated as you move the sliders. Additional information have been added to"
text_321_c="the information screen."

text_323_a="Good job on satisfying power balance! Let's check if the line limits are respected."
text_323_b="Click on the Next button."

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