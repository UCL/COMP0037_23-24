#!/usr/bin/env python3

'''
Created on 25 Jan 2022

@author: ucacsjj
'''

from common.airport_map_drawer import AirportMapDrawer
from common.scenarios import all_scenarios

if __name__ == '__main__':

    for scenario in all_scenarios():
        airport, drawer_height = scenario()
        airport_map_drawer = AirportMapDrawer(airport, drawer_height)
    
        airport_map_drawer.update()
    
        airport_map_drawer.wait_for_key_press()

    
