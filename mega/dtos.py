from mega.models import Looking


class CompanyDto:
    def __init__(self, company):
        self.name = company.name
        self.city = company.address.city
        self.status = company.status
        self.view_count = Looking.objects.get(pk=company)