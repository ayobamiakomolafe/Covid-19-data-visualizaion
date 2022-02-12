'''This module cleans the dataset and extract columns for visualization'''

def data_preprocessing(dataset_path):
    import pandas as pd
    import warnings
    warnings.filterwarnings("ignore")
    df=pd.read_csv(dataset_path)

    
    """
    **PRE-PROCESSING**

    First extract the unique columns based on newCasesBySpecimenDate- which is the column newCasesBySpecimenDate-0_59 and newCasesBySpecimenDate-60+, the addition of this
    two columns give the total number of cases per day
    """

    newCasesBySpecimenDate=df[['areaName','date','newCasesBySpecimenDate-0_59', 'newCasesBySpecimenDate-60+']]
    newCasesBySpecimenDate['Total cases']=newCasesBySpecimenDate.sum(axis=1)

    'Respective Months and Week can also be Extracted from the newCasesBySpecimenDate df'
    newCasesBySpecimenDate['date']=newCasesBySpecimenDate['date'].astype('datetime64[ns]')
    newCasesBySpecimenDate['months']=newCasesBySpecimenDate['date'].dt.month
    newCasesBySpecimenDate['weeks']=newCasesBySpecimenDate['date'].dt.week
    global newCasesBySpecimenDate_df
    newCasesBySpecimenDate_df=newCasesBySpecimenDate

    
    """
    Second Extract dataframe of cases across the respective age groups
    """

    df_age_groups=df[['areaName',	'date',	'newCasesBySpecimenDate-0_4', 'newCasesBySpecimenDate-10_14',	'newCasesBySpecimenDate-15_19',
                      'newCasesBySpecimenDate-20_24',	'newCasesBySpecimenDate-25_29',	'newCasesBySpecimenDate-30_34',	'newCasesBySpecimenDate-35_39',
                      'newCasesBySpecimenDate-40_44',	'newCasesBySpecimenDate-45_49',	'newCasesBySpecimenDate-50_54',	'newCasesBySpecimenDate-55_59',
                      'newCasesBySpecimenDate-5_9',	'newCasesBySpecimenDate-60_64',	'newCasesBySpecimenDate-65_69',
                      'newCasesBySpecimenDate-70_74',	'newCasesBySpecimenDate-75_79',	'newCasesBySpecimenDate-80_84',
                      'newCasesBySpecimenDate-85_89',	'newCasesBySpecimenDate-90+' ]]

    
    'Respective Months and Week can also be Extracted for the df_age_groups'
    df_age_groups['date']=df_age_groups['date'].astype('datetime64[ns]')
    df_age_groups['months']=df_age_groups['date'].dt.month
    df_age_groups['weeks']=df_age_groups['date'].dt.week
    global age_groups_df
    age_groups_df=df_age_groups


    
    """
    Third,
    Extraction of Cumulative cases based on rollingrates
    """

    df_cum_cases=df[['date','newCasesBySpecimenDateRollingRate-0_4',	'newCasesBySpecimenDateRollingRate-10_14',
                     'newCasesBySpecimenDateRollingRate-15_19',	'newCasesBySpecimenDateRollingRate-20_24',	'newCasesBySpecimenDateRollingRate-25_29',	
                     'newCasesBySpecimenDateRollingRate-30_34',	'newCasesBySpecimenDateRollingRate-35_39',	'newCasesBySpecimenDateRollingRate-40_44',
                     'newCasesBySpecimenDateRollingRate-45_49',	'newCasesBySpecimenDateRollingRate-50_54',	'newCasesBySpecimenDateRollingRate-55_59',	
                     'newCasesBySpecimenDateRollingRate-5_9',		'newCasesBySpecimenDateRollingRate-60_64',
                     'newCasesBySpecimenDateRollingRate-65_69', 'newCasesBySpecimenDateRollingRate-70_74',	'newCasesBySpecimenDateRollingRate-75_79',	
                     'newCasesBySpecimenDateRollingRate-80_84',	'newCasesBySpecimenDateRollingRate-85_89',	'newCasesBySpecimenDateRollingRate-90+'	]]
    global cum_cases_df
    cum_cases_df= df_cum_cases


    """
    Fourth, Extraction of cumulative cases based on rollingsum
    """
    df_cum_cases_sum=df[['date','newCasesBySpecimenDateRollingSum-0_4',	'newCasesBySpecimenDateRollingSum-10_14',
                 'newCasesBySpecimenDateRollingSum-15_19',	'newCasesBySpecimenDateRollingSum-20_24',	'newCasesBySpecimenDateRollingSum-25_29',	
                 'newCasesBySpecimenDateRollingSum-30_34',	'newCasesBySpecimenDateRollingSum-35_39',	'newCasesBySpecimenDateRollingSum-40_44',
                 'newCasesBySpecimenDateRollingSum-45_49',	'newCasesBySpecimenDateRollingSum-50_54',	'newCasesBySpecimenDateRollingSum-55_59',	
                 'newCasesBySpecimenDateRollingSum-5_9',		'newCasesBySpecimenDateRollingSum-60_64',
                 'newCasesBySpecimenDateRollingSum-65_69', 'newCasesBySpecimenDateRollingSum-70_74',	'newCasesBySpecimenDateRollingSum-75_79',	
                 'newCasesBySpecimenDateRollingSum-80_84',	'newCasesBySpecimenDateRollingSum-85_89',	'newCasesBySpecimenDateRollingSum-90+'	]]
    global cum_cases_sum
    cum_cases_sum= df_cum_cases_sum

        
