""" Binomial CRR tree COM server """
from BinomialCRROption import BinomialCRROption
import pythoncom

class BinomiaCRRCOMServer:
    _public_methods_ = ['pricer']
    _reg_progid_ = "BinomialCRRCOMServer.Pricer"
    _reg_clsid_ = pythoncom.CreateGuid()
    
    def pricer(self, S0, K, r, T, N, sigma, is_call=True, div=0., is_eu=False):
        model = BinomailCRROption(S0, K, r, T, N, {"sigma": sigma, "div": div, "is_call": is_call, "is_eu": is_eu})
        return model.price()
