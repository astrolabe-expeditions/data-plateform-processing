
"""
You will find here unitary tests for helpers functions
"""

#############################################################################################################################################################################

import pandas as pd
import numpy as np
from tools import treatments_tools as treat

#############################################################################################################################################################################

### Test of 'drop_invalid_datetime'

def test_drop_invalid_datetime():
    '''
    dataframe:
       Dates: date valide, espace, string vide, jour impossible, mois impossible, année impossible, espace avant, espace après, les 2
       Temps: temps valide, espace, string vide, seconde impossible, minute impossible, heure impossible, espace avant, espace après, les 2
    format : année / mois / jour | heure / minute / seconde
    '''
    data = {
        "Date" : ['20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',
                  '20/01/01',' ','', np.nan,'21/01/40','12/24/23', '254/02/15',' 20/02/02', '20/02/03 ', ' 20/02/04 ',],
        "Time" : ['13:45:25','13:45:25','13:45:25','13:45:25','13:45:25','13:45:25','13:45:25','13:45:25','13:45:25','13:45:25',
                  ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','','','','','','','','','','',
                    np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,
                    '13:45:70','13:45:70','13:45:70','13:45:70','13:45:70','13:45:70','13:45:70','13:45:70','13:45:70','13:45:70',
                    '13:70:25','13:70:25','13:70:25','13:70:25','13:70:25','13:70:25','13:70:25','13:70:25','13:70:25','13:70:25',
                    '25:45:25','25:45:25','25:45:25','25:45:25','25:45:25','25:45:25','25:45:25','25:45:25','25:45:25','25:45:25',
                    ' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',' 13:45:26',
                    '13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ','13:45:27 ',
                    ' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ',' 13:45:28 ']
    }
    df = treat.drop_invalid_datetime(pd.DataFrame(data))


    assert pd.to_datetime('20/01/01', format='%y/%m/%d').date() in df["Date"].values, "La fonction enlève des dates valides"
    assert pd.to_datetime('13:45:25', format='%H:%M:%S').time() in df["Time"].values, "La fonction enlève des temps valides"
    assert ' ' not in df["Date"].values, "La fonction ne gère par les strings ' ' pour les dates"
    assert ' ' not in df["Time"].values, "La fonction ne gère par les strings ' ' pour les temps"
    assert '' not in df["Date"].values, "La fonction ne gère par les strings '' pour les dates"
    assert '' not in df["Time"].values, "La fonction ne gère par les strings '' pour les temps"
    assert not df["Date"].isnull().values.any(), "Il y à un Null/NaN/NaT dans la colonne Date: les nan déjà présents ne sont pas traités où les erreurs sont transformées en nan et non traités"
    assert not df["Time"].isnull().values.any(), "Il y à un Null/NaN/NaT dans la colonne Time: les nan déjà présents ne sont pas traités où les erreurs sont transformées en nan et non traités"
    assert '25/01/40' not in df['Date'].values, "Les erreurs de type jour impossible ne sont pas traités"
    assert '12/24/23' not in df['Date'].values, "Les erreurs de type mois impossible ne sont pas traités"
    assert '254/02/15' not in df['Date'].values, "Les erreurs de type année impossible ne sont pas traités"
    assert '13:45:70' not in df['Time'].values, "Les erreurs de type seconde impossible ne sont pas traités"
    assert '13:70:25' not in df['Time'].values, "Les erreurs de type minute impossible ne sont pas traités"
    assert '25:45:25' not in df['Time'].values, "Les erreurs de type heure impossible ne sont pas traités"
    assert ' 13:45:26' not in df["Time"].values, "les temps avec un espace avant ne sont pas traités"
    assert '13:45:27 ' not in df["Time"].values, "les temps avec un espace après ne sont pas traités"
    assert ' 13:45:28 ' not in df['Time'].values, "les temps avec un espace avant et après ne sont pas traités"
    assert pd.to_datetime('13:45:26', format='%H:%M:%S').time() in df["Time"].values, "les temps avec un espace avant sont supprimés et non modifiées"
    assert pd.to_datetime('13:45:27', format='%H:%M:%S').time() in df["Time"].values, "les temps avec un espace après sont supprimés et non modifiées"
    assert pd.to_datetime('13:45:28', format='%H:%M:%S').time() in df["Time"].values, "les temps avec un espace avant et après sont supprimés et non modifiées"
    assert ' 20/02/02'   not in df["Date"].values, "les dates avec un espace avant ne sont pas traités"
    assert '20/02/03 ' not in df["Date"].values, "les dates avec un espace après ne sont pas traités"
    assert ' 20/02/04 ' not in df['Date'].values, "les dates avec un espace avant et après ne sont pas traités"
    assert pd.to_datetime('20/02/02', format='%y/%m/%d').date() in df["Date"].values, "les dates avec un espace avant sont supprimés et non modifiées"
    assert pd.to_datetime('20/02/03', format='%y/%m/%d').date() in df["Date"].values, "les dates avec un espace après sont supprimés et non modifiées"
    assert pd.to_datetime('20/02/04', format='%y/%m/%d').date() in df["Date"].values, "les dates avec un espace avant et après sont supprimés et non modifiées"

