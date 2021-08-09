from rest_framework.exceptions import ValidationError

from mega.models import Looking, Company


def counts_views(company):
    views = Looking.objects.get(pk=company.id)
    views.counter += 1
    views.save()


def get_object(pk):
    try:
        return Company.objects.get(pk=pk)
    except Company.DoesNotExist:
        raise ValidationError