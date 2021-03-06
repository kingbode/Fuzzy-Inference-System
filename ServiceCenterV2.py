''''
This is the static coding for Fuzzy inference System
'''


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


mean_delay               = ctrl.Antecedent(np.arange(0,0.7,0.05),'Mean Delay')
number_of_servers        = ctrl.Antecedent(np.arange(0,1,0.05),'Number of Servers')
repair_utiliztion_factor = ctrl.Antecedent(np.arange(0,1,0.05),'Repair Utilization Factor')

number_of_spares         = ctrl.Consequent(np.arange(0,1,0.05),'Number of Spares')

mean_delay.automf(3)
number_of_servers.automf(3)
repair_utiliztion_factor.automf(3)

number_of_spares.automf(7)

mean_delay['VS']    = fuzz.trapmf(mean_delay.universe,[0,0,0.1,0.3])
mean_delay['S']     = fuzz.trimf(mean_delay.universe,[0.1,0.3,0.5])
mean_delay['M']     = fuzz.trapmf(mean_delay.universe,[0.4,0.6,0.7,0.8])

number_of_servers['S']     = fuzz.trapmf(number_of_servers.universe,[0,0,0.2,0.35])
number_of_servers['M']     = fuzz.trimf(number_of_servers.universe,[0.3,0.5,0.7])
number_of_servers['L']     = fuzz.trapmf(number_of_servers.universe,[0.6,0.8,1,1])

repair_utiliztion_factor['L']     = fuzz.trapmf(repair_utiliztion_factor.universe,[0,0,0.4,0.6])
repair_utiliztion_factor['M']     = fuzz.trimf(repair_utiliztion_factor.universe,[0.4,0.6,0.8])
repair_utiliztion_factor['H']     = fuzz.trapmf(repair_utiliztion_factor.universe,[0.6,0.8,1,1])


number_of_spares['VS'] = fuzz.trapmf(number_of_spares.universe,[0,0,0.1,0.3])
number_of_spares['S']  = fuzz.trimf(number_of_spares.universe,[0,0.2,0.4])
number_of_spares['RS'] = fuzz.trimf(number_of_spares.universe,[0.25,0.35,0.45])

number_of_spares['M']  = fuzz.trimf(number_of_spares.universe,[0.3,0.5,0.7])
number_of_spares['RL'] = fuzz.trimf(number_of_spares.universe,[0.55,0.65,0.75])
number_of_spares['L']  = fuzz.trimf(number_of_spares.universe,[0.6,0.8,1])
number_of_spares['VL'] = fuzz.trapmf(number_of_spares.universe,[0.7,0.9,1,1])

print(mean_delay['VS'])
dd = mean_delay['VS']
print('\n')
print(type(mean_delay['VS']))
# Rules



rule_1 = ctrl.Rule(mean_delay['VS'] & number_of_servers['S'] & repair_utiliztion_factor['L'] , number_of_spares['VS'])
rule_2 = ctrl.Rule(mean_delay['S'] & number_of_servers['S'] & repair_utiliztion_factor['L'] , number_of_spares['VS'])
rule_3 = ctrl.Rule(mean_delay['M'] & number_of_servers['S'] & repair_utiliztion_factor['L'] , number_of_spares['VS'])

rule_4 = ctrl.Rule(mean_delay['VS'] & number_of_servers['M'] & repair_utiliztion_factor['L'] , number_of_spares['VS'])
rule_5 = ctrl.Rule(mean_delay['S'] & number_of_servers['M'] & repair_utiliztion_factor['L'] , number_of_spares['VS'])
rule_6 = ctrl.Rule(mean_delay['M'] & number_of_servers['M'] & repair_utiliztion_factor['L'] , number_of_spares['VS'])

rule_7 = ctrl.Rule(mean_delay['VS'] & number_of_servers['L'] & repair_utiliztion_factor['L'] , number_of_spares['S'])
rule_8 = ctrl.Rule(mean_delay['S'] & number_of_servers['L'] & repair_utiliztion_factor['L'] , number_of_spares['S'])
rule_9 = ctrl.Rule(mean_delay['M'] & number_of_servers['L'] & repair_utiliztion_factor['L'] , number_of_spares['VS'])

