from django import forms

from . hiddenfields import Allfields


class generateHiddenFiles(forms.Form):

    f = Allfields()
    merchantid_get = f.getmid
    amount_get= f.getamout

    merchantId = forms.CharField(widget=forms.HiddenInput(),initial=merchantid_get)
    amount = forms.CharField(widget=forms.HiddenInput(),initial=amount_get)
    orderid = forms.CharField(widget=forms.HiddenInput(),initial=123)
    dateofregistry = forms.CharField(widget=forms.HiddenInput(),initial=123)
    refno = forms.CharField(widget=forms.HiddenInput(),initial=123)
    byteSignedDataString = forms.CharField(widget=forms.HiddenInput(),initial=123)
    signature = forms.CharField(widget=forms.HiddenInput(),initial=123)
    key = forms.CharField(widget=forms.HiddenInput(),initial=123)
    emerchantId = forms.CharField(widget=forms.HiddenInput(),initial=123)
    currencyCode = forms.CharField(widget=forms.HiddenInput(),initial=123)
    merchantType = forms.CharField(widget=forms.HiddenInput(),initial=123)
    terminalId = forms.CharField(widget=forms.HiddenInput(),initial=123)
    txnRefNo = forms.CharField(widget=forms.HiddenInput(),initial=123)
    url = forms.CharField(widget=forms.HiddenInput(),initial=123)

    # radio = forms.CharField(widget=forms.HiddenInput(),initial=123)