#############################################################################################################################################################################

### Test of 'to_numeric'

def test_to_numeric():
    """
    tests done:
    - tests of expected response
    - tests with other value types
    """
    data = {
        'ec_1' : [0.0 , 10.2, np.pi, 12, 8.4, np.nan],
        'ec_2' : ['4', 'np.pi', '10**23', '', 'O', 6],
        'str' : ['yes', 'no', 'a', 'b', 'c', 'd']
    }

    df = pd.DataFrame(data)
    df = treat.to_numeric(df,['ec_1','ec_2'])

    assert all(value in df['ec_1'].values for value in [0.0,10.2,12,8.4]), "La fonction enlève des valeurs valides"
    assert df['ec_1'].isin([np.pi]).any(), "la fonction enlève des valeurs complexes (comme np.pi)"
    assert df['ec_1'].isin([np.nan]).any(), "la fonction enlève les np.nan déjà existants"
    assert not df['ec_2'].isin([np.pi, 'np.pi', 10**23, '10**23', '', 'O']).all(), "la fonction ne traite pas des valeurs normalement traitées par pd.to_numeric"
    assert not np.isnan(df['ec_2'][0]), "la fonction renvoie np.nan pour des valeurs normalement transformées en numérique"
    assert list(df['str']) == data['str'], "la fonction traite des colonnes qu'elle ne devrait pas traiter"

#############################################################################################################################################################################

### Test of 'trim_all_columns'

def test_trim_all_columns():
    data = {
        'A ' : [4     , 8   , 10.4 , 'oui'],
        ' B' : [' z'  , 'e ', ' r ', '   '],
        ' C ': [np.nan, 5   , 10   , 'h'  ]
    }
    df = pd.DataFrame(data)
    df_unchanged = df.copy()
    df_changed = treat.trim_all_columns(df)

    try:
        A = df_changed['A']
        B = df_changed['B']
        C = df_changed['C']
    except KeyError:
        print("the function doesn't trim columns names")
    assert df_unchanged['A '].equals(df_changed['A']), "the function modify columns that are already ok"
    assert df_unchanged[' C '].equals(df_changed['C']), "the function modify columns that are already ok"
    assert df_changed['B'].isin(['z']).any(), "the function doesn't trim spaces before values"
    assert df_changed['B'].isin(['e']).any(), "the function doesn't trim spaces after values"
    assert df_changed['B'].isin(['r']).any(), "the function doesn't trim spaces around values"
    assert df_changed['B'].isin(['']).any(), "the function doesn't trim empty strings"

#############################################################################################################################################################################

### Test of 'drop_null_columns'

def test_drop_null_columns():
    data1 = {
        'A' : [0, 1, 2, 3],
        'B' : [2, 'oui', None, 4]
    }

    data2 = {
        'A' : [0, 1, 2, 3],
        'B' : [2, 'oui', None, 4],
        'C' : [None, None, None, None]
    }

    df1 = pd.DataFrame(data1)
    df1_changed = df1.copy()
    df2 = pd.DataFrame(data2)
    df2_changed = df2.copy()
    treat.drop_null_columns(df1_changed)
    treat.drop_null_columns(df2_changed)

    assert df1.equals(df1_changed), "La fonction enlève des colonnes comportant des données"
    assert df1.equals(df2_changed), "la fonction n'enlève pas les colonnes "


########################################################################################################################


### Test of 'process_columns'