rule_10 = ctrl.Rule(mean_delay['VS'] & number_of_servers['S'] & repair_utiliztion_factor['M'] , number_of_spares['S'])
rule_11 = ctrl.Rule(mean_delay['S'] & number_of_servers['S'] & repair_utiliztion_factor['M'] , number_of_spares['VS'])
rule_12 = ctrl.Rule(mean_delay['M'] & number_of_servers['S'] & repair_utiliztion_factor['M'] , number_of_spares['VS'])

rule_13 = ctrl.Rule(mean_delay['VS'] & number_of_servers['M'] & repair_utiliztion_factor['M'] , number_of_spares['RS'])
rule_14 = ctrl.Rule(mean_delay['S'] & number_of_servers['M'] & repair_utiliztion_factor['M'] , number_of_spares['S'])
rule_15 = ctrl.Rule(mean_delay['M'] & number_of_servers['M'] & repair_utiliztion_factor['M'] , number_of_spares['VS'])

rule_16 = ctrl.Rule(mean_delay['VS'] & number_of_servers['L'] & repair_utiliztion_factor['M'] , number_of_spares['M'])
rule_17 = ctrl.Rule(mean_delay['S'] & number_of_servers['L'] & repair_utiliztion_factor['M'] , number_of_spares['RS'])
rule_18 = ctrl.Rule(mean_delay['M'] & number_of_servers['L'] & repair_utiliztion_factor['M'] , number_of_spares['S'])

rule_19 = ctrl.Rule(mean_delay['VS'] & number_of_servers['S'] & repair_utiliztion_factor['H'] , number_of_spares['VL'])
rule_20 = ctrl.Rule(mean_delay['S'] & number_of_servers['S'] & repair_utiliztion_factor['H'] , number_of_spares['L'])
rule_21 = ctrl.Rule(mean_delay['M'] & number_of_servers['S'] & repair_utiliztion_factor['H'] , number_of_spares['M'])

rule_22 = ctrl.Rule(mean_delay['VS'] & number_of_servers['M'] & repair_utiliztion_factor['H'] , number_of_spares['M'])
rule_23 = ctrl.Rule(mean_delay['S'] & number_of_servers['M'] & repair_utiliztion_factor['H'] , number_of_spares['M'])
rule_24 = ctrl.Rule(mean_delay['M'] & number_of_servers['M'] & repair_utiliztion_factor['H'] , number_of_spares['S'])

rule_25 = ctrl.Rule(mean_delay['VS'] & number_of_servers['L'] & repair_utiliztion_factor['H'] , number_of_spares['RL'])
rule_26 = ctrl.Rule(mean_delay['S'] & number_of_servers['L'] & repair_utiliztion_factor['H'] , number_of_spares['M'])
rule_27 = ctrl.Rule(mean_delay['M'] & number_of_servers['L'] & repair_utiliztion_factor['H'] , number_of_spares['RS'])

number_of_spares_tipping_ctrl = ctrl.ControlSystem([rule_1,rule_2,rule_3,rule_4,rule_5,rule_6,rule_7,rule_8,
                                           rule_9, rule_10, rule_11,rule_12,rule_13,rule_14,rule_15,rule_16,
                                           rule_17,rule_18,rule_19,rule_20,rule_21,rule_22,rule_23,rule_24,
                                           rule_25,rule_26,rule_27])


number_of_spares_tipping = ctrl.ControlSystemSimulation(number_of_spares_tipping_ctrl)

number_of_spares_tipping.input['Mean Delay'] = 0.54
number_of_spares_tipping.input['Number of Servers'] = 0.321
number_of_spares_tipping.input['Repair Utilization Factor'] = 0.71
#
number_of_spares_tipping.compute()


print(number_of_spares_tipping.output['Number of Spares'])






