from rest_framework import viewsets
from apps.task2.api_endpoints.salary.serializers import VacancySerializer
from apps.task2.models import Vacancy


class VacancyFilterViewSet(viewsets.ModelViewSet):
    serializer_class = VacancySerializer

    def get_queryset(self):
        queryset = Vacancy.objects.all()
        salary_from = self.request.query_params.get('salary_from', None)
        salary_to = self.request.query_params.get('salary_to', None)
        salary = self.request.query_params.get('salary', None)

        if salary_from is not None:
            queryset = queryset.filter(salary__gte=salary_from)
        if salary_to is not None:
            queryset = queryset.filter(salary__lte=salary_to)
        if salary is not None:
            queryset = queryset.filter(salary=salary)

        return queryset


__all__ = ["VacancyFilterViewSet"]
