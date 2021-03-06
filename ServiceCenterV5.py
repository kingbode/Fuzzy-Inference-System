import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import pandas as pd
import ModelsV2

# reading Model data set

def _get_Models_List(_fielname):


    pd.set_option("display.max_rows", None, "display.max_columns", None)

    df = pd.read_csv(_fielname)


    _Master_Models_Description_List = []
    _Master_Actual_Models_List = []

    _model = ModelsV2._Model()
    _model_Member_Fn = ModelsV2._Model_Member_Fn_()

    _model_Member_Fn_List = []

    parsing_ac = False


    for i in range(df.shape[0]):

        for j in range(df.shape[1]):
            # print(df.values[i][j])
            if('str' in str(type(df.values[i][j]))):
                if((df.values[i][j]).lower() == 'a' or (df.values[i][j]).lower() == 'c'):
                    if(_model.A_or_C == None):
                        _model.A_or_C = (df.values[i][j]).lower()
                        parsing_ac = True
                    else:
                        if(len(_model_Member_Fn_List) != 0):
                            _model._Model_Member_Fn_List = _model_Member_Fn_List.copy()
                            # _model_Member_Fn_List.clear()


                        _Master_Models_Description_List.append(_model)

                        _model_Member_Fn_List.clear()
                        _model = ModelsV2._Model()

                        _model.A_or_C = (df.values[i][j]).lower()
                        parsing_ac = True


                elif((df.values[i][j]).lower() == 'ftria' or (df.values[i][j]).lower() == 'ftrap'):
                    _model_Member_Fn.Tri_or_Trap = (df.values[i][j]).lower()
                    parsing_ac = False


            if(parsing_ac):
                if(j==1):
                    _model._Model_Label = df.values[i][j]
            else:
                if (j == 1):
                    _model_Member_Fn._Model_Member_Fn_Label = df.values[i][j]

            if (parsing_ac):
                if (j == 2):
                    _model._Model_Range1 = df.values[i][j]
            else:
                if (j == 2):
                    _model_Member_Fn._Model_Member_Fn_Label_Range1 = df.values[i][j]

            if (parsing_ac):
                if (j == 3):
                    _model._Model_Range2 = df.values[i][j]
            else:
                if (j == 3):
                    _model_Member_Fn._Model_Member_Fn_Label_Range2 = df.values[i][j]

            if (parsing_ac):
                if (j == 4):
                    _model._Model_Range3 = df.values[i][j]
            else:
                if (j == 4):
                    _model_Member_Fn._Model_Member_Fn_Label_Range3 = df.values[i][j]

            if (parsing_ac):
                if (j == 5):
                    _model._Model_Range4 = df.values[i][j]
                    parsing_ac = False  #completed parsing a or c
            else:
                if (j == 5):
                    _model_Member_Fn._Model_Member_Fn_Label_Range4 = df.values[i][j]

                    _model_Member_Fn_List.append(_model_Member_Fn)
                    # important to initiate the Model Member Function Object
                    _model_Member_Fn = ModelsV2._Model_Member_Fn_()

            if(i== df.shape[0]-1 and j == df.shape[1]-1):

                if (len(_model_Member_Fn_List) != 0):
                    _model._Model_Member_Fn_List = _model_Member_Fn_List.copy()
                    # _model_Member_Fn_List.clear()

                _Master_Models_Description_List.append(_model)
                _model_Member_Fn_List.clear()

    for model_ in _Master_Models_Description_List:

        '''
        now _Master_Models_List contains all the descriptions for all Model, so we need to use this description to
        build the real Fuzzy Model using ScikitFuzzy library, so _model_copy is a copy to avoid changing the description
        by overwriting it !!
        this is data driven approach to build the Models and the Rules dynamically
        '''
        _model_copy = model_

        if (model_.A_or_C == 'a'):
            model_Antecedent = ctrl.Antecedent(np.arange(model_._Model_Range1, model_._Model_Range2, model_._Model_Range3), model_._Model_Label)
            model_Antecedent.automf(len(_model_copy._Model_Member_Fn_List))
            # model_Antecedent.terms = {}
            for _label in _model_copy._Model_Member_Fn_List:
                if (_label.Tri_or_Trap == 'ftria'):
                    model_Antecedent[_label._Model_Member_Fn_Label] = fuzz.trimf(model_Antecedent.universe,
                                                                                      [_label._Model_Member_Fn_Label_Range1,
                                                                                       _label._Model_Member_Fn_Label_Range2,
                                                                                       _label._Model_Member_Fn_Label_Range3])
                elif (_label.Tri_or_Trap == 'ftrap'):
                    model_Antecedent[_label._Model_Member_Fn_Label] = fuzz.trapmf(model_Antecedent.universe, [
                        _label._Model_Member_Fn_Label_Range1, _label._Model_Member_Fn_Label_Range2,
                        _label._Model_Member_Fn_Label_Range3, _label._Model_Member_Fn_Label_Range4])

            _Master_Actual_Models_List.append(model_Antecedent)

        elif (model_.A_or_C == 'c'):
            model_Consequent = ctrl.Consequent(np.arange(model_._Model_Range1, model_._Model_Range2, model_._Model_Range3), model_._Model_Label)
            model_Consequent.automf(len(_model_copy._Model_Member_Fn_List))

            # model_Consequent.terms = {}
            for _label in _model_copy._Model_Member_Fn_List:
                if (_label.Tri_or_Trap == 'ftria'):
                    model_Consequent[_label._Model_Member_Fn_Label] = fuzz.trimf(model_Consequent.universe,
                                                                                      [_label._Model_Member_Fn_Label_Range1,
                                                                                       _label._Model_Member_Fn_Label_Range2,
                                                                                       _label._Model_Member_Fn_Label_Range3])
                elif (_label.Tri_or_Trap == 'ftrap'):
                    model_Consequent[_label._Model_Member_Fn_Label] = fuzz.trapmf(model_Consequent.universe,
                                                                                       [
                                                                                           _label._Model_Member_Fn_Label_Range1,
                                                                                           _label._Model_Member_Fn_Label_Range2,
                                                                                           _label._Model_Member_Fn_Label_Range3,
                                                                                           _label._Model_Member_Fn_Label_Range4])
            _Master_Actual_Models_List.append(model_Consequent)


    return _Master_Actual_Models_List

