from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet,
    AccountViewSet,
    TransactionViewSet,
    BudgetViewSet,
    GoalViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)  # has .queryset, no basename needed
router.register(r'accounts', AccountViewSet, basename='account')
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'budgets', BudgetViewSet, basename='budget')
router.register(r'goals', GoalViewSet, basename='goal')

urlpatterns = [
    path('', include(router.urls)),
]
