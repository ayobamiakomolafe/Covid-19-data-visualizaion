"VISUALIZATION MODULE TO PRODUCE VISUAL CHARTS"

def plot_charts_by_newCasesBySpecimenDate(newCasesBySpecimenDate):
  """Top 5 Areas with the highest number of cases from 2020-03-16 to 2020-11-01, the entire timeframe period of the whole dataset alongside age_group distribution"""
  import matplotlib.pyplot as plt
  newCasesBySpecimenDate.groupby('areaName')['Total cases','newCasesBySpecimenDate-0_59','newCasesBySpecimenDate-60+' ].sum().sort_values('Total cases', ascending=False).head(5)\
  .plot(kind='bar', color= ['green', 'blue', 'orange'], figsize=(15,7))
  plt.xlabel('AreaName')
  plt.ylabel('Total cases')
  plt.title('Top 5 Areas with the highest number of cases from 2020-03-16 to 2020-11-01 with age_group distribution')
  plt.tight_layout()
  plt.show()
  
  """Top 3 Areas with the lowest number of cases from 2020-03-16 to 2020-11-01, the entire timeframe period of the whole dataset"""
  newCasesBySpecimenDate.groupby('areaName')['Total cases','newCasesBySpecimenDate-0_59','newCasesBySpecimenDate-60+' ].sum().sort_values('Total cases', ascending=False).tail(3)\
  .plot(kind='bar', color= ['green', 'blue', 'orange'], figsize=(15,7))
  plt.xlabel('AreaName')
  plt.ylabel('Total cases')
  plt.title('Top 3 Areas with the lowest of cases from 2020-03-16 to 2020-11-01 alongside age_distribution')
  plt.tight_layout()
  plt.show()
  
  """Pie chart showing Comparison of Total cases per month"""
  newCasesBySpecimenDate.groupby('months')['Total cases'].sum().to_frame().plot(kind='pie',y='Total cases',autopct='%1.1f%%',figsize=(25,9) )
  plt.title('Pie chart showing Comparison of Total cases per month')
  plt.show()
  "Top 5 Areas with the highest number of cases in October the month with highest recorded case"
  newCasesBySpecimenDate10=newCasesBySpecimenDate[newCasesBySpecimenDate['months']==10].   \
  groupby('areaName')['Total cases'].sum().to_frame().reset_index().sort_values('Total cases', ascending=False)   \
  
  colors_list = ['Red','Orange', 'Blue', 'Purple', 'Black']
  newCasesBySpecimenDate10=newCasesBySpecimenDate10.head(5)
  plt.figure(figsize=(12,8))
  ax=plt.barh(newCasesBySpecimenDate10['areaName'], newCasesBySpecimenDate10['Total cases'], color = colors_list)
  total=2396342
  for p in ax.patches:
        
        percentage = '{:.1f}%'.format(100 * p.get_width()/total)
        x = p.get_x() + p.get_width() + 0.02
        y = p.get_y() + p.get_height()/2
        plt.annotate(percentage, (x, y))
  
  plt.xlabel('Total cases')
  plt.ylabel('AreaName')
  plt.title('Top 5 Areas with the highest number of cases in october, the month with highest recorded case')
  plt.show()
  
  
  """Grouped Bar chart showing trends for Total newCases of people below age 59 and Total newCases of people above age 60 per month"""

  newCasesBySpecimenDate.groupby('months').sum()[['newCasesBySpecimenDate-0_59',	'newCasesBySpecimenDate-60+']].plot(kind='bar',figsize=(15,8) )
  plt.xlabel('Months')
  plt.ylabel('Total cases')
  plt.title('Total newCases of people below age 59 and Total newCases of people above age 60 per month')
  plt.tight_layout()
  plt.show()


  """Total number of cases reported each day from 2020-02 to 2020-11"""
  newCasesBySpecimenDate[['date', 'Total cases']].set_index('date').plot(kind='line',figsize=(15,8), color='orange')
  plt.xlabel('Dates')
  plt.ylabel('Total cases')
  plt.title('Total number of cases reported each day from 2020-02 to 2020-11')
  plt.show()

  """Total number of cases reported each week from from 2020-03-16 to 2020-11-01, the entire timeframe period of the whole dataset"""
  newCasesBySpecimenDate.groupby('weeks')['Total cases'].sum().plot(kind='line', figsize=(15,8), color='purple')
  plt.xlabel('Weeks')
  plt.ylabel('Total cases')
  plt.title('Total number of cases reported each week')
  plt.show()




  """Total number of cases reported each week for People below age 59 and people above age 59 from 2020-03-16 to 2020-11-01, the entire timeframe period of the whole dataset"""

  colors=['orange', 'blue']
  newCasesBySpecimenDate.groupby('weeks')['newCasesBySpecimenDate-60+', 'newCasesBySpecimenDate-0_59' ].sum().plot(kind='bar', figsize=(15,8),stacked=True, color=colors)
  plt.xlabel('Weeks')
  plt.ylabel('Total cases')
  plt.title('Total number of cases reported each week for People below age 59 and people above age 59')
  plt.show()
  
  
  """Donut chart showing comparison of total cases of people between age 0-59 and people above 60"""
  colors=['blue', 'orange']
  labels=['Total cases age -0_59', 'Total cases age -60+']
  newCasesBySpecimenDate.sum().to_frame().reset_index().drop([0,3, 4, 5]).set_index('index').plot(kind='pie', y=0, colors=colors, labels=labels,autopct='%1.1f%%',figsize=(15,8))
  centre_circle = plt.Circle((0, 0), 0.70, fc='white')
  fig = plt.gcf()
  # Adding Circle in Pie chart
  fig.gca().add_artist(centre_circle)
  plt.title('Donut chart showing comparison of total cases of people between age 0-59 and people above 60')
  plt.show()