def _get_Rules_List_Description(_fielname):

    pd.set_option("display.max_rows", None, "display.max_columns", None)

    df = pd.read_csv(_fielname)

    _Master_Rules_List = []

    _rule_dict = {}
    _tmp_rule_dict = {}
    _value_dict = {}

    for i in range(df.shape[0]):

        for j in range(1, df.shape[1]):

            _rule_dict[df.columns[j]] = df.values[i][j]


        _Master_Rules_List.append(_rule_dict.copy())
        print(_rule_dict)
        _rule_dict.clear()

    return _Master_Rules_List


def get_Actual_Rules(Rules_List_Description_List,Models_List):

    _Master_Rules_List =[]

    for rule_ in Rules_List_Description_List:

        # ================================================
        # Building Rule method #1
        # ================================================
        _rule_inputs_index_list = [x for x in range(len(list(rule_.values())[:-1]))]

        _rule_inputs_list = [Models_List[x].terms[y] for x, y in
                             zip(_rule_inputs_index_list, list(rule_.values())[:-1])]

        dd = _rule_inputs_list[0]

        print(dd)

        _rule_input_resultant = _rule_inputs_list[0]

        for _rule_input in _rule_inputs_list[1:]:
            _rule_input_resultant &= _rule_input

        _Consequent_Variable = Models_List[len(rule_.values()) - 1][list(rule_.values())[-1]]

        tmp_rule = ctrl.Rule(_rule_input_resultant, _Consequent_Variable)

        _Master_Rules_List.append(tmp_rule)


    return _Master_Rules_List

'''
Main App
'''
#  you can test with below two sets, where the code is general for all ..


# Actual_Models_List_ = []
# Actual_Models_List_ = _get_Models_List(r'.\Data1\ModelData.csv')
#
#
# Rules_List = []
# Rules_List = _get_Rules_List_Description(r'.\Data1\RuleData.csv')
#
# # Actual_Rules_List = [] # = get_Actual_Rules(Rules_List,Actual_Models_List_)
#
# Consequent_ctrl = ctrl.ControlSystem(get_Actual_Rules(Rules_List,Actual_Models_List_))
#
# Consequent_ctrl_ControlSystemSimulation = ctrl.ControlSystemSimulation(Consequent_ctrl)
#
# print('Hi')
#
# #===========================================================================
# #===========================================================================
# #=========================================================================== Antecedent_Consequent
#
#
# Consequent_ctrl_ControlSystemSimulation.input['Mean Delay'] = 0.54
# Consequent_ctrl_ControlSystemSimulation.input['Number of Servers'] = 0.321
# Consequent_ctrl_ControlSystemSimulation.input['Repair Utilization Factor'] = 0.71
# #
# Consequent_ctrl_ControlSystemSimulation.compute()
#
#
# print(Consequent_ctrl_ControlSystemSimulation.output['Number of Spares'])


print('Hi')


#===========================================================================



Actual_Models_List_ = []
Actual_Models_List_ = _get_Models_List(r'.\Data2\ModelDataTips.csv')


Rules_List = []
Rules_List = _get_Rules_List_Description(r'.\Data2\RuleDataTips.csv')

for rule_ in get_Actual_Rules(Rules_List,Actual_Models_List_):
    rule_.view()

# Actual_Rules_List = [] # = get_Actual_Rules(Rules_List,Actual_Models_List_)

Consequent_ctrl = ctrl.ControlSystem(get_Actual_Rules(Rules_List,Actual_Models_List_))

Consequent_ctrl_ControlSystemSimulation = ctrl.ControlSystemSimulation(Consequent_ctrl)

print('Hi')

#===========================================================================
#===========================================================================
#=========================================================================== Antecedent_Consequent


Consequent_ctrl_ControlSystemSimulation.input['quality'] = 6.5
Consequent_ctrl_ControlSystemSimulation.input['service'] = 9.8
#
Consequent_ctrl_ControlSystemSimulation.compute()


print(Consequent_ctrl_ControlSystemSimulation.output['tip'])


print('Hi')

#===========================================================================
#==========================================================================