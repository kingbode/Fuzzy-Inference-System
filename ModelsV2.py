import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pandas as pd
from skfuzzy.control.term import _MembershipValueAccessor

import ModelsV2

class _Model(object):


    def __init__(self, A_or_C=None, _Model_Label=None, _Model_Range1=None, _Model_Range2=None,
                 _Model_Range3=None, _Model_Member_Fn_List=None,
                 _Model_Ctrl=None, _Model_Fuzz_Dict=None):

        self.A_or_C = A_or_C
        self._Model_Label = _Model_Label

        self._Model_Range1 = _Model_Range1
        self._Model_Range2 = _Model_Range2
        self._Model_Range3 = _Model_Range3

        self._Model_Member_Fn_List = _Model_Member_Fn_List

        self._Model_Ctrl = _Model_Ctrl
        self._Model_Fuzz_Dict = _Model_Fuzz_Dict



class _Model_Member_Fn_(object):

    def __init__(self, Tri_or_Trap=None, _Model_Member_Fn_Label=None, _Model_Member_Fn_Label_Range1=None, _Model_Member_Fn_Label_Range2=None,
                 _Model_Member_Fn_Label_Range3=None, _Model_Member_Fn_Label_Range4=None,
                 _Model_Member_Fn_List=None):

        self.Tri_or_Trap = Tri_or_Trap
        self._Model_Member_Fn_Label = _Model_Member_Fn_Label

        self._Model_Member_Fn_Label_Range1 = _Model_Member_Fn_Label_Range1
        self._Model_Member_Fn_Label_Range2 = _Model_Member_Fn_Label_Range2
        self._Model_Member_Fn_Label_Range3 = _Model_Member_Fn_Label_Range3
        self._Model_Member_Fn_Label_Range4 = _Model_Member_Fn_Label_Range4


