
from django.shortcuts import render
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
import xlsxwriter
from itertools import chain

def index(request):


    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=ClientRoster.xlsx'
    xlsx_data = CreateClientRoster(start_date, end_date)
    response.write(xlsx_data)
    return response




def CreateClientRoster(start_date, end_date):
    output = StringIO.StringIO()
    workbook = xlsxwriter.Workbook(output)

    worksheet_s = workbook.add_worksheet("Roster")
    header = workbook.add_format({
    'bg_color': '#F7F7F7',
    'color': 'black',
    'align': 'center',
    'valign': 'top',
    'border': 1
    })

    worksheet_s.write(0, 0, ugettext("Client Last Name"), header)
    worksheet_s.write(0, 1, ugettext("Client First Name"), header)
    worksheet_s.write(0, 2, ugettext("Client email"), header)
    worksheet_s.write(0, 3, ugettext("Year"), header)
    worksheet_s.write(0, 4, ugettext("Lead First Name"), header)
    worksheet_s.write(0, 5, ugettext("Lead Last Name"), header)
    worksheet_s.write(0, 6, ugettext("Paid"), header)
    worksheet_s.write(0, 7, ugettext("Sh1"), header)
    worksheet_s.write(0, 8, ugettext("Sh2"), header)
    worksheet_s.write(0, 9, ugettext("Sh3"), header)
    worksheet_s.write(0, 10, ugettext("Sh4"), header)
    worksheet_s.write(0, 11, ugettext("Sh5"), header)
    worksheet_s.write(0, 12, ugettext("Sh6"), header)
    worksheet_s.write(0, 13, ugettext("Comments"), header)

    service_list = Service.objects.filter(start_date__range=[str(start_date), str(end_date)])
    admission_list = AddmissionsService.objects.filter(start_date__range=[str(start_date), str(end_date)])
    result_list = list(chain(service_list, admission_list))

    for idx, data in enumerate(result_list):
        row = 1 + idx
        school_col = 7
        worksheet_s.write_string(row, 0, data.client.last_name, cell)
        worksheet_s.write_string(row, 1, data.client.first_name, cell)
        worksheet_s.write_string(row, 2, data.client.email, cell)
        worksheet_s.write_string(row, 3, "??????", cell)
        try:
            worksheet_s.write_string(row, 4, data.consultant.first_name, cell)
            worksheet_s.write_string(row, 5, data.consultant.last_name, cell)
            worksheet_s.write_string(row, 6, data.consultant.payment, cell)
        except:
            worksheet_s.write_string(row, 4, data.provider.first_name, cell)
            worksheet_s.write_string(row, 5, data.provider.last_name, cell)
            worksheet_s.write_string(row, 6, data.provider.payment, cell)
        try:
            for school in data.schools:
                worksheet_s.write_string(row, school_col, school.name, cell)
                school_col += 1
        worksheet_s.write_string(row, school_col, data.client.comments, cell)


    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data
