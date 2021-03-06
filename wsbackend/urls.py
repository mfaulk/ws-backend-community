"""wsbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

from rest import views

schema_view = get_schema_view(title="Web Sight REST API")
swagger_view = get_swagger_view(title="Web Sight REST API")

handler404 = views.custom404

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    # Organization URLs

    url(r'^organizations/(?P<pk>[-\w]+)/quick-scan/?$', views.quick_scan_organization, name="organization-quickscan"), #TESTED
    url(r'^organizations/(?P<pk>[-\w]+)/orders/?$', views.OrdersByOrganizationView.as_view(), name="organizationorder-list"), #TESTED
    url(r'^organizations/(?P<pk>[-\w]+)/es/domain-names/analytics/?$', views.OrganizationDomainNameReportAnalyticsAPIView.as_view(), name="organizationdomainnamereport-analytics"),
    url(r'^organizations/(?P<pk>[-\w]+)/es/domain-names/by-parent-domain/(?P<domain>[^/]+)/?$', views.DomainNameReportByParentDomainListAPIView.as_view(), name="organizationdomainnamereportbyparentdomain-detail"),
    url(r'^organizations/(?P<pk>[-\w]+)/es/domain-names/by-domain/(?P<domain>[^/]+)/?$', views.DomainNameReportByDomainDetailAPIView.as_view(), name="organizationdomainnamereportbydomain-detail"),
    url(r'^organizations/(?P<pk>[-\w]+)/es/domain-names/?$', views.OrganizationDomainNameReportListAPIView.as_view(), name="organizationdomainnamereport-list"),
    url(r'^organizations/(?P<pk>[-\w]+)/es/ssl-support/analytics/?$', views.OrganizationSslSupportReportAnalyticsAPIView.as_view(), name="organizationsslsupport-analytics"),
    url(r'^organizations/(?P<pk>[-\w]+)/es/ssl-support/by-domain/(?P<domain>[^/]+)/?$', views.SslSupportReportByDomainListAPIView.as_view(), name="organizationsslsupportbydomain-list"), #TESTED
    url(r'^organizations/(?P<pk>[-\w]+)/es/ssl-support/by-ip/(?P<ip>[^/]+)/?$', views.SslSupportReportByIpListAPIView.as_view(), name="organizationsslsupportbyip-list"), #TESTED
    url(r'^organizations/(?P<pk>[-\w]+)/es/ssl-support/?$', views.OrganizationSslSupportReportListAPIView.as_view(), name="organizationsslsupport-list"),
    url(r'^organizations/(?P<pk>[-\w]+)/permissions/?$', views.organization_permissions, name="organizationpermission-details"),
    url(r'^organizations/(?P<pk>[-\w]+)/users/?$', views.OrganizationUserAdminAPIView.as_view(), name="organizationuser-admin"),
    url(r'^organizations/(?P<pk>[-\w]+)/networks/upload/?$', views.upload_networks_file, name="orgnetworks-upload"),
    url(r'^organizations/(?P<pk>[-\w]+)/networks/?$', views.NetworksByOrganizationView.as_view(), name="orgnetworks-list"),
    url(r'^organizations/(?P<pk>[-\w]+)/domain-names/upload/?$', views.DomainsUploadAPIView.as_view(), name="orgdomainnames-upload"),
    url(r'^organizations/(?P<pk>[-\w]+)/domain-names/?$', views.DomainNamesByOrganizationView.as_view(), name="orgdomainnames-list"),
    url(r'^organizations/(?P<pk>[-\w]+)/scan-config/set/?$', views.set_organization_scan_config, name="orgscanconfig-set"),
    url(r'^organizations/(?P<pk>[-\w]+)/scan-config/?$', views.retrieve_organization_scan_config, name="orgscanconfig-details"),
    url(r'^organizations/(?P<pk>[-\w]+)/es/web-services/analytics/?$', views.OrganizationWebServiceReportAnalyticsAPIView.as_view(), name="organizationwebreport-analytics"),
    url(r'^organizations/(?P<pk>[-\w]+)/es/web-services/by-domain/(?P<domain>[^/]+)/?$', views.WebServiceReportByDomainListAPIView.as_view(), name="organizationwebreportbydomain-list"), #TESTED
    url(r'^organizations/(?P<pk>[-\w]+)/es/web-services/by-ip/(?P<ip>[^/]+)/?$', views.WebServiceReportByIpAddressListAPIView.as_view(), name="organizationwebreportbyip-list"), #TESTED
    url(r'^organizations/(?P<pk>[-\w]+)/es/web-services/?$', views.OrganizationWebServiceReportListAPIView.as_view(), name="organizationwebreport-list"),
    url(r'^organizations/(?P<pk>[-\w]+)/es/ip-addresses/analytics/?$', views.OrganizationIpAddressReportAnalyticsAPIView.as_view(), name="organizationipreport-analytics"), #TESTED
    url(r'^organizations/(?P<pk>[-\w]+)/es/ip-addresses/by-ip/(?P<ip>[^/]+)/?$', views.IpAddressReportByIpDetailAPIView.as_view(), name="organizationipreportbyip-detail"), #TESTED
    url(r'^organizations/(?P<pk>[-\w]+)/es/ip-addresses/?$', views.OrganizationIpAddressReportListAPIView.as_view(), name="organizationipreport-list"), #TESTED
    url(r'^organizations/(?P<pk>[-\w]+)/?$', views.OrganizationDetailView.as_view(), name="organization-detail"),
    url(r'^organizations/?$', views.OrganizationListView.as_view(), name="organization-list"),

    # IP Address URLs

    url(r'^ip-addresses/(?P<pk>[-\w]+)/es/?$', views.IpAddressReportDetailAPIView.as_view(), name="ipaddressreport-detail"), #TESTED

    # Order URLs

    url(r'^orders/(?P<pk>[-\w]+)/domain-names/?$', views.DomainNamesByOrderView.as_view(), name="orderdomainnames-list"),
    url(r'^orders/(?P<pk>[-\w]+)/networks/?$', views.NetworksByOrderView.as_view(), name="ordernetworks-list"),
    url(r'^orders/(?P<pk>[-\w]+)/place/?$', views.place_order, name="order-place"),
    url(r'^orders/(?P<pk>[-\w]+)/?$', views.OrderDetailView.as_view(), name="order-detail"),
    url(r'^orders/?$', views.OrderListView.as_view(), name="order-list"),

    # Web Service URLs

    url(r'^web-services/(?P<pk>[-\w]+)/es/resources/analytics/?$', views.WebServiceResourceAnalyticsAPIView.as_view(), name="webserviceresource-analytics"),
    url(r'^web-services/(?P<pk>[-\w]+)/es/resources/?$', views.WebServiceResourceListAPIView.as_view(), name="webserviceresource-list"),
    url(r'^web-services/(?P<pk>[-\w]+)/es/http-screenshots/?$', views.WebServiceScreenshotListAPIView.as_view(), name="webservicescreenshot-list"),
    url(r'^web-services/(?P<pk>[-\w]+)/?$', views.WebServiceReportDetailAPIView.as_view(), name="webservice-detail"),

    # SSL Support URLs

    url(r'^ssl-support/(?P<pk>[-\w]+)/related-services/?$', views.NetworkServiceSslSupportRelatedAPIView.as_view(), name="sslsupportrelation-list"),
    url(r'^ssl-support/(?P<pk>[-\w]+)/?$', views.SslSupportReportDetailAPIView.as_view(), name="sslsupport-detail"),

    # Pre-authentication URLs

    url(r'^api-token-auth/?$', views.WsObtainAuthToken.as_view()),
    url(r'^api-check-token-auth/?$', views.WsCheckAuthTokenStatus.as_view()),
    url(r'^verify-email/?$', views.VerifyEmailView.as_view()),
    url(r'^forgot-password/?$', views.ForgotPasswordView.as_view()),
    url(r'^verify-forgot-password/?$', views.VerifyForgotPasswordView.as_view()),
    url(r'^log-out/?$', views.LogoutView.as_view()),
    url(r'^setup-account/?$', views.SetupAccountView.as_view()),
    url(r'^users/?$', views.UserCreateView.as_view()),

    url('^docs/?$', views.SwaggerSchemaView.as_view(), name="swagger-detail"),

    # Admin URLs

    url(r'^admin/manage-users/?$', views.AdminManageUsersView.as_view()),
    url(r'^admin/manage-users/enable-disable/?$', views.AdminManageUsersEnableDisableView.as_view()),
    url(r'^admin/manage-users/delete-user/?$', views.AdminManageUsersDeleteUserView.as_view()),
    url(r'^admin/manage-users/resend-verification-email/?$', views.AdminManageUsersResendVerificationEmailView.as_view()),
    url(r'^admin/scan-configs/default/?$', views.AdminDefaultScanConfigListCreateView.as_view(), name="admindefaultscanconfig-list"),

    # Network URLs

    url(r'^networks/(?P<pk>[-\w]+)/?$', views.NetworkDetailView.as_view(), name="network-detail"),
    url(r'^networks/?$', views.NetworkListView.as_view(), name="network-list"),

    # Domain Name URLs

    url(r'^domain-names/(?P<pk>[-\w]+)/es/report/?$', views.DomainNameReportDetailAPIView.as_view(), name="domainreport-detail"),
    url(r'^domain-names/(?P<pk>[-\w]+)/?$', views.DomainNameDetailView.as_view(), name="domain-detail"),
    url(r'^domain-names/?$', views.DomainNameListView.as_view(), name="domain-list"),

    # Scan Config URLs

    url(r'^dns-record-types/(?P<pk>[-\w]+)/?$', views.DnsRecordTypeDetailView.as_view(), name="dnsrecordtype-detail"),
    url(r'^dns-record-types/?$', views.DnsRecordTypeListView.as_view(), name="dnsrecordtype-list"),
    url(r'^scan-ports/(?P<pk>[-\w]+)/?$', views.ScanPortDetailView.as_view(), name="scanport-detail"),
    url(r'^scan-ports/?$', views.ScanPortListView.as_view(), name="scanport-list"),
    url(r'^scan-configs/default/?$', views.DefaultScanConfigListView.as_view(), name="defaultscanconfig-list"),
    url(r'^scan-configs/(?P<pk>[-\w]+)/is-valid/?$', views.check_scan_config_validity, name="scanconfig-check-validity"),
    url(r'^scan-configs/(?P<pk>[-\w]+)/dns-record-types/?$', views.DnsRecordTypesByScanConfigView.as_view(), name="scanconfigdnsrecordtypes-list"),
    url(r'^scan-configs/(?P<pk>[-\w]+)/scan-ports/?$', views.ScanPortsByScanConfigView.as_view(), name="scanconfigscanports-list"),
    url(r'^scan-configs/(?P<pk>[-\w]+)/?$', views.ScanConfigDetailView.as_view(), name="scan-config-detail"),
    url(r'^scan-configs/?$', views.ScanConfigListView.as_view(), name="scan-config-list"),

    # Account URLs

    url(r'^account/change-password/?$', views.AccountChangePasswordView.as_view()),

    url(r'^sa/', include(admin.site.urls)),
]
