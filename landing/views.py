from . import models
from django.contrib import messages
from account.models import Purchase
from account.forms import ContactForm
from django.shortcuts import render, redirect
from django.utils.timezone import datetime, timedelta
from django.contrib.auth.decorators import login_required


def about_view(request):
    return render(request, "landing/about.html")


def index_view(request):
    apartments = models.Apartment.objects.filter(current__isnull=True)[:9]

    context = {"apartments": apartments}
    return render(request, "landing/index.html", context)


def category_view(request):
    categories = models.Category.objects.all()

    context = {"categories": categories}
    return render(request, "category/index.html", context)


def category_detail_view(request, id):
    category = models.Category.objects.get(id=id)
    apartments = category.apartment_set.filter(current__isnull=True)

    context = {"apartments": apartments, "category": category}
    return render(request, "category/detail.html", context)


@login_required
def detail_view(request, id):
    if request.method == "POST":
        apartment = request.POST.get("apartment")
        month_count = int(request.POST.get("month", 0))

        if month_count:
            apartment = models.Apartment.objects.get(id=id)
            to_date = datetime.now() + timedelta(days=30 * month_count)

            apartment.current = request.user
            Purchase.objects.create(
                apartment=apartment,
                to_date=to_date,
                buyer=request.user,
                total_price=apartment.price * month_count,
            )
            apartment.save()

            messages.success(
                request, f"Apartment rented successfully for {month_count} months"
            )
            return redirect("landing:index-view")

    apartment = models.Apartment.objects.get(id=id)
    if apartment.current:
        messages.warning(request, "The apartment is already rented")
        return redirect("landing:index-view")

    context = {"apartment": apartment}
    return render(request, "landing/detail.html", context)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid() and form.save():
            messages.success(request, "Message sent successfully")
        else:
            messages.error(request, "Message not sent")

        return redirect("landing:contact-view")

    return render(request, "landing/contact.html")
