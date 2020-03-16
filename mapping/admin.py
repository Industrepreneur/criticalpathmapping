from django.contrib import admin
# from django.contrib.admin.sites import AdminSite
from django.contrib.admin import AdminSite


class SiteAdminSite(AdminSite):
    site_header = 'CPM'
    site_title = 'CPM'
    index_title = 'Site Admin'

    # def get_urls(self):
    #     self._registry.update(admin.site._registry)
    #     return super(SiteAdminSite, self).get_urls()

    def has_permission(self, request):
        user = request.user
        if user.is_authenticated() and user.is_admin:
            return True

site_admin = SiteAdminSite(name='siteadmin')


class ManagerAdminSite(AdminSite):
    site_header = 'CPM'
    site_title = 'CPM'
    index_title = 'Manager Admin'

    # def get_urls(self):
    #     self._registry.update(admin.site._registry)
    #     return super(ManagerAdminSite, self).get_urls()

manager_admin = ManagerAdminSite(name='manageradmin')
