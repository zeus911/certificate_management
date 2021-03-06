from django.contrib import admin
from .models import Domain, SSLCertContent, SubDomains, SubSyncLimit, ToEmail, CustomDomain


# Register your models here.


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'domain', 'extensive_domain', 'status', 'create_time', 'start_date', 'expire_date', 'dns', 'dns_account',
        'comment', "source_ip",
    )
    # list_display = [d.name for d in Domain._meta.get_fields()]

    search_fields = ('domain', 'dns',)


@admin.register(SSLCertContent)
class SSLCertContentAdmin(admin.ModelAdmin):
    list_display = ("id", "cert_content", "key_content", "domain")
    search_fields = ("domain__domain",)


@admin.register(SubDomains)
class SubDomainsAdmin(admin.ModelAdmin):
    list_display = (
        "id", "protocol", "sub_domain", "record_type", "record_value", "start_date", "expire_date", "comment", "domain")
    search_fields = ("sub_domain", "domain__domain",)


@admin.register(SubSyncLimit)
class SubSyncLimitAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "domain", "sync_time",)
    search_fields = ("user",)


@admin.register(ToEmail)
class ToEmailAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "domain", "custom_domain")
    search_fields = ("email", "domain__domain",)


@admin.register(CustomDomain)
class CustomDomainAdmin(admin.ModelAdmin):
    list_display = ("id", "domain", "source_ip", "start_date", "expire_date")
    search_fields = ("domain", "source_ip")
