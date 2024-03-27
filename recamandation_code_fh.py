import joblib
 
# Save the model as a pickle in a file
#joblib.dump(XB, 'xg_boost_recomondation_fh.pkl')
 
# Load the model from the file
knn_from_joblib = joblib.load('xg_boost_recomondation_fh.pkl')
 
# Use the loaded model to make predictions


def recondation_fn_fh(input_list1):

					features_list=input_list1

					for i in range(len(features_list)):
					    features_list[i] = float(features_list[i])

					print(features_list)					

					print(features_list)

					import numpy as np


					int_features2 = np.array(features_list)

					int_features1 = int_features2.reshape(1, -1)


					tested1=knn_from_joblib.predict(int_features1)



					print(tested1)

					return(tested1)




