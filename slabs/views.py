from django.shortcuts import render

from .forms import SlabForm
from .utils import generate_gcode


def home(request):
    gcode_output = None
    if request.method == "POST":
        form = SlabForm(request.POST)
        if form.is_valid():
            gcode_output = generate_gcode(**form.cleaned_data)
    else:
        form = SlabForm()

    return render(
        request,
        "slabs/form.html",
        {
            "form": form,
            "gcode_output": gcode_output,
        },
    )

