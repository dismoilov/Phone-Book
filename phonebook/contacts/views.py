from django.http import HttpResponse
from .models import Contact, Call
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.timezone import now
from rest_framework import status


def download_xml(request):
    xml_data = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    xml_data += '<ContactData>\n'
    xml_data += '    <Group Id="1" Name="Default" Ring="Auto" Description="">\n'

    contacts = Contact.objects.all()
    n = 0
    for contact in contacts:
        mobile_number = contact.MobileNumber or ''
        other_number = contact.OtherNumber or ''
        n += 1
        xml_data += (f'        <Contact Id="{n}" Line="0" DisplayName="{contact.DisplayName}" '
                     f'OfficeNumber="{contact.OfficeNumber}" MobileNumber="{mobile_number}" '
                     f'OtherNumber="{other_number}" Ring="Auto" Photo="" />\n')

    xml_data += '    </Group>\n'
    xml_data += '</ContactData>\n'

    response = HttpResponse(xml_data, content_type='text/xml')
    response['Content-Disposition'] = 'attachment; filename="contacts.xml"'
    return response


def view_xml(request):
    xml_data = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    xml_data += '<ContactData>\n'
    xml_data += '    <Group Id="1" Name="Default" Ring="Auto" Description="">\n'

    contacts = Contact.objects.all()
    n = 0
    for contact in contacts:
        mobile_number = contact.MobileNumber or ''
        other_number = contact.OtherNumber or ''
        n += 1
        xml_data += (f'        <Contact Id="{n}" Line="0" DisplayName="{contact.DisplayName}" '
                     f'OfficeNumber="{contact.OfficeNumber}" MobileNumber="{mobile_number}" '
                     f'OtherNumber="{other_number}" Ring="Auto" Photo="" />\n')

    xml_data += '    </Group>\n'
    xml_data += '</ContactData>\n'

    return HttpResponse(xml_data, content_type='text/xml; charset=utf-8')


@api_view(['GET'])
def incoming_call(request):
    call_id = request.GET.get('call_id')
    remote = request.GET.get('remote')
    local = request.GET.get('local')

    if not call_id or not remote or not local:
        return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)

    # Определяем тип звонка
    call_type = "incoming"
    if len(local) < 5 and len(remote) < 5:
        call_type = "local"

    call, created = Call.objects.get_or_create(
        call_id=call_id,
        defaults={
            "caller": remote,
            "receiver": local,
            "call_type": call_type,
            "date": now().date(),
            "time": now().time(),
        }
    )

    if not created:
        return Response({"message": "Call already exists"}, status=status.HTTP_200_OK)

    return Response({"message": "Incoming call registered"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def outgoing_call(request):
    call_id = request.GET.get('call_id')
    remote = request.GET.get('remote')
    local = request.GET.get('local')

    if not call_id or not remote or not local:
        return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)

    if len(local) < 5 and len(remote) < 5:
        call_type = "local"
    else:
        call_type = "outgoing"

    call, created = Call.objects.get_or_create(
        call_id=call_id,
        defaults={
            "caller": local,
            "receiver": remote,
            "call_type": call_type,
            "date": now().date(),
            "time": now().time(),
        }
    )

    if not created:
        return Response({"message": "Call already exists"}, status=status.HTTP_200_OK)

    return Response({"message": "Outgoing call registered"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def missed_call(request):
    call_id = request.GET.get('call_id')
    remote = request.GET.get('remote')
    local = request.GET.get('local')

    if not call_id or not remote or not local:
        return Response({"error": "Missing parameters"}, status=status.HTTP_400_BAD_REQUEST)

    call, created = Call.objects.get_or_create(
        call_id=call_id,
        defaults={
            "caller": remote,
            "receiver": local,
            "call_type": "missed",
            "date": now().date(),
            "time": now().time(),
        }
    )

    if not created:
        return Response({"message": "Call already exists"}, status=status.HTTP_200_OK)

    return Response({"message": "Missed call registered"}, status=status.HTTP_201_CREATED)
