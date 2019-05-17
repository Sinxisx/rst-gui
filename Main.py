# ##### Program untuk desain BOILER dengan bahan bakar minyak

import math

##INPUT PARAMETER FLUIDA (STEP 1)
def parameterfluida():
    print(' ------Efficiency for an oil fired boiler--------')
    print(' Masukan persentase ultimate analysis ')
    C  = float(input(' Carbon = '))
    H2  = float(input(' Hidrogen = '))
    N2  = float(input(' Nitrogen = '))
    O2  = float(input(' Oksigen = '))
    S  = float(input(' Sulphur = '))
    M  = float(input(' Moisture = '))
    GCVFUEL  = float(input(' GCV of fuel (kCal/kg)= '))
    FFR  = float(input(' Fuel firing rate (kg/hr) = '))
    Ts_B  = float(input(' Surface Temperature of Boiler (derajat C) = '))
    As_B  = float(input(' Surface area of boiler (m^2) = '))
    H  = float(input(' Humidity (kg/kg of dry air) = '))
    WS  = float(input(' Wind speed (m/s) = '))

    print(' Masukan persentase flue gas analysis ')
    Tf  = float(input(' Flue gas temperature (derajat C) = '))
    Ta  = float(input(' Ambient temperature (derajat C) = '))
    CO2  = float(input(' C02 % in flue gas by volume = '))
    O2  = float(input(' 02 % in flue gas by volume = '))

    print(' Masukan Konstanta ')
    Cp1 = float(input(' specific heat of flue gas (kCal/kg derajat C) = '))
    Cp2 = float(input(' specific heat of superheated steam (kCal/kg derajat C) = '))
                   
    
    airteori = ((11.6*C)+(34.8*(H2-(O2/8)))+(4.35*S))/100
    EA = (O2*100)/(21-O2)
    AAS = (1+(EA/100))*airteori
    MDFG = ((C/100)*44/12)+((S/100)*64/32)+(N2/100)+((O2/100)*23/100)+(AAS*77/100)
    
    L1 = ((MDFG*Cp1*abs(Tf-Ta))*100)/GCVFUEL
    L2 = ((9*(H2/100)*(584+(Cp2*abs(Tf-Ta))))*100)/GCVFUEL
    L3 = (((M/100)*(584+(Cp2*abs(Tf-Ta))))*100)/GCVFUEL
    L4 = (AAS*H*Cp2*abs(Tf-Ta)*100)/GCVFUEL
    radconv = (0.548*((((Ts_B/55.55)**4)-((Ta/55.55)**4)))+(1.957*((Ts_B-Ta)**1.25)*(math.sqrt(((1.9685*WS)+68.9)/68.9))))
    konversi = radconv*0.86
    TotRad_conv = konversi*As_B
    Rad_conv = (TotRad_conv*100)/(GCVFUEL*FFR)
    L6 = Rad_conv
    B_E = abs(100-(L1+L2+L3+L4+L6))

    print(' Theoritical air required =', airteori)
    print(' Excess air supplied =', EA)
    print(' Actual mass of air supplied/kg of fuel =', AAS)
    print(' Mass of dry flue gas =', MDFG)
    print(' Dry flue gas L1 =', L1)
    print(' Loss due to hydrogen in fuel, L2 =', L2)
    print(' loss due to moisture in fuel, L3 =', L3)
    print(' Loss due to moisture in air, L4 =', L4)
    print(' Surface heat losses, L6 =', L6)
    print(' Boiler Efficiency =',B_E)

parameterfluida()
