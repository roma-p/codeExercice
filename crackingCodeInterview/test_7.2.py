# -*- coding: utf-8 -*-

from ex_7_2 import *

import unittest

class Test(unittest.TestCase):

    def test_basic(self):

        titi        = Respondents("titi")
        luuul       = Respondents("luuul")
        bidule      = Respondents("bidule")
        didier      = Respondents("didier")
        corenting   = Respondents("corenting")
        constructor = Respondents("constructor")

        fabieng  = Manager("fabieng")
        rerquing = Manager("rerquing")

        BerndardArnault = Director("BerndardArnault")

        callCenter = CallCenter()

        callCenter.addRespondents(
            titi, luuul,
            bidule, didier,
            corenting, constructor)
        callCenter.addManagers(fabieng, rerquing)
        callCenter.director = BerndardArnault

        callCenter.createTeam(fabieng, titi, luuul, bidule, didier)
        callCenter.createTeam(rerquing, corenting, constructor)

        callCenter.dispatchNewCall()
        callCenter.dispatchNewCall()
        callCenter.dispatchNewCall()
        callCenter.dispatchNewCall()
        callCenter.dispatchNewCall()

if __name__ == '__main__':
    unittest.main()