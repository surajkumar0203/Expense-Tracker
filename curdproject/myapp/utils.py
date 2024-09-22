from django.shortcuts import redirect

def redirect_if_not_authenticated(redirect_url='/home/'):
    def decorater(func):
        def wrapper(request):
            if request.user.is_authenticated:
                return redirect(redirect_url)
            return func(request)
        return wrapper
    return decorater




