from .box import Box
def box(request):
    return {'box': Box(request)}