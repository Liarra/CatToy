from django.http import HttpResponse
from django.shortcuts import render
from ToyController.executables import toy_controller


# Create your views here.


def control_page(request):
    context = {}
    return render(request, "ToyController/control_page_template.html", context)


def control(request):
    request_number = int(request.POST["number"])
    request_value = float(request.POST["value"]) / 10.0

    print(request_number,request_value)

    print (toy_controller.move_toy(request_value, request_number))
    return HttpResponse("OK")