# Unitary test function
def test_process_columns():
    data = {
    'Temp_1': [25, 30, 35, None, 45],  # Add a null value for testing
    'Temp_2': [20, 25, 30, 35, 40],
    'Pres_1': [1000, 1010, 1020, 1030, 1040],
    'Pres_2': [990, None, 1010, 1020, 1030],  #Add a null value for testing
    'EC_1': [5, 10, 15, 20, 25],
    'EC_2': [8, 12, 16, 'invalid', 24]  # Add not numerical value for testing
    }

    df = pd.DataFrame(data)

    # Define values for filters
    temp_min = 25
    temp_max = 40
    temp_ext_min = 20
    temp_ext_max = 45
    pres_min = 1000
    pres_max = 1030
    ec_min = 5
    ec_max = 20

    processed_df, temp_cols, ec_cols, pres_cols = treat.process_columns(df, temp_min, temp_max, temp_ext_min, temp_ext_max, pres_min, pres_max, ec_min, ec_max)

    # Assertions
    assert processed_df.shape[1] == 6  # Check number of columns
    assert 'Temp_1' in temp_cols  # Check if Temp_1 is in the temp_cols list
    assert 'EC_1' in ec_cols  # Check if EC_1 is in ec_cols list
    assert 'Pres_1' in pres_cols  # Check if Pres_1 is in ec_cols list
    assert processed_df['Temp_1'].notnull().all()  # Check that there is no null value in Temp_1 column in the final df
    assert processed_df['Pres_2'].notnull().all()  # Check that there is no null value in Pres_2 column in the final df
    assert processed_df['EC_2'].apply(pd.to_numeric, errors='coerce').notnull().all()  # Check that all EC_2 values are numeric
    assert processed_df.applymap(lambda x: isinstance(x, (int, float))).all().all()


#############################################################################################################################################################################

### Test of 'to_unique_col'

def test_to_unique_col():
    # Define test data
    data_to_unique_col = {
        'temp_1': [25, 30, 35, 40],
        'temp_2': [20, 25, 30, 35],
        'ec_1': [5, 10, 15, 20]
    }
    df_to_unique_col = pd.DataFrame(data_to_unique_col)

    processed_df = treat.to_unique_col(df_to_unique_col)

    # Check that original columns are deleted
    assert 'temp_1' not in processed_df.columns
    assert 'temp_2' not in processed_df.columns
    assert 'ec_1' not in processed_df.columns

    # Check that new columns are created
    assert 'temp_sea' in processed_df.columns
    assert 'ec_sea' in processed_df.columns
    assert 'depth' in processed_df.columns

    # Check that values are correctly concatenated in lists
    assert processed_df['temp_sea'].tolist() == [[25, 20], [30, 25], [35, 30], [40, 35]]
    assert processed_df['ec_sea'].tolist() == [[5], [10], [15], [20]]
    assert processed_df['depth'].tolist() == [[], [], [], []] # Check that a column depth made of empty lists is created when no depth column are in the original file

#############################################################################################################################################################################

def test_salinity_calculator_cas_normal():
    """
    On teste avec des valeurs normales et on s'assure que le résultat est correct (compléter les valeurs)
    """
    data = [
        {'coeffs': {'A': [0.0080, -0.1692, 25.3851, 14.0941, -7.0261, 2.7081],
                    'B': [0.0005, -0.0056, -0.0066, -0.0375, 0.0636, -0.0144],
                    'C': [0.6766097, 0.0200564, 0.000110426, -6.9698E-07, 1.0031E-09],
                    'K': 0.0162},
         'temperature': 13.500,
         'conductivity': 38500,
         'resultat': 66076698.95429349},
        {'coeffs': {'A': [0.0080, -0.1692, 25.3851, 14.0941, -7.0261, 2.7081],
                    'B': [0.0005, -0.0056, -0.0066, -0.0375, 0.0636, -0.0144],
                    'C': [0.6766097, 0.0200564, 0.000110426, -6.9698E-07, 1.0031E-09],
                    'K': 0.0162},
         'temperature': 5.345,
         'conductivity': 38500,
         'resultat': 116613280.47066434},
        {'coeffs': {'A': [0.0080, -0.1692, 25.3851, 14.0941, -7.0261, 2.7081],
                    'B': [0.0005, -0.0056, -0.0066, -0.0375, 0.0636, -0.0144],
                    'C': [0.6766097, 0.0200564, 0.000110426, -6.9698E-07, 1.0031E-09],
                    'K': 0.0162},
         'temperature': 13.500,
         'conductivity': 45555,
         'resultat': 101284981.33029039},
        {'coeffs': {'A': [0.0080, -0.1692, 25.3851, 14.0941, -7.0261, 2.7081],
                    'B': [0.0005, -0.0056, -0.0066, -0.0375, 0.0636, -0.0144],
                    'C': [0.6766097, 0.0200564, 0.000110426, -6.9698E-07, 1.0031E-09],
                    'K': 0.0162},
         'temperature': 5.345,
         'conductivity': 45555,
         'resultat': 178694226.6800965}
    ]

    for test_case in data:
        coeffs = test_case['coeffs']
        temperature = test_case['temperature']
        conductivity = test_case['conductivity']
        resultat = test_case['resultat']
        salinity = treat.salinity_calculator(temperature, conductivity, coeffs)
        assert salinity == resultat, 'Le résultat est faux pour un cas classique'


