from django.shortcuts import render
from django.views.generic.base import TemplateView
from .forms import ModelWithCSVForm
from .models import ModelWithCSV


class Index(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['options'] = ModelWithCSV.OPTIONS
        obj = ModelWithCSV.objects.first()
        context['object'] = obj
        context['form'] = ModelWithCSVForm(instance=context['object'])
        return context

    def post(self, request):
        context = self.get_context_data()
        data = request.POST.copy()
        data['csv_field'] = ','.join(data.getlist('csv_field'))

        form = ModelWithCSVForm(data, instance=context['object'])
        if form.is_valid():
            obj = form.save()
            context['message'] = 'saved! - csv_field = "{}"'.format(obj.csv_field)
        else:
            context['message'] = 'error!'

        context['form'] = form
        return render(request, self.template_name, context)
