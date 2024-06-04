def role(request):
    return {'role': request.session['role']}
