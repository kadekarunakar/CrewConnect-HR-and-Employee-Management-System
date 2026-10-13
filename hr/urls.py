from hr import views
from django.urls import path

urlpatterns = [
    path("", views.login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
    # path("viewemployees/", viewemployees, name="viewemployees"),
    path("employees/",views.employee_list,name='employee_list'),
    path("employees/add/",views.employee_create,name='employee_create'),
    path("employees/<int:id>/edit/", views.employee_update, name="employee_update"),
    path("employees/<int:id>/delete/", views.employee_delete, name="employee_delete"),
    path("leave_approve",views.leave_approve,name="leave_approve"),
    path("leave/<int:id>/action/",views.leave_action,name="leave_action"),

    path("departments/",views.department_list,name="department_list"),
    path("departments/add/", views.department_create,name="department_create"),
    path("departments/edit/<int:pk>/", views.department_update,name="department_update" ),
    path("departments/delete/<int:pk>/",views.department_delete,name="department_delete"),

    path(
        "hr/calendar-management/",
        views.hr_calendar_management,
        name="hr_calendar_management",
    ),
    path(
        "leave-calendar/events/",
        views.leave_calendar_events,
        name="leave_calendar_events",
    ),
    path(
        "holiday-calendar/events/",
        views.employee_holiday_events,
        name="employee_holiday_events",
    ),


]