def plot_charts_by_age_groups(df_age_groups):
  import matplotlib.pyplot as plt

  """Total Number of cases recorded for each age group from 2020-03-16 to 2020-11-01, the entire timeframe period of the whole dataset"""
  df_age_groups.sum().to_frame().drop(['months', 'areaName', 'weeks']).rename(columns={0:'Total cases'}).sort_values('Total cases')\
  .plot(kind='bar',figsize=(15,8), color='purple')
  plt.xlabel('Age-Range')
  plt.ylabel('Total cases')
  plt.title('Total Number of cases recorded for each age group')
  plt.tight_layout()
  plt.show()
  
  """Proportion of each age group contribution in the Month with the higest case Using a waffle chart; 'The month with highest record of cases is 10-October'"""
  
  df_age_groups.groupby('months').sum().sum(axis=1).to_frame().idxmax()
  df_waffle=df_age_groups.groupby('months').sum().loc[10,:].to_frame().drop('weeks')
  df_waffle['perc']=(df_waffle[10]/df_waffle[10].sum()) * 100
  df_waffle.reset_index(inplace=True)
  age_groups= ['0_4:','10_14:', '15_19:', '20_24:', '25_29:','30_34:', '35_39:', '40_44:', '45_49:', '50_54:',\
                 '55_59:', '5_9:', '60_64:', '65_69:', '70_74:','75_79:', '80_84:', '85_89:', '90:']
  from pywaffle import Waffle
  # To plot the waffle Chart
  fig = plt.figure(
        FigureClass = Waffle,
        rows = 5,
        title={'label': 'Proportion of each age group contribution in October, the Month with the higest case', 'loc': 'left'},
        values = df_waffle.perc,
        labels = ['{} {:.1f}%'.format(k, v) for k, v in zip(age_groups,df_waffle.perc)], 
        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(df_waffle.perc),'fontsize': 12, 'framealpha': 0},
        figsize=(40,10)
    )
  plt.tight_layout()
  plt.show()


"""Cumulative cases per day across age ranges by rollingrates"""
def plot_charts_by_rollingrates(df_cum_cases):
    import matplotlib.pyplot as plt
    df_cum_cases['Total Cum cases']=df_cum_cases.sum(axis=1)
    df_cum_cases[['date', 'Total Cum cases']].set_index('date').plot(kind='line', figsize=(15,8))
    plt.xlabel('Date')
    plt.ylabel('Total cases')
    plt.title('Total Number of Cumulative cases per day across age ranges by rollingrates')
    plt.show()



"""Cumulative cases per day across age ranges by rolling sum """
def plot_charts_by_rollingsum(cum_cases_sum):
    import matplotlib.pyplot as plt
    cum_cases_sum['Total Cum cases']=cum_cases_sum.sum(axis=1)
    cum_cases_sum[['date', 'Total Cum cases']].set_index('date').plot(kind='line', figsize=(15,8))
    plt.xlabel('Date')
    plt.ylabel('Total cases')
    plt.title('Total Number of Cumulative cases per day across age ranges by rollingsum')
    plt.show()








  


  
  
  


