
#Matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.colors as mcolors
import pandas as pd
import streamlit as st  

def graph(df_requete):
     st.set_option('deprecation.showPyplotGlobalUse', False)
     df_requete['Date_Facturation'] = df_requete['Date_Facturation'].astype(str)
     df_requete[['Date_Facturation', 'Heure_Facturation']] = df_requete['Date_Facturation'].apply(lambda x: pd.Series(x.split(' ')))
     #ordre_colonnes = ['Date', 'Heure'] + [col for col in meteo.columns if col not in ['Date', 'Heure']]
     df_requete = df_requete.drop('date', axis=1)
     
    
     dates = pd.to_datetime(df_requete['Date_Facturation'])
     colors = mdates.date2num(dates)
     
     
     
     
     
     #Partie graphique
     # Créer une liste de couleurs uniques pour chaque date
     unique_dates = df_requete['Date_Facturation'].unique()
     num_unique_dates = len(unique_dates)
     colors_temp = [mcolors.to_hex(plt.cm.viridis(i / num_unique_dates)) for i in range(num_unique_dates)]
    
     # Créer une légende catégorielle avec les dates
     legend_labels = [str(date) for date in unique_dates]
    
     # Tracer les graphiques
     fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 15))
    
     # Graphique 1 : Variation de la Température
     ax1 = axes[0, 0]
     sc = ax1.scatter(df_requete["Date_Facturation"], df_requete["FactureID"], c=colors, cmap='viridis', marker='*')
     ax1.set_xlabel('Date_Facturation')
     ax1.set_ylabel('FactureID', fontsize = 18)
    
     # Graphique 2 : Pluie
     ax2 = axes[0, 1]
     for i, date in enumerate(unique_dates):
         data = meteo[df_requete['Date'] == date]
         ax2.plot(data["Heure"], data["Pluie"], color=colors_temp[i], label=legend_labels[i], marker='*')
     ax2.set_xlabel('', fontsize = 18)
     ax2.set_ylabel('Pluie', fontsize = 18)
     ax2.legend(legend_labels, title='Pluie', title_fontsize=18)
    
     # Graphique 3 : Couverture nuageuse
     ax3 = axes[1, 0]
     for i, date in enumerate(unique_dates):
         data = df_requete[meteo['Date'] == date]
         ax3.plot(data["Heure"], data["Couverture nuageuse"], color=colors_temp[i], label=legend_labels[i], marker='*')
     ax3.set_xlabel('Heures', fontsize = 18)
     ax3.set_ylabel('Couverture nuageuse', fontsize = 18)
     ax3.legend(legend_labels, title='Couverture nuageuse', title_fontsize=18)
    
     # Graphique 4 : Humidité
     ax4 = axes[1, 1]
     for i, date in enumerate(unique_dates):
         data = df_requete[df_requete['Date'] == date]
         ax4.plot(data["Heure"], data["Humidité"], color=colors_temp[i], label=legend_labels[i], marker='*')
     ax4.set_xlabel('Heures', fontsize = 18)
     ax4.set_ylabel('Humidité', fontsize = 18)
     ax4.legend(legend_labels, title='Humidité', title_fontsize=18)
    
     plt.tight_layout()
     
     return