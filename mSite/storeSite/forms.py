from django import forms

from . hiddenfields import Allfields


class generateHiddenFiles(forms.Form):

    f = Allfields()

    merchantid_get = f.getmid


    byteSignedDataString = forms.CharField(widget=forms.HiddenInput(),initial=merchantid_get)
    signature = forms.CharField(widget=forms.HiddenInput(),initial=123)
    key = forms.CharField(widget=forms.HiddenInput(),initial=123)
    emerchantId = forms.CharField(widget=forms.HiddenInput(),initial=123)
    currencyCode = forms.CharField(widget=forms.HiddenInput(),initial=123)
    merchantType = forms.CharField(widget=forms.HiddenInput(),initial=123)
    terminalId = forms.CharField(widget=forms.HiddenInput(),initial=123)
    txnRefNo = forms.CharField(widget=forms.HiddenInput(),initial=123)
    url = forms.CharField(widget=forms.HiddenInput(),initial=123)

    # radio = forms.CharField(widget=forms.HiddenInput(),initial=123)