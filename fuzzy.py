import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

distance = ctrl.Antecedent(np.arange(0,36,1), 'distance')
speed = ctrl.Antecedent(np.arange(0,131,1), 'speed')

ABS = ctrl.Consequent(np.arange(0,11,1), 'brake')

distance.automf(3, 'quant')
speed.automf(3, 'quant')
ABS.automf(5, 'quant')



ABS_rule1 = ctrl.Rule(speed['low'] & distance['high'], ABS['lower'])
ABS_rule2 = ctrl.Rule(speed['low'] & distance['average'], ABS['lower'])
ABS_rule3 = ctrl.Rule(speed['low'] & distance['low'], ABS['low'])

ABS_rule4 = ctrl.Rule(speed['average'] & distance['high'], ABS['lower'])
ABS_rule5 = ctrl.Rule(speed['average'] & distance['average'], ABS['average'])
ABS_rule6 = ctrl.Rule(speed['average'] & distance['low'], ABS['high'])

ABS_rule7 = ctrl.Rule(speed['high'] & distance['high'], ABS['lower'])
ABS_rule8 = ctrl.Rule(speed['high'] & distance['average'], ABS['high'])
ABS_rule9 = ctrl.Rule(speed['high'] & distance['low'], ABS['higher'])



ABS_ctrl = ctrl.ControlSystem([ABS_rule1, ABS_rule2, ABS_rule3, ABS_rule4, ABS_rule5, ABS_rule6, ABS_rule7, ABS_rule8, ABS_rule9])
ABS_sim = ctrl.ControlSystemSimulation(ABS_ctrl)


ABS_sim.input['speed'] = 50
ABS_sim.input['distance'] = 40



ABS_sim.compute()
ABS.view(sim=ABS_sim)

print(ABS_sim.output)
plt.show()

