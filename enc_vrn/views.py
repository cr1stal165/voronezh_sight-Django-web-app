from django.shortcuts import render
from enc_vrn.models import Excursion, Address
from enc_vrn.models import Sight
from enc_vrn.models import Architect
from enc_vrn.models import History
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@csrf_protect
@csrf_exempt
def index(request):

    search_query = request.GET.get('search', '')
    filter_query = request.GET.get('filter_sight', '')
    author = request.GET.get('arch', '')
    if search_query:
        exc = Sight.objects.filter(sight_name__contains=search_query)
    elif filter_query:
        exc = Sight.objects.filter(building_date__lte=filter_query) & Sight.objects.filter(architect_id__exact=author)
    else:
        exc = Sight.objects.all()

    p = Paginator(exc, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    arch = Architect.objects.all()
    add = Address.objects.all()
    his = History.objects.all()
    return render(request, "index.html", context={'exc': exc, 'arch': arch, 'address': add, 'his': his,
                                                  'page_obj': page_obj})


@csrf_protect
@csrf_exempt
@ensure_csrf_cookie
def add_sight(request):
    return render(request, "add_sight.html")


@csrf_protect
@csrf_exempt
def add_excursion(request):
    return render(request, "add_excursion.html")


@csrf_protect
@csrf_exempt
@ensure_csrf_cookie
def show_sight(request, sight_id, his_id):
    sight = Sight.objects.get(id=sight_id)
    his = History.objects.get(sight_id=his_id)
    return render(request, "show_sight.html", context={'exc': sight, 'hs': his})


@csrf_protect
@csrf_exempt
@ensure_csrf_cookie
def confirm_add_sight(request):
    if request.method == 'POST':
        architect = Architect.objects.create(name="", year_of_birth=0, year_of_death=0)
        architect.name = request.POST.get('fio')
        architect.year_of_birth = request.POST.get('date_birth')
        architect.year_of_death = request.POST.get('date_death')
        architect.save()

        address = Address.objects.create(district="", street="", house="")
        address.district = request.POST.get('district')
        address.street = request.POST.get('street')
        address.house = request.POST.get('house')
        address.save()

        sight = Sight.objects.create(sight_name="", building_date=0, image="", address_id=address.id,
                                     architect_id=architect.id)
        sight.sight_name = request.POST.get('sight')
        sight.building_date = request.POST.get('build_date')
        sight.image = request.FILES.get('file-input')
        sight.save()

        his = History.objects.create(history="", excursion_id=None, sight_id=sight.id)
        his.history = request.POST.get('history_text')
        his.save()

        print(request.FILES.get('file-input'))
        print(sight.image)
    return render(request, "confirm_add_sight.html")


@csrf_protect
@csrf_exempt
@ensure_csrf_cookie
def edit_sight(request, sight_id, his_id):
    sight = Sight.objects.get(id=sight_id)
    his = History.objects.get(sight_id=his_id)
    return render(request, "edit_sight.html", context={'sight': sight, 'his': his})


@csrf_protect
@csrf_exempt
@ensure_csrf_cookie
def delete_sight(request, sight_id, his_id):
    sight = Sight.objects.get(id=sight_id)
    his = History.objects.get(sight_id=his_id)
    address = Address.objects.get(id=sight.address_id)
    architect = Architect.objects.get(id=sight.architect_id)
    architect.delete()
    address.delete()
    his.delete()
    sight.delete()
    return render(request, "delete_sight.html")


@csrf_protect
@csrf_exempt
@ensure_csrf_cookie
def confirm_edit_sight(request, sight_id, his_id):
    if request.method == 'POST':
        sight = Sight.objects.get(id=sight_id)
        sight.sight_name = request.POST.get('sight')
        sight.building_date = request.POST.get('build_date')
        sight.save(update_fields=["sight_name", "building_date"])

        his = History.objects.get(id=his_id)
        his.history = request.POST.get('history_text')
        his.save(update_fields=["history"])

        address = Address.objects.get(id=sight.address_id)
        address.district = request.POST.get('district')
        address.street = request.POST.get('street')
        address.house = request.POST.get('house')
        address.save(update_fields=["district", "street", "house"])

        architect = Architect.objects.get(id=sight.architect_id)
        architect.name = request.POST.get('fio')
        architect.year_of_birth = request.POST.get('date_birth')
        architect.year_of_death = request.POST.get('date_death')
        architect.save(update_fields=["name", "year_of_birth", "year_of_death"])

    return render(request, "confirm_edit_sight.html")


def show_excursion(request):
    exc = Excursion.objects.all()
    p = Paginator(exc, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:

        page_obj = p.page(1)
    except EmptyPage:

        page_obj = p.page(p.num_pages)
    return render(request, "show_excursion.html", context={'exc' : exc, 'page_obj': page_obj})


def show_architectors(request):
    architect = Architect.objects.all()
    p = Paginator(architect, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:

        page_obj = p.page(1)
    except EmptyPage:

        page_obj = p.page(p.num_pages)
    return render(request, "show_architectors.html", context={'architect' : architect, 'page_obj': page_obj})


def edit_excursion():
    pass


def delete_excursion():
    pass

