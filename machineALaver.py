import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#Entré avec definition du repere orthonormé
degree_salete = np.arange(0,101,1)
type_salete = np.arange(0,101,1)

#entré avec definition variable linguistique
#pour le degrée de saleté
degree_bas = fuzz.trimf(degree_salete,[0,0,50])
degree_medium = fuzz.trimf(degree_salete,[0,50,100])
degree_haut = fuzz.trimf(degree_salete,[50,100,100])
#VL pour le type de gras
type_nongras = fuzz.trimf(type_salete,[0,0,50])
type_migras = fuzz.trimf(type_salete,[0,50,100])
type_gras = fuzz.trimf(type_salete,[50,100,100])

#sortie définition du repere et des variables linguistiques
temps_lavage = np.arange(0,61,1)
tres_court = fuzz.trimf(temps_lavage,[0,8,12])
court = fuzz.trimf(temps_lavage,[8,12,20])
moyen = fuzz.trimf(temps_lavage,[12,20,40])
long = fuzz.trimf(temps_lavage,[20,40,60])
tres_long = fuzz.trimf(temps_lavage,[40,60,60])

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8,9))
ax0.plot(degree_salete, 'b', linewidth=1.5, label='Bas')
ax0.plot(degree_salete, 'g', linewidth=1.5, label='Moyen')
ax0.plot(degree_salete, 'r', linewidth=1.5, label='Haut')
ax0.set_title('Degrée de saleté')
ax0.legend()

ax1.plot(degree_salete, 'b', linewidth=1.5, label='Non gras')
ax1.plot(degree_salete, 'g', linewidth=1.5, label='Migras')
ax1.plot(degree_salete, 'r', linewidth=1.5, label='Gras')
ax1.set_title('Type de saleté')
ax1.legend()

ax2.plot(degree_salete, 'b', linewidth=1.5, label='Très court')
ax2.plot(degree_salete, 'g', linewidth=1.5, label='Court')
ax2.plot(degree_salete, 'r', linewidth=1.5, label='Moyen')
ax2.plot(degree_salete, 'y', linewidth=1.5, label='Long')
ax2.plot(degree_salete, 'b', linewidth=1.5, label='Très long')
ax2.set_title('Temps de lavage')
ax2.legend()

for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
plt.tight_layout()