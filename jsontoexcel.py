import sys, json
import xlsxwriter

class json2excel:
    excelbook = None
    excelsheet = {}

    def __init__(self, filename):
        self.excelbook = xlsxwriter.Workbook(filename+".xlsx")

    def createSheet(self, sheetname, jsonData):
        self.excelsheet[sheetname] = self.excelbook.add_worksheet(sheetname)
        data = json.loads(jsonData)

        writeToSheet(self.excelsheet[sheetname], self.excelbook, 0, 1, data, "")
        return self.excelsheet[sheetname]

    def getSheet(self, sheetname):
        return self.excelsheet[sheetname]

    def closeWorkbook(self):
        self.excelbook.close()




def writeToSheet(worksheet, workbook, col, row, data, header):
    xcol = col
    xrow = row

    if type(data) is list:
        for entry in data:
            writeToSheet(worksheet, workbook, col, xrow, entry, header)
            xrow = xrow+1

    elif type(data) is dict:
        for key, value in data.items():
            writeToSheet(worksheet, workbook, xcol, row, value, header + "_" + key)
            xcol = xcol+1

    else:
        bold = workbook.add_format({'bold': True, 'bg_color': 'yellow'})
        worksheet.write(0, col, header, bold)
        worksheet.write(row, col, data)
