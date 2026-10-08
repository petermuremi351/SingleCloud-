from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thanks for reaching out! We'll get back to you within 24 hours."
            )
            return redirect("contact")
        else:
            messages.error(request, "Please check the form below and try again.")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def terms(request):
    return render(request, "terms.html")


def privacy(request):
    return render(request, "privacy.html")


def faq(request):
    return render(request, "faq.html")

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "",
        f"Sitemap: https://{request.get_host()}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
