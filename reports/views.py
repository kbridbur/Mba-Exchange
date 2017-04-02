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
    urls = ['Consultant_Client_Round', 'Consultant_Contact_Information', 'Client_Roster']
    if request.method == 'POST':
        if 'Consultant_Client_Round' in request.POST:
            HttpResponseRedirect('/reports/consultant_client_round/')
        elif 'Consultant_Contact_Information' in request.POST:
            HttpResponseRedirect('/reports/consultant_roster/')
        elif 'Client_Roster' in request.POST:
            HttpResponseRedirect('/reports/client_roster/')
    return render(request, 'Addperson/index.html', {'urls':urls})
    
def consultantRoster(request):
    data = CreateConsultantMap()
    return render(request, 'Addperson/reportsmap.html', {'data':data, 'length':len(data)})
    
def clientRoster(request):
    data = CreateClientMap()
    return render(request, 'Addperson/reportsmap.html', {'data':data, 'length':len(data)})

def consultantClientRound(request):
    data = CreateConsultantClientRoundMap()
    return render(request, 'Addperson/reportsmap.html', {'data':data, 'length':len(data)})
    

def CreateClientMap():
    service_list = Service.objects.all()#filter(start_date__range=[str(start_date), str(end_date)])
    admission_list = AddmissionsService.objects.all()
    result_list = list(chain(service_list, admission_list)) 
    
    result = {}
    result[0] = ["Client Last Name", "Client First Name", "Client Email", "Year", "Lead First Name", "Lead Last Name", "Paid", "Sh1", "Sh2", "Sh3", "Sh4", "Sh5", "Sh6", "Comments"]
    
    for idx, data in enumerate(result_list):
    row = 1 + idx
    result[row] = [
      data.client.last_name,
      data.client.first_name,
      data.client.email,
      u"??????",
      data.provider.first_name,
      data.provider.last_name,
      data.provider.payment]
    try:
        for school in data.schools:
            result[row].append(school.name)
    except:
        pass
    result[row].append(data.client.comments)
    
    return result
    
def CreateConsultantMap():
    
    consultants = Consultant.objects.all()

    result = {}
    result[0] = [
      "First Name",
      "Last Name",
      "Email",
      "Alternate Email",
      "Day Phone",
      "Evening Phone",
      "Text",
      "Skype",
      "Rate"
      ]

    for idx, data in enumerate(consultants):
        row = 1 + idx
        result[row] = [
          data.last_name,
          data.first_name,
          data.email,
          data.alternate_email,
          data.day_phone,
          data.evening_phone,
          data.text_phone,
          data.skype,
          data.payment
        ]
    
    return result
    
    
def CreateConsultantClientRoundMap():
    
    consultants = Consultant.objects.all()
    
    result = {}
    result[0] = ["", "Open Capacity Round 1"]
    result[1] = ["", "Open Capacity Round 2"]
    result[4] = ["", "Hourly?"]
    result[5] = ["", "Round 1"]
    result[6] = ["", "Round 2"]
    result[7] = ["", "App check"]
    result[8] = ["", "Editor"]
    result[9] = ["", "Round 1"]
    result[25] = ["", "Round 2"]
    result[41] = ["", "Round 3"]
    result[45] = ["", "Comments"]
    result = fillempty(result, 45)
    
    for idx, data in enumerate(consultants):
      col = 2 + idx
      result[2].append(data.first_name)
      result[3].append(data.last_name)
      if data.hourly_capability:
        result[4].append("yes")
      else:
        result[4].append("no")
      result[5].append(data.round_one_capacity)
      result[6].append(data.round_two_capacity)
      result[8].append(data.editor)
      result[9].append("XXX")
      result[25].append("XXX")
      result[41].append("XXX")
      
      round_one_row = 10
      round_two_row = 26
      round_three_row = 42
      
      for service in consultant.addmissionsservice_set.all():
        if service.entry_round == 1:
          result = writeInPlace(result, str(service.client), round_one_row, col)
          round_one_row += 1
        elif service.entry_round == 2:
          result = writeInPlace(result, str(service.client), round_two_row, col)
          round_two_row += 1
        elif service.entry_round == 3:
          result = writeInPlace(result, str(service.client), round_three_row, col)
          round_three_row += 1
      
      result[0].append(data.round_one_capacity-round_one_row+10)
      result[1].append(data.round_two_capacity-round_two_row+26)
      
    return result
      
def writeInPlace(obj, text, row, col):
    while len(obj[col]) < row:
      obj[col].append("")
    obj[col].append(text)
    return obj

def fillempty(result, num):
    for i in range(num)
      if i not in result:
        result[i] = ["", ""]
    return result
            
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
