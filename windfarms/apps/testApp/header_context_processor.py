from datetime import datetime


def header_cp(request):
    ctx = {"now": datetime.now()}
    return ctx
