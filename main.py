from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1N2e3kVyWOEa5nhEneaUFG7zqFK2Qd00dUc1x7cjAOLs'  
service = build('sheets', 'v4', credentials=creds)

movie_name = input("Enter the movie that you have recently seen: ")
genre = input("Enter the genre of the movie: ")
release_date = input('Enter the release date of the movie: ')
director = input("Enter the name of the director: ")
actors = input("Enter the names of the actors: ")

# Call the Sheets API
sheet = service.spreadsheets()
data=[[movie_name, genre, release_date, director, actors]]
request = request = sheet.values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="sheet1!A1", valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body={"values":data}).execute()
print(request)