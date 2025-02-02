from django import forms


class BookingForm(forms.Form):
    check_in_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control'}
        ),
        label='Check-in',
        required=True
    )
    check_out_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        ),
        label='Check-out',
        required=True
    )
    adults = forms.IntegerField(
        min_value=1,
        max_value=5,
        label="Adults (18+)",
        required=True,
        widget=forms.NumberInput(attrs={
            'onchange': 'updateGuestCount()'
        })
    )
    children = forms.IntegerField(
        min_value=0,
        max_value=5,
        label="Children (5+)",
        required=False,
        widget=forms.NumberInput(attrs={
            'onchange': 'updateGuestCount()'
        })
    )
    infants = forms.IntegerField(
        min_value=0,
        max_value=5,
        label="Infants (0-5)",
        required=False,
        widget=forms.NumberInput(attrs={
            'onchange': 'updateGuestCount()'
        })
    )

    class Meta:
        fields = [
            'check_in_date',
            'check_out_date',
            'adults',
            'children',
            'infants'
        ]
