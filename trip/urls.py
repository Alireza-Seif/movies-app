from django.urls import path

from .views import HomeView, TripCreateView, trip_list, TripDetailView, NoteDetailView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("dashboard/", trip_list, name="trip_list"),
    path("dashboard/trip/create/", TripCreateView.as_view(), name="trip-create"),
    path("dashboard/trip/<int:pk>/", TripDetailView.as_view(), name="trip-detail"),
    path("dashboard/note/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
]