def test_salinity_calculator_cas_limite():
    """
    On teste avec des valeurs limites et nulles de température et on s'assure que le résultat est correct
    """
    data = [
        {'coeffs': {'A': [0.0080, -0.1692, 25.3851, 14.0941, -7.0261, 2.7081],
                    'B': [0.0005, -0.0056, -0.0066, -0.0375, 0.0636, -0.0144],
                    'C': [0.6766097, 0.0200564, 0.000110426, -6.9698E-07, 1.0031E-09],
                    'K': 0.0162},
         'temperature': -20,
         'conductivity': 38500,
         'resultat': 1455642842.2176728},
        {'coeffs': {'A': [0.0080, -0.1692, 25.3851, 14.0941, -7.0261, 2.7081],
                    'B': [0.0005, -0.0056, -0.0066, -0.0375, 0.0636, -0.0144],
                    'C': [0.6766097, 0.0200564, 0.000110426, -6.9698E-07, 1.0031E-09],
                    'K': 0.0162},
         'temperature': 100,
         'conductivity': 38500,
         'resultat': 2600744.709900622},
        {'coeffs': {'A': [0.0080, -0.1692, 25.3851, 14.0941, -7.0261, 2.7081],
                    'B': [0.0005, -0.0056, -0.0066, -0.0375, 0.0636, -0.0144],
                    'C': [0.6766097, 0.0200564, 0.000110426, -6.9698E-07, 1.0031E-09],
                    'K': 0.0162},
         'temperature': 0,
         'conductivity': 38500,
         'resultat': 177818660.56553715}
    ]

    for test_case in data:
        coeffs = test_case['coeffs']
        temperature = test_case['temperature']
        conductivity = test_case['conductivity']
        resultat = test_case['resultat']

        salinity = treat.salinity_calculator(temperature, conductivity, coeffs)
        assert salinity == resultat, 'Le résultat est faux pour un cas limite'


def test_salinity_calculator_conductivity_null():
    """
    On teste avec une valeur de conductivité nulle
    """
    data = [
        {'coeffs': {'A': [0.0080, -0.1692, 25.3851, 14.0941, -7.0261, 2.7081],
                    'B': [0.0005, -0.0056, -0.0066, -0.0375, 0.0636, -0.0144],
                    'C': [0.6766097, 0.0200564, 0.000110426, -6.9698E-07, 1.0031E-09],
                    'K': 0.0162},
         'temperature': 20,
         'conductivity': 0,
         'resultat': 0.010312673450508788}
    ]

    for test_case in data:
        coeffs = test_case['coeffs']
        temperature = test_case['temperature']
        conductivity = test_case['conductivity']
        resultat = test_case['resultat']

        salinity = treat.salinity_calculator(temperature, conductivity, coeffs)
        assert salinity == resultat, 'Le résultat est faux pour le cas de conductivité nulle'


# Test for rename_columns()
def test_rename_columns():
    data = {
        'Lat1': [1.0, 2.0, 3.0],
        'Lng2': [4.0, 5.0, 6.0],
        'Bat %4': [90, 80, 70],
        'Bat mV5': [4000, 3900, 3800],
        'Pression_ext6': [1010, 1012, 1015],
        'Temp_ext7': [25.0, 26.0, 27.0],
        'Temp_int8': [22.0, 23.0, 24.0],
        'Temp_sea9': [28.0, 29.0, 30.0],
        'EC_sea10': [35.0, 36.0, 37.0],
        'Profondeur11': [10.0, 12.0, 15.0],
    }
    df = pd.DataFrame(data)
    treat.rename_columns(df)

    expected_columns = [
        "latitude", "longitude", "battery_percentage",
        "battery_voltage", "pression_ext", "temp_ext", "temp_int",
        "temp_sea", "ec_sea", "depth"
    ]
    assert df.columns.tolist() == expected_columns
