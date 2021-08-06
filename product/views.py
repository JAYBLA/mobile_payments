from django.shortcuts import render

def product_add(request):
    template_name = 'main/home.html'

    if request.POST:
        form=ProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user_id=request.user.id
            obj.save
        return redirect('/')
    else:
        form=ProductForm()
        context = {
            'form':form,
        }
    return render(request, template_name, context)

