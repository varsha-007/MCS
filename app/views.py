from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import *
from .models import *

# Create your views here.


@login_required(login_url="log-in")
def index(request):
    context = {
        "forward_physical_values": ForwardPhysicalValues.objects.all(),
        "seaborne_last_traded_levels": SeaborneLastTradedLevels.objects.all(),
        "forward_physical_text_card": ForwardPhysicalTextCard.objects.all(),
        "prem_or_disc_table": PremOrDiscTable.objects.all(),
        "proxy_blend_table": ProxyBlendTable.objects.all(),
        "other_product_values_table": OtherProductValuesTable.objects.all(),
        "primaryvs_secondary_differential_table": PrimaryvsSecondaryDifferentialTable.objects.all(),
        "onshore_values": OnshoreValues.objects.all(),
        "onshore_values": OnshoreValues.objects.all(),
        "mysteel_table": MysteelTable.objects.all(),
        "futures_table": FuturesTable.objects.all(),
        "futures_sub_table": FuturesSubTable.objects.all(),
        "secondary_offer": SecondaryOffer.objects.all(),
        "port_side_iron": PortSideIron.objects.all(),
        "port_side_iron_text_card1": PortSideIronTextCard1.objects.all(),
        "port_side_iron_text_card2": PortSideIronTextCard2.objects.all(),
    }
    return render(request, "index.html", context)


@login_required(login_url="log-in")
def clean_data(request):
    ForwardPhysicalValues.objects.all().delete()
    SeaborneLastTradedLevels.objects.all().delete()
    ForwardPhysicalTextCard.objects.all().delete()
    PremOrDiscTable.objects.all().delete()
    ProxyBlendTable.objects.all().delete()
    OtherProductValuesTable.objects.all().delete()
    PrimaryvsSecondaryDifferentialTable.objects.all().delete()
    OnshoreValues.objects.all().delete()
    OnshoreValues.objects.all().delete()
    MysteelTable.objects.all().delete()
    FuturesTable.objects.all().delete()
    FuturesSubTable.objects.all().delete()
    SecondaryOffer.objects.all().delete()
    PortSideIron.objects.all().delete()
    PortSideIronTextCard1.objects.all().delete()
    PortSideIronTextCard2.objects.all().delete()
    messages.success(
        request,
        "All the data is cleared. New data can be added from admin panel",
    )
    return redirect("index")


def sign_up(request):
    signup_form = CreateUserForm()
    if request.method == "POST":
        signup_form = CreateUserForm(request.POST)
        if signup_form.is_valid:
            signup_form.save()
            messages.success(
                request,
                "Account created, Try to login",
            )
            return redirect("log-in")
        else:
            messages.error(
                request,
                "Make sure that password contains at-least 8 characters!",
            )

    context = {"signup_form": signup_form}
    return render(request, "signup.html", context)


def log_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f" Account authenticated successfully!.")
            return redirect("index")
        else:
            messages.error(request, "Username or password is not valid, Try again")

            return redirect("sign-up")
    return render(request, "login.html")


#      Log out
def logout_user(request):
    logout(request)
    return redirect("log-in")
