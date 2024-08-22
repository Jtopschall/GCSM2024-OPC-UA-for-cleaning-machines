#Validate Price reduction (13.2.24)

prices = {'tf1_price': 68.59, 'tf2_price': 65.37, 'tf3_price': 63.41, 'tf4_price': 60.49, 'tf5_price': 60.06, 'tf6_price': 63.59, 'tf7_price': 70.69, 'tf8_price': 82.18, 'tf9_price': 89.1, 'tf10_price': 75.12, 'tf11_price': 69.21, 'tf12_price': 63.87, 'tf13_price': 60.53, 'tf14_price': 60.26, 'tf15_price': 63.1, 'tf16_price': 70.7, 'tf17_price': 78.36, 'tf18_price': 95.01, 'tf19_price': 99.88, 'tf20_price': 90.99, 'tf21_price': 77.97, 'tf22_price': 71.86, 'tf23_price': 68.39, 'tf24_price': 64.74}

prices_vals = list(prices.values())
average_price = sum(prices_vals)/len(prices_vals)


hours = 5 #change this for longer production
workpieces = ((60*(hours-1)+25)*60)/12


i = 0
total_electricity_costs = [] 
for i in range(0, 19):
    
    #first hour
    cost_of_tank_preheat= 60* 0.001*(35/60)*prices_vals[i]
    cost_of_reference_process = 24.08* 0.001*(25/60)*prices_vals[i]
    cost_of_first_hour = cost_of_tank_preheat + cost_of_reference_process
    
    
    #every addtional hour without preheating, only reference process
    j = i+1
    cost_of_additional_hours = 0.0
    for j in range(i+1, i+hours):
        cost_of_additional_hour = 24.08*0.001*prices_vals[j]
        cost_of_additional_hours = cost_of_additional_hours + cost_of_additional_hour
        j+=1
        
    total_electricity_costs.append(cost_of_first_hour+cost_of_additional_hours) 
    i+=1   
        
print(total_electricity_costs)

cheapest_cost = min(total_electricity_costs)
print(cheapest_cost)
average_cost = sum(total_electricity_costs)/len(total_electricity_costs)
print(average_cost)

improvement = cheapest_cost/average_cost

print(str((1-improvement)*100)+"% Stromkostenreduktion gegenueber Tagesdurchschnitt (mittlerer Strompreis 13.02.2024)")
print(str(cheapest_cost/workpieces) +" Eur Stromkosten pro Werkstueck (35mins Tankheizung, danach Referenzbetrieb)")




#validate CO2 Reduction (13.2.24)
WS_percentages = [0.438086282938187, 0.4535356334580389, 0.4454290623021973, 0.4410799955372085, 0.43139169107278447, 0.41971748579070545, 0.3856037710744901, 0.36272062598473986, 0.3439063720845178, 0.330638270940793, 0.3231117986735491, 0.32144473612745544, 0.32453598913535536, 0.33433567727609176, 0.34956368585381475, 0.37838488386087377, 0.4160091674180944, 0.4180591925547748, 0.40941302067036023, 0.40891913707073674, 0.4186578212552238, 0.4334564011366053, 0.4512541504980598, 0.47110594486881435]

all_CEFs = [0.4094946879846351, 0.38012457219946155, 0.3625485152965296, 0.3599190226689478, 0.36174146871863505, 0.3813479046497348, 0.4187965265607759, 0.4447486142143235, 0.4208912655465321, 0.3518766137400396, 0.304072373084988, 0.2681632975525347, 0.2554309207168584, 0.26196470179563913, 0.30605328055346376, 0.3765180466093731, 0.45384000440052075, 0.5071612735806481, 0.4961495611059191, 0.46969879774625334, 0.43494479637604766, 0.4020065157974272, 0.3812356834860792, 0.37237356824998824]

#WS_Percentages_120224 = [0.3839704267230988, 0.3794174961815979, 0.3762579638538552, 0.3735386516969666, 0.3677881572618415, 0.35096478533526293, 0.31483837577900936, 0.2915722069760967, 0.27399349139934914, 0.26322319909245606, 0.25490229483619264, 0.2504488031914894, 0.24688985865954535, 0.24830538708526578, 0.25956082328845315, 0.28081785322519737, 0.2996309541926647, 0.3023917777862683, 0.29703469795773463, 0.29090179922343545, 0.2899822662951033, 0.2969210914454277, 0.3032673118763598, 0.3220759624357218]

#all_CEFs_120224 = [0.4561633322923796, 0.45413087862433366, 0.45835857203032854, 0.4574901087870471, 0.45992968937492296, 0.46844858831812, 0.48932572963393695, 0.52072354733796, 0.5268617162972123, 0.4956782249430497, 0.4655382781979983, 0.43428937179052973, 0.4070515781265584, 0.4045897666633671, 0.41428060917252385, 0.4467791393298399, 0.49437305274665205, 0.5400122544541984, 0.536813173782821, 0.5152679492160332, 0.47914827951271166, 0.460909195572862, 0.45007715852175517, 0.4298832491414585]

WS_percentage_average = sum(WS_percentages)/len(WS_percentages)


i=0
WS_percentages_intervals = []
for i in range(0, 19):
    interval_sum = 0
    for j in range(0,hours):
        interval_sum = interval_sum + WS_percentages[i+j]
        
    WS_percentages_intervals.append(interval_sum) 
    i+=1   

print("durchschnittlicher vorhergesagter solarwind anteil am 13.2.24: " +str(WS_percentage_average))        

print(WS_percentages_intervals)

print("vorhergesagter intervall mit am meisten wind und solar: " +str(max(WS_percentages_intervals)))


#get the number of max interval
i = 0 
for i in range(0,len(WS_percentages_intervals)-1):
    if max(WS_percentages_intervals) == WS_percentages_intervals[i]:
        chosen_interval = i
    else:
        pass
    i+=1
    
print("chosen interval: " +str(chosen_interval))





i=0
Emissions_intervals = []
for i in range(0, 19):
    
   #first hour
    emissions_of_tank_preheat= 60*(35/60)*all_CEFs[i]
    emissions_of_reference_process = 24.08*(25/60)*all_CEFs[i]
    emissions_of_first_hour = emissions_of_tank_preheat + emissions_of_reference_process
    
    
    #every addtional hour without preheating, only reference process
    j = i+1
    emissions_of_additional_hours = 0.0
    for j in range(i+1, i+hours):
        emissions_of_additional_hour = 24.08*all_CEFs[j]
        emissions_of_additional_hours = emissions_of_additional_hours + emissions_of_additional_hour
        j+=1
        
    Emissions_intervals.append(emissions_of_first_hour+emissions_of_additional_hours) 
    i+=1
    
print(Emissions_intervals)

average_emissions = sum(Emissions_intervals)/len(Emissions_intervals)

print("average emissions: "+str(average_emissions))


print("best interval: "+str(min(Emissions_intervals)))

possible_improvement =  (1- min(Emissions_intervals)/average_emissions)*100

realized_improvement = (1 - Emissions_intervals[chosen_interval]/average_emissions)*100

print("best possible emissions reduction: " + str(possible_improvement) +"%")

print("realized_reduction: " + str(realized_improvement) +"%")

#---> vorhersage wird mit tatsaechlich an diesem tag erzielten CEF verifiziert --> wenn vorhersage besser wird, dann kann auch betrieb im richtigen intervall geplant werden! - wenn anders, als vorhergesagt, andere intervalle windiger und sonniger werden/mehr gruene energietraeger beitragen, dann versagt die vorhersage!

