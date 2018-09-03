from django import forms

from . hiddenfields import Allfields


class generateHiddenFiles(forms.Form):

    fields = Allfields()

    merchantid_get = fields.getmid();

    location = "storeSite/static/keyfile/"+merchantid_get+".pem";

    emerchantid_get = fields.getemid(merchantid_get,location)
    byteSignedDataString_get = fields.getbytesigneddatastring(str(merchantid_get),location)


    byteSignedDataString = forms.CharField(widget=forms.HiddenInput(),initial=byteSignedDataString_get)
    signature = forms.CharField(widget=forms.HiddenInput(),initial=merchantid_get)
    key = forms.CharField(widget=forms.HiddenInput(),initial="")
    emerchantId = forms.CharField(widget=forms.HiddenInput(),initial=emerchantid_get)
    # currencyCode = forms.CharField(widget=forms.HiddenInput(),initial="LKR")
    merchantType = forms.CharField(widget=forms.HiddenInput(),initial=1234)
    terminalId = forms.CharField(widget=forms.HiddenInput(),initial=88888888)
    txnRefNo = forms.CharField(widget=forms.HiddenInput(),initial=456)
    # url = forms.CharField(widget=forms.HiddenInput(),initial="{{urlipg}}")

    # radio = forms.CharField(widget=forms.HiddenInput(),initial=123)