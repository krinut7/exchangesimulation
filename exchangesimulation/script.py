import math
import random
import numpy as np
import matplotlib.pyplot as plt
from exchangesimulation import classes, constants


def calculate_rate(
    exchange_rate: float, months: int, fluctuation: classes.Fluctuation
) -> float:
    new_rate = exchange_rate + eval(
        fluctuation.formula, None, {fluctuation.variable: months}
    )
    if new_rate > constants.UPPER_LIMIT:
        return constants.UPPER_LIMIT
    if new_rate < constants.LOWER_LIMIT:
        return constants.LOWER_LIMIT
    return new_rate


def final_return(init: float, months: int):
    return init * math.pow(1 + constants.ROI, months)


def calculate_roi(fluctuation: classes.Fluctuation):
    current_rate = constants.CURRENT_RATE
    invs_ret = 0

    for months in range(constants.TOTAL_MONTHS, 0, -1):
        # current_rate = calculate_rate(
        #     current_rate, constants.TOTAL_MONTHS - months, fluctuation
        # )
        current_rate = (
            constants.LOWER_LIMIT
            + (constants.UPPER_LIMIT - constants.LOWER_LIMIT) * random.random()
        )
        invs_ret = invs_ret + final_return(constants.MONTHLY * current_rate, months)

    print(current_rate)
    total_invst = constants.MONTHLY * constants.TOTAL_MONTHS
    return_invst = invs_ret / current_rate
    total_return = return_invst - total_invst
    print(total_return)
    print(total_invst)
    roi = (total_return / total_invst) * 100
    return total_return, roi


def main():
    # linear = classes.Fluctuation("x/1000")
    # quadratic = classes.Fluctuation("(x**2)/1000")
    # random = classes.Fluctuation("random.random()")

    # linear_tot, linear_roi = calculate_roi(linear)
    # quad_tot, quad_roi = calculate_roi(quadratic)
    # rand_tot, rand_roi = calculate_roi(random)

    # print(f"Linear: {linear_tot, linear_roi}")
    # print(f"Quadratic: {quad_tot, quad_roi}")
    # print(f"Random: {rand_tot, rand_roi}")
    # # print(f"Difference: {rand_tot - rand_tot}")
    tot, roi = calculate_roi(None)
    print(tot, roi)
    # roi_list = []
    # tot_list = []
    # for _ in range(10):
    #     tot, roi = calculate_roi(None)
    #     tot_list.append(tot)
    #     roi_list.append(roi)
    #     print(roi_list)

    # plt.plot(np.array(roi_list))
    # plt.show()


if __name__ == "__main__":
    main()
