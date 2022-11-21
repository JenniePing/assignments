import random
import matplotlib.pyplot as plt
import numpy as np

# fig5

miu = np.linspace(0.015, 0.3, 200)


def csma_aoi(lamda):
    q = []
    NAoi = []
    ele1 = pow((1 - lamda), 50) / lamda
    for i in miu:
        for tp in np.linspace(0.001, 1, 100000):  # q7取样
            c = pow((1 - lamda), 50)  # 其中一坨参数
            tag = 0
            if abs(c * pow((1 - tp), 9) / (1 - (1 - lamda) * pow((1 - tp), 9) - c * (1 - pow((1 - tp), 9))) + (
                    1 / i) - (1 / tp)) < np.exp(-4):
                q.append(tp)
                tag = 1
                break
        if tag == 0:
            q.append(0)
            print(0)
    print(len(q))

    for x, j in zip(miu, q):
        ele2 = (50 - 49 * pow((1 - j), 9)) / (pow((1 - j), 9) * x)
        print(abs((1 - lamda) / lamda + ele2 + (
                (ele1 / lamda * (2 + 49 * lamda) + 49 * (1 - 1 / x)) / (2 * (ele1 + ele2 + 49))) + 3 * 49 / 2))
        # print(ele2)
        for aoi in np.linspace(0, 4000, 100000):
            # print(aoi)
            tag = 0
            if abs(((1 - lamda) / lamda + ele2 + (
                    (ele1 / lamda * (2 + 49 * lamda) + 49 * (1 - 1 / x)) / (
                    2 * (ele1 + ele2 + 49))) + 3 * 49 / 2) - aoi) < np.exp(
                -3):
                NAoi.append(aoi)
                tag = 1
                print(aoi)
                break
        if tag == 0:
            NAoi.append(0)

    return NAoi


if __name__ == "__main__":
    NAoi_1 = csma_aoi(0.5)
    NAoi_2 = csma_aoi(0.05)
    plt.plot(miu, NAoi_1, 'darkorange', label="Simulation for λ=0.5")
    plt.plot(miu, NAoi_2, 'b--', label='Simulation for λ=0.05')
    plt.legend(loc='best')
    plt.xlabel("Conditional transmission probability μ")
    plt.ylabel("Network Aoi")
    plt.show()
