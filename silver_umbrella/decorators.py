from django.http import HttpResponse
from django.shortcuts import redirect

# def view_archived(sender=None, retrieve_archived =False):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             _model = sender.objects.get(owner=request.user.id).filter(is_archived=retrieve_archived)

#             if user_is_authorized_party:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse("You're not authorized to view this page")

#         return wrapper_func

#     return decorator


def authorized_party(sender=None):
    """
    @authorized_party(sender=User)
    """

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            patient = sender.objects.get(owner=patient_id)
            user_is_authorized_party = len(
                [
                    user.username
                    for user in patient.authorized_party.all()
                    if user.username == request.user.username
                ]
            )
            if user_is_authorized_party:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You're not authorized to view this page")

        return wrapper_func

    return decorator


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("homepage")
        return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=()):
    """
    @allowed_users(allowed_roles=('admin', 'supervisor', 'lead'))
    """

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You're not authorized to view this page")

        return wrapper_func

    return decorator


def object_fields(fields=[], model=None):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            _fields = set(fields)

            # _protected_fields = {k:v for k,v in }
            return view_func(request, *args, **kwargs)

        return wrapper_func

    return decorator


#  ryan, interview process
