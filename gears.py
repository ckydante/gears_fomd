import math as trig
import time

class gear_parameters:
    def __init__ (self,z1,z2,u ,module = None):
        self.z1 = z1
        self.z2 = z2
        self.u = u
        self.module = module




gear_data_input = open("gears_entry_parameters.txt" , "w")
gear_data_output = open("gears_calculated.txt", "w")
print ("Input your z1, beta, and atw")
z1 = int(input ("Enter z1: "))
beta = int(input ("Enter beta: "))
a_tw = int(input("Enter a_tw: "))

gear_data_input.write("z1: {} \nbeta: {} \na_tw: {}".format(z1,beta,a_tw))

def calc_alfa_t(z1, beta):
    a_n = trig.radians(20)
    beta = trig.radians(beta)
    tan_alfa_t = trig.tan(a_n)/trig.cos(beta)
    alfa_t_radians = trig.atan(tan_alfa_t)
    return alfa_t_radians


def a_t_min_max (a_tw, alfa_t_radians):
    alfa_t_max = trig.radians(25)
    alfa_t_min = trig.radians(22)
    a_t_min = (a_tw*trig.cos(alfa_t_max)/trig.cos(alfa_t_radians))
    a_t_max = (a_tw*trig.cos(alfa_t_min)/trig.cos(alfa_t_radians))
    return a_t_max, a_t_min



def module_min_max (transmission_ratio, max_distance, min_distance, teeth1, teeth2, beta):
    possible_modules = [1, 1.25, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10, 1.125, 1.375, 1.75, 2.25, 2.75, 3.5, 4.5, 5.5, 7.5, 9]
    beta = trig.radians(beta)
   
    module_min = ((2*min_distance*trig.cos(beta))/(teeth1*(1+transmission_ratio)))
    module_max = ((2*max_distance*trig.cos(beta))/(teeth1*(1+transmission_ratio)))
    
    for module in possible_modules:
        if module_min <= module and module_max >= module:  
            gear_data_output.write("z1: {}, z2: {}, transmission_ratio: {}, module: {}\n".format(teeth1,int(teeth2),transmission_ratio,module))


alfa_t_radians = calc_alfa_t(z1, int(beta))
a_t_min_max(int(a_tw), alfa_t_radians)
max_distance_module, min_distance_module = a_t_min_max(int(a_tw), alfa_t_radians)




u_h = float(input("Enter your theoretical gear transmission ratio: "))
u_ba = float(input("Enter your real belt transmission ratio: "))


theoretical_trans_ratio = float(input("Enter your theoretical overall transmission ratio: "))
z2_start = z1*u_h
z2_current = z2_start
z2_current_minus = z2_start

real_trans_ratio = (z2_current*u_ba)/z1

error = (real_trans_ratio-theoretical_trans_ratio)/theoretical_trans_ratio
error2 = (real_trans_ratio-theoretical_trans_ratio)/theoretical_trans_ratio





while z2_current<300000:
    real_trans_ratio = (z2_current*u_ba)/z1
    gear_trans_ratio = z2_current/z1
    error = (real_trans_ratio-theoretical_trans_ratio)/theoretical_trans_ratio
    if abs(error)<= 0.04:
        module_min_max(gear_trans_ratio, max_distance_module, min_distance_module, z1, z2_current, beta)
    z2_current += 1

while z2_current_minus>0:
    real_trans_ratio = (z2_current_minus*u_ba)/z1
    gear_trans_ratio = z2_current_minus/z1
    error2 = (real_trans_ratio-theoretical_trans_ratio)/theoretical_trans_ratio
    if abs(error2) <= 0.04:
        module_min_max(gear_trans_ratio, max_distance_module, min_distance_module, z1, z2_current_minus, beta)
    z2_current_minus -= 1









    
    

    

