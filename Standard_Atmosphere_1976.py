# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 16:36:24 2016
sourcecode from http://aero.stanford.edu/stdatm.html
This is 1976 standard atmosphere up to 230,000 ft(70km)
@author: shuixin
"""

import math

def atm_compute(h,v,rl):
    h_Metric=h
    v_Metric=v
    rl_Metric=rl
    h = h_Metric*3.2808;
    v = v_Metric*3.2808;
    rl = rl_Metric*3.2808;
    TEMPSL = 518.67
    RHOSL = 0.00237689
    PRESSSL = 2116.22
    saTheta = 1.0
    saSigma = 1.0
    saDelta = 1.0
    if 167323<=h<300000:
        saTheta = 1.434843 - h/337634.0
        saSigma = math.pow(0.79899-h/606330.0,11.20114)
        saDelta = math.pow(0.838263-h/577922.0,12.20114)
    elif 154199<=h<167323:
        saTheta = 0.939268;
        saSigma = 0.00116533 * math.exp((h-154200)/-25992.0)
        saDelta = 0.00109456 * math.exp((h-154200)/-25992.0)
    elif 104987<=h<154199:
        saTheta = 0.482561 + h/337634.0;
        saSigma = math.pow(0.857003+h/190115.0, -13.20114)
        saDelta = math.pow(0.898309+h/181373.0, -12.20114)
    elif 65617<=h<104987:
        saTheta = 0.682457 + h/945374.0
        saSigma = math.pow(0.978261+h/659515.0,-35.16319)
        saDelta = math.pow(0.988626+h/652600.0,-34.16319)
    elif 36089<=h<65617:
        saTheta = 0.751865
        saSigma = 0.297076 * math.exp((36089-h)/20806.0)
        saDelta = 0.223361 * math.exp((36089-h)/20806.0)
    elif h<36089:
        saTheta = 1.0 - h/145442.0;
        saSigma = math.pow(1.0-h/145442.0, 4.255876)
        saDelta = math.pow(1.0-h/145442.0, 5.255876)
        
    tempVal = TEMPSL * saTheta
    temp=tempVal/1.8
    rhoVal = RHOSL * saSigma
    rho=rhoVal/.068521/.028317
    pVal = PRESSSL * saDelta
    p=pVal/.020885
    viscVal = 0.0226968*math.pow(tempVal,1.5)/((tempVal)+198.72)/1000000.0
    visc = viscVal/.22481/.092903
    soundVal = math.sqrt( 1.4*1716.56*(tempVal));
    sound = soundVal/3.2808
    mach = v/soundVal
    #qVal = 0.7*pVal*machVal*machVal
    reynolds = v*rl*rhoVal/viscVal
    #cfturb = 0.455/math.pow((math.log(reynolds)/math.log(10)),2.58)
    #cflam = 1.328/math.sqrt(reynolds)
    atm_info=[temp,rho,p,sound,mach,reynolds,visc]
    return atm_info
'''
atm_info=atm_compute(h,v,rl)
print "Altitude    Temp     Rho      P      a      Mach     Re     Viscous (In Metric Unit System)"
print h_Metric,atm_info[0],atm_info[1],atm_info[2],atm_info[3],atm_info[4],atm_info[5],atm_info[6]
'''