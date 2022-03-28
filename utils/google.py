import apiclient
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'plan-240009-a5cdae7d141c.json'
ID = '1rQeYMdzimMVF6CjsbIE83VHoC0e0Ra-bjBk5XUv55f4'

# async def write_data_to_google(data):
#     credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
#                                                                    ['https://www.googleapis.com/auth/spreadsheets',
#                                                                     'https://www.googleapis.com/auth/drive'])
#
#     httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
#     service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
#     resp = service.spreadsheets().values().get(spreadsheetId=ID, range="Лист1!A1:A999").execute()
#     print(resp)

credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
resp = service.spreadsheets().values().get(spreadsheetId=ID, range="Лист1!A1:Z999").execute()
print(resp)