from django import forms

SKIP_CHOICES = [
    ("", "No skip"),
    ("forward", "Skip forward moves"),
    ("backwards", "Skip backward moves"),
]


class SlabForm(forms.Form):
    width = forms.FloatField(min_value=0.01, label="Width (X axis)")
    length = forms.FloatField(min_value=0.01, label="Length (Y axis)")
    stepover = forms.FloatField(label="Stepover", initial=1.24)
    depth = forms.FloatField(min_value=0.001, label="Depth per pass", initial=0.1)
    passes = forms.IntegerField(min_value=1, max_value=50, initial=1, label="Passes")
    feed_rate = forms.FloatField(min_value=1, label="Feed rate (IPM)", initial=250)
    spindle_speed = forms.FloatField(min_value=1, label="Spindle speed (RPM)", initial=12000)
    skip_direction = forms.ChoiceField(
        choices=SKIP_CHOICES, required=False, label="Skip direction"
    )

    def clean_skip_direction(self):
        value = self.cleaned_data.get("skip_direction") or None
        if value not in {None, "forward", "backwards"}:
            raise forms.ValidationError("Invalid skip direction.")
        return value
