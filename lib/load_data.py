import xlrd

# 打开一个excel 并获取到指定的工作表
def get_sheet(file, name):
    excel = xlrd.open_workbook(file)
    sheet = excel.sheet_by_name(name)
    return sheet

# 从一个工作表中找到 指定用例名的 用例数据
def get_case(sheet, case_name):
    for i in range(1, sheet.nrows):
        if sheet.cell(i, 0).value==case_name:
            return sheet.row_values(i)
    return None

if __name__ == '__main__':
    sheet = get_sheet("test_data.xlsx", "add")
    print(get_case(sheet, "test_add_card_exist"))