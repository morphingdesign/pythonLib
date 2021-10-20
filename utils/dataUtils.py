import openpyxl


def extractDataFromXL(spreadsheet):
    """
    Extract data from spreadsheet file.

    spreadsheet is a string dir path.

    """

    dataList = []
    workbook = openpyxl.load_workbook(spreadsheet)
    sheet = workbook['Sheet1']

    for i in range(1, 100):
        data = sheet.cell(row=i, column=2).value

        # Exit loop before printing a None value.
        if data == None:
            break
        else:
            dataList.append(data)

    return dataList


XLfile = "../data/testData.xlsx"
print(extractDataFromXL(XLfile))