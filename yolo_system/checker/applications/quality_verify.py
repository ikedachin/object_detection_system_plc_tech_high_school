from typing import Dict, Any

##################################################################
###################### 判定ロジックライブラリ ######################
##################################################################

def quality_verify_common(result_dict):
    if len(result_dict) == 0:
        return False
    else:
        return True



def quality_verify_thr17(result_dict):

    if len(result_dict) == 1:
        key, value = list(result_dict.items())[0]
        if key == "s":
            if value == 8:
                return True
            else:
                return False
        else:
            if value == 9:
                return True
            else:
                return False
    else:
        return False

def get_results_sum_multiple(result_dict):
    print(f'Calculating sum and multiple for result_dict: {result_dict}')
    sum_result, multiple_results = 0, 1
    for key, value in result_dict.items():
        if not isinstance(value, int):
            raise ValueError(f"Value for key '{key}' is not an integer: {value}")
        else:
            dice_eyes = int(key.split('_')[1])
            sum_result += dice_eyes * int(value)
            multiple_results *= int(dice_eyes) ** int(value)
    return sum_result, multiple_results
