
# Create your views here.
def intercepter(func):
    def pre_process(request):
#         client_addr = request.META.get('REMOTE_HOST')
#         print(client_addr)
        func_name = str(func).split(" ")[1]
        print(func_name)
        return func(request)
    return pre_process