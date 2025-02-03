import jsontoexcel
import json

workbook = jsontoexcel.JsonToExcel("data")

# Open and read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Now call createSheet without worrying about the type of `data`
workbook.createSheet("data", data)
workbook.closeWorkbook()
