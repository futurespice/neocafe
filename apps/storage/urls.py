from django.urls import path

from apps.storage.views import (CreateCategoryView, CreateEmployeeView,
                                CreateIngredientView, DestroyCategoryView,
                                EmployeeDetailView, EmployeeListView,
                                EmployeeUpdateView, IngredientListView,
                                ListCategoryView, ScheduleUpdateView)

urlpatterns = [
    path("categories/", ListCategoryView.as_view()),  # storage/categories/
    path(
        "categories/create/", CreateCategoryView.as_view()
    ),  # storage/categories/create/
    path(
        "categories/destroy/<int:pk>/", DestroyCategoryView.as_view()
    ),  # storage/categories/destroy/<int:pk>/
    path(
        "employees/create/", CreateEmployeeView.as_view()
    ),  # storage/employees/create/
    path("employees/", EmployeeListView.as_view()),  # storage/employees/
    path(
        "employees/<int:pk>/", EmployeeDetailView.as_view()
    ),  # storage/employees/<int:pk>/
    path(
        "employees/update/<int:pk>/", EmployeeUpdateView.as_view()
    ),  # storage/employees/update/<int:pk>/
    path(
        "employees/schedule/update/<int:pk>/", ScheduleUpdateView.as_view()
    ),  # storage/employees/schedule/update/<int:pk>/
    path(
        "ingredients/create/", CreateIngredientView.as_view()
    ),  # storage/ingredients/create/
    path("ingredients/", IngredientListView.as_view()),  # storage/ingredients/
]
