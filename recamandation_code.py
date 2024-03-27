import joblib
 

knn_from_joblib = joblib.load('flight_price.pkl')
 



#features_list=[                   'area',             'temperature',
    #                'wind_speed',           'precipitation',
   #                   'humidity',                       'N',
   #                          'P',                       'K',
   #                 'AHMEDNAGAR',                   'AKOLA',
   #                   'AMRAVATI',              'AURANGABAD',
   #                       'BEED',                'BHANDARA',
   #                   'BULDHANA',              'CHANDRAPUR',
   #                      'DHULE',              'GADCHIROLI',
   #                     'GONDIA',                 'HINGOLI',
   #                    'JALGAON',                   'JALNA',
   #                   'KOLHAPUR',                   'LATUR',
   #                     'NAGPUR',                  'NANDED',
   #                  'NANDURBAR',                  'NASHIK',
   #                  'OSMANABAD',                 'PALGHAR',
   #                   'PARBHANI',                    'PUNE',
   #                     'RAIGAD',               'RATNAGIRI',
   #                     'SANGLI',                  'SATARA',
   #                 'SINDHUDURG',                 'SOLAPUR',
   #                      'THANE',                  'WARDHA',
   #                     'WASHIM',                'YAVATMAL',
   #                'Kharif     ',             'Rabi       ',
   #                'Summer     ',             'Whole Year ',
   #                  'Arhar/Tur',                   'Bajra',
   #                'Castor seed',            'Cotton(lint)',
   #                       'Gram',               'Groundnut',
   #                      'Jowar',                 'Linseed',
     #                    'Maize',       'Moong(Green Gram)',
    #                'Niger seed',      'Other  Rabi pulses',
   #    'Other Cereals & Millets',     'Other Kharif pulses',
   #                       'Ragi',       'Rapeseed &Mustard',
   #                       'Rice',               'Safflower',
   #                    'Sesamum',                'Soyabean',
   #                  'Sugarcane',               'Sunflower',
   #                    'Tobacco',                    'Urad',
   #                      'Wheat',          'other oilseeds',
   #                         2004,                      2005,
   #                         2006,                      2007,
   #                         2008,                      2009,
   #                         2010,                      2011,
   #                         2012,                      2013,
   #                         2014,             'Maharashtra',
   #                     'chalky',                    'clay',
  #                       'loamy',                   'peaty',
  #                       'sandy',                    'silt',
 #                       'silty']
#for p in range(91):

#  features_list[p]=0

#print(features_list)

import numpy as np

def yield_fn(features_list):
                int_features2 = np.array(features_list)

                int_features1 = int_features2.reshape(1, -1)


                tested1=knn_from_joblib.predict(int_features1)



                print(tested1)

                return  tested1

