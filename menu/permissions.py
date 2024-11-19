from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    """
    Ruxsat: Admin bo'lsa hamma amallarni bajarishi mumkin
    Oddiy foydalanuvchilar faqat o'qiy olishadi.
    """
    def has_permission(self, request, view):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return request.user.is_staff
