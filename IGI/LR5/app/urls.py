from django.urls import path, re_path
from app.views import (aboutView, authView, contactsView, faqView, homeView, newsView, privacyPolicyView,
                       promoView, ratesView, vacanciesView, productView, profileView, cartView, adminView)


urlpatterns = [
    path('', homeView.home, name="home"),
    path('login/', authView.LoginView.as_view(), name='login'),
    path('sign-up/', authView.SignUpView.as_view(), name='sign-up'),
    path('logout/', authView.LogoutView.as_view(), name='logout'),

    path('about/', aboutView.AboutView.as_view(), name='about'),
    path('news/', newsView.NewsView.as_view(), name='news'),
    path('faq/', faqView.FaqView.as_view(), name='faq'),
    path('contacts/', contactsView.ContactsView.as_view(), name='contacts'),
    path('privacy-policy/', privacyPolicyView.PrivacyPolicy.as_view(), name='privacy-policy'),
    path('vacancies/', vacanciesView.VacanciesView.as_view(), name='vacancies'),
    path('rates/', ratesView.RatesView.as_view(), name='rates'),
    path('promos/', promoView.PromoView.as_view(), name='promos'),

    path('products/', productView.ProductView.as_view(), name='products'),
    re_path(r'^products/(?P<product_id>\d+)$', productView.ProductDetailView.as_view(), name='product-details'),

    path('profile/', profileView.ProfileView.as_view(), name='profile'),
    path('cart/', cartView.CartView.as_view(), name='cart'),

    path('admin-panel/', adminView.AdminView.as_view(), name='admin'),

    # path('about/', ),
    # path('contacts/', ),
    # path('faq/', ),
    # path('news/', ),
    # path('privacy-policy/', ),
    # path('promos/', ),
    # path('rates/', ),
    # path('vacancies/', )
]
