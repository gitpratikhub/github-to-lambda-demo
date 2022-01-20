import pandas as pd
def lambda_handler(event, context):
    d = {'col1':[1,2,3,4,5,6],'col2':[11,22,33,44,55,66]}
    df = pd.DataFrame(data = d)
    print (df)
    print ('done V1.4')
