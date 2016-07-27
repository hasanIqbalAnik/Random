from __future__ import division
import math

ctr = 0
ita = .9
w1 = .5
w2 = .5

i1 = .1
target = .9

while True:
    ctr += 1
    neth = i1 * w1
    outh = 1 / (1 + math.exp(-neth))

    neto = w2 * outh
    outo = 1 / (1 + math.exp(-neto))

    e = .5 * math.pow((target - outo), 2)
    print 'error now is: ', e
    if e < .00005:
        print '*' * 100
        print 'target is: ', target
        print 'output is now: ', outo
        print 'w1 and w2 is: ', w1, ',', w2
        print 'number of iterations: ', ctr
        break
    # update w2
    de_by_douto = (-1) * (target - outo)
    douto_by_dneto = outo * (1 - outo)
    dneto_by_dw2 = outh

    de_by_dw2 = de_by_douto * douto_by_dneto * dneto_by_dw2

    # update w1
    # de_by_dw1 = de_by_douto * douto_by_dneto * dneto_by_douth * douth_by_dneth * dneth_by_dw1
    dneto_by_douth = w2
    de_by_outh = de_by_douto * douto_by_dneto * dneto_by_douth
    douth_by_dneth = outh * (1 - outh)
    dneth_by_dw1 = i1

    de_by_dw1 = de_by_outh * douth_by_dneth * dneth_by_dw1

    # updated w1 and w2
    w1 = w1 - (ita * de_by_dw1)
    w2 = w2 - (ita * de_by_dw2)
