import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

degreeS = ctrl.Antecedent(np.arange(0,101,1), 'Degrée de saleté')
typeS = ctrl.Antecedent(np.arange(0,101,1), 'Type de saleté')
temps_lavage = ctrl.Consequent(np.arange(0,61,1), 'Temps de lavage')

degreeS.automf(3)
typeS.automf(3)

temps_lavage['tres_court'] = fuzz.trimf(temps_lavage.universe, [0, 8, 12])
temps_lavage['court'] = fuzz.trimf(temps_lavage.universe, [8, 12, 20])
temps_lavage['moyen'] = fuzz.trimf(temps_lavage.universe, [12, 20, 40])
temps_lavage['long'] = fuzz.trimf(temps_lavage.universe, [20, 40, 60])
temps_lavage['tres_long'] = fuzz.trimf(temps_lavage.universe, [40, 60, 60])

degreeS.view()
typeS.view()
temps_lavage.view()

rule1 = ctrl.Rule(degreeS['good'] | typeS['good'], temps_lavage['tres_long'])
rule2 = ctrl.Rule(degreeS['average'] | typeS['good'], temps_lavage['long'])
rule3 = ctrl.Rule(degreeS['poor'] | typeS['good'], temps_lavage['long'])
rule4 = ctrl.Rule(degreeS['good'] | typeS['average'], temps_lavage['long'])
rule5 = ctrl.Rule(degreeS['average'] | typeS['average'], temps_lavage['moyen'])
rule6 = ctrl.Rule(degreeS['poor'] | typeS['average'], temps_lavage['moyen'])
rule7 = ctrl.Rule(degreeS['good'] | typeS['poor'], temps_lavage['moyen'])
rule8 = ctrl.Rule(degreeS['average'] | typeS['poor'], temps_lavage['court'])
rule9 = ctrl.Rule(degreeS['poor'] | typeS['poor'], temps_lavage['tres_court'])

rule1.view()

lavage_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
lavage = ctrl.ControlSystemSimulation(lavage_ctrl)

lavage.input['Degrée de saleté'] = 99
lavage.input['Type de saleté'] = 99

lavage.compute()
print(lavage.output['Temps de lavage'])
temps_lavage.view(sim=lavage)