from django.core.mail import send_mail
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Lead
from .forms import CustomUserCreationForm, LeadModelForm, LeadForm

# Create your views here.


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


class LandingPageView(TemplateView):
    template_name = "landing.html"


# def landing_page(request):
#     return render(request, "landing.html")


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "Leads"


# def lead_list(request):
#     leads = Lead.objects.all()
#     context = {
#         "Leads": leads
#     }
#     return render(request, "leads/lead_list.html", context)


class LeadDetailView(LoginRequiredMixin, DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

# def lead_detail(request, pk):
#     lead = Lead.objects.get(id=pk)
#     context = {
#         "lead": lead
#     }
#     return render(request, "leads/lead_detail.html", context)


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        # overriding this method to allow me to do something in between

        send_mail(
            subject="A lead has been created",
            message="Go to site to see the new lead",
            from_email="test@test.com",
            recipient_list=["gabrielpitaromero@gmail.com"]
        )

        return super(LeadCreateView, self).form_valid(form)


# def lead_create(request):
#     form = LeadModelForm()
#     if request.method == "POST":
#         form = LeadModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


# def lead_update(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadModelForm(instance=lead)
#     if request.method == "POST":
#         form = LeadModelForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("/leads")
#     context = {
#         "form": form,
#         "lead": lead
#     }
#     return render(request, "leads/lead_update.html", context)


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


# def lead_delete(request, pk):
#     lead = Lead.objects.get(id=pk)
#     lead.delete()
#     return redirect("/leads")
