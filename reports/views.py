from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
try:
    from BytesIO import BytesIO
except ImportError:
    from io import BytesIO
import xlsxwriter
from itertools import chain
from AddPerson.models import *

def index(request):
    options = ['Consultant_Client_Round', 'Consultant_Contact_Information', 'Client_Roster']
    output = CreateConsultantClientRound()
    response = HttpResponse(output.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=ConsultantClientRound.xlsx'
    return response
    if request.method == 'POST':
        print("hi")
        if 'Consultant_Client_Round' in request.POST:
            print("hi")
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=ConsultantClientRound.xlsx'
            xlsx_data = CreateConsultantClientRound()
            response.write(xlsx_data)
            return response
        elif 'Consultant_Contact_Information' in request.POST:
            response = HttpResponse(content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=ConsultantContactInfo.xlsx'
            xlsx_data = CreateConsultantInfo()
            response.write(xlsx_data)
            return response
        elif 'Client_Roster' in request.POST:
            response = HttpResponse(content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename=ClientRoster.xlsx'
            xlsx_data = CreateClientRoster()
            response.write(xlsx_data)
            return response



def CreateConsultantClientRound():

    consultants = Consultant.objects.all()

    output = BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory' : True})

    worksheet_s = workbook.add_worksheet("ConsultantClientRound")
    x = worksheet_s.write_string(0, 0,  "ACTIVE")
    print(x)

    '''
    worksheet_s.write(0, 1,  u"Open capacity round 1")
    worksheet_s.write(1, 1,  u"Open capacity round 2")
    worksheet_s.write(4, 1,  u"Hourly?")
    worksheet_s.write(5, 1,  u"round 1")
    worksheet_s.write(6, 1,  u"round 2")
    worksheet_s.write(7, 1,  u"App check")
    worksheet_s.write(8, 1,  u"Editor")
    worksheet_s.write(9, 1,  u"Round 1")
    worksheet_s.write(25, 1,  u"Round 2")
    worksheet_s.write(41, 1,  u"Round 3")
    worksheet_s.write(45, 0,  u"Comments")

    col = 2
    for idx, data in enumerate(consultants):
        worksheet_s.write(2, col, data.first_name)
        worksheet_s.write(3, col, data.last_name)
        if data.hourly_capability:
            worksheet_s.write(4, col, 'yes')
        else:
            worksheet_s.write(4, col, 'no')
        worksheet_s.write(5, col, data.round_one_capacity)
        worksheet_s.write(6, col, data.round_two_capacity)
        worksheet_s.write(8, col, str(data.editor))
        worksheet_s.write(9, col, "XXX")
        worksheet_s.write(25, col, "XXX")
        worksheet_s.write(41, col, "XXX")

        round_one_row = 10
        round_two_row = 26
        round_three_row = 42

        for service in data.addmissionsservice_set.all():
            if service.entry_round == 1:
                worksheet_s.write(round_one_row, col, str(service.client))
                round_one_row += 1
            elif service.entry_round == 2:
                worksheet_s.write(round_two_row, col, str(service.client))
                round_two_row += 1
            elif service.entry_round == 3:
                worksheet_s.write(round_three_row, col, str(service.client))
                round_three_row += 1

        worksheet_s.write(0, col, data.round_one_capacity - round_one_row + 10)
        worksheet_s.write(1, col, data.round_two_capacity - round_two_row + 26)

        col += 1
        '''
    workbook.close()
    output.seek(0)
    return output

def CreateConsultantInfo():
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)

    worksheet_s = workbook.add_worksheet("ConsultantInfo")

    consultants = Consultant.objects.all()

    worksheet_s.write(0, 1,  u"First Name")
    worksheet_s.write(0, 0,  u"Last Name")
    worksheet_s.write(0, 2,  u"Email")
    worksheet_s.write(0, 3,  u"Alternate Email")
    worksheet_s.write(0, 4,  u"Day Phone")
    worksheet_s.write(0, 5,  u"Evening Phone")
    worksheet_s.write(0, 6,  u"Text")
    worksheet_s.write(0, 7,  u"Skype")
    worksheet_s.write(0, 8,  u"Rate")

    for idx, data in enumerate(consultants):
        row = 1 + idx
        worksheet_s.write(row, 0, data.last_name)
        worksheet_s.write(row, 1, data.first_name)
        worksheet_s.write(row, 2, data.email)
        worksheet_s.write(row, 3, data.alternate_email)
        worksheet_s.write(row, 4, data.day_phone)
        worksheet_s.write(row, 5, data.evening_phone)
        worksheet_s.write(row, 6, data.text_phone)
        worksheet_s.write(row, 7, data.skype)
        worksheet_s.write(row, 8, data.payment)

    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data



def CreateClientRoster():
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)

    worksheet_s = workbook.add_worksheet("Roster")

    worksheet_s.write(0, 0,  u"Client Last Name")
    worksheet_s.write(0, 1,  u"Client First Name")
    worksheet_s.write(0, 2,  u"Client email")
    worksheet_s.write(0, 3,  u"Year")
    worksheet_s.write(0, 4,  u"Lead First Name")
    worksheet_s.write(0, 5,  u"Lead Last Name")
    worksheet_s.write(0, 6,  u"Paid")
    worksheet_s.write(0, 7,  u"Sh1")
    worksheet_s.write(0, 8,  u"Sh2")
    worksheet_s.write(0, 9,  u"Sh3")
    worksheet_s.write(0, 10, u"Sh4")
    worksheet_s.write(0, 11,  u"Sh5")
    worksheet_s.write(0, 12,  u"Sh6")
    worksheet_s.write(0, 13, u"Comments")

    service_list = Service.objects.all()#filter(start_date__range=[str(start_date), str(end_date)])
    admission_list = AddmissionsService.objects.all()#filter(start_date__range=[str(start_date), str(end_date)])
    result_list = list(chain(service_list, admission_list))

    for idx, data in enumerate(result_list):
        row = 1 + idx
        school_col = 7
        worksheet_s.write(row, 0, data.client.last_name)
        worksheet_s.write(row, 1, data.client.first_name)
        worksheet_s.write(row, 2, data.client.email)
        worksheet_s.write(row, 3, u"??????")
        worksheet_s.write(row, 4, data.provider.first_name)
        worksheet_s.write(row, 5, data.provider.last_name)
        worksheet_s.write(row, 6, data.provider.payment)
        try:
            for school in data.schools:
                worksheet_s.write(row, school_col, school.name)
                school_col += 1
        except:
            pass
        worksheet_s.write(row, school_col, data.client.comments)


    workbook.close()
    xlsx_data = output.getvalue()
    # xlsx_data contains the Excel file
    return xlsx_data
