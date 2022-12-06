import requests

API_KEY = "ko42iLTdBtcJzrUEGNl5c6BQ1cBiJesZNPMric43ahVu"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={
                               "apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
header = {'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + mltoken}
#ip = float(input('Enter Your Marks: '))
# NOTE: manually define and pass the array(s) of values to be scored in the next line


def predictRank(ip):
    payload_scoring = {"input_data": [
        {"fields": ['AGGREGATE_MARK'], "values": [[ip]]}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/79f8a59e-ac4c-4979-a5dd-e57af9dba42a/predictions?version=2022-12-02', json=payload_scoring,
                                     headers={'Authorization': 'Bearer ' + mltoken})
    pred_Rank = round(response_scoring.json()[
                      'predictions'][0]['values'][0][0][0])
    return pred_Rank


def predictRound(ip):
    payload_scoring2 = {"input_data": [
        {"fields": ['RANK'], "values": [[ip]]}]}
    response_scoring2 = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/8a5e830f-f2d5-4e67-a393-195f96c8d32f/predictions?version=2022-12-02', json=payload_scoring2,
                                      headers={'Authorization': 'Bearer ' + mltoken})
    pred_Round = response_scoring2.json()['predictions'][0]['values'][0][0][0]
    if (pred_Round < 1):
        pred_Round = 1
    elif pred_Round > 4:
        pred_Round = 4
    else:
        pred_Round = round(pred_Round)
    return pred_Round
