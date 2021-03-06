# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

from .base import WsRetrieveUpdateDestroyAPIView, WsListAPIView, WsRetrieveDestroyAPIView
from rest.models import DomainName
from rest.serializers import DomainNameSerializer
import rest.serializers
import rest.models


class DomainNameQuerysetMixin(object):
    """
    This is a class that provides queryset retrieval methods for querying domain name objects.
    """

    serializer_class = DomainNameSerializer

    def _get_su_queryset(self):
        return DomainName.objects.all()

    def _get_user_queryset(self):
        return DomainName.objects\
            .filter(organization__auth_groups__users=self.request.user, organization__auth_groups__name="org_read")\
            .all()

    def perform_destroy(self, instance):
        if not self.request.user.is_superuser:
            self.__verify_write_permissions()
        return super(DomainNameQuerysetMixin, self).perform_destroy(instance)

    def perform_update(self, serializer):
        if not self.request.user.is_superuser:
            self.__verify_write_permissions()
        return super(DomainNameQuerysetMixin, self).perform_update(serializer)

    def __verify_write_permissions(self):
        """
        Verify that the requesting User has write permissions to the queried organization.
        :return: None
        """
        network = get_object_or_404(DomainName, pk=self.kwargs["pk"])
        if not network.organization.can_user_write(self.request.user):
            raise PermissionDenied("You do not have permission to modify that network.")


class DomainNameDetailView(DomainNameQuerysetMixin, WsRetrieveUpdateDestroyAPIView):
    """
    get:
    Get a specific domain name.

    put:
    Update a specific domain name.

    patch:
    Update a specific domain name.

    delete:
    Delete a specific domain name.
    """


class DomainNameListView(DomainNameQuerysetMixin, WsListAPIView):
    """
    get:
    Get all domain names.
    """


class DnsRecordTypeQuerysetMixin(object):
    """
    This is a mixin class that provides the queryset retrieval methods for querying DnsRecordType objects.
    """

    serializer_class = rest.serializers.DnsRecordTypeRelatedSerializer

    def _get_su_queryset(self):
        return rest.models.DnsRecordType.objects.all()

    def _get_user_queryset(self):
        return rest.models.DnsRecordType.objects\
            .filter(
                Q(scan_config__user=self.request.user) |
                Q(scan_config__is_default=True) |
                Q(
                    scan_config__organization__auth_groups__users=self.request.user,
                    scan_config__organization__auth_groups__name="org_read",
                )
            ).all()


class DnsRecordTypeListView(DnsRecordTypeQuerysetMixin, WsListAPIView):
    """
    get:
    Get all DnsRecordType objects associated with the requesting user.
    """


class DnsRecordTypeDetailView(DnsRecordTypeQuerysetMixin, WsRetrieveDestroyAPIView):
    """
    get:
    Get a specific DnsRecordType.

    delete:
    Delete a specific DnsRecordType.
    """

    def perform_destroy(self, instance):
        if instance.scan_config.is_default and not self.request.user.is_superuser:
            raise PermissionDenied()
        elif hasattr(instance.scan_config, "organization"):
            if self.request.user not in instance.scan_config.organization.admin_group.users.all() \
                    and not self.request.user.is_superuser:
                raise PermissionDenied(
                    "You do not have sufficient permissions for the related organization to delete this object."
                )
        elif not instance.scan_config.can_be_modified:
            raise PermissionDenied("The related scanning configuration cannot be modified at this time.")
        else:
            return super(DnsRecordTypeQuerysetMixin, self).perform_destroy(instance)