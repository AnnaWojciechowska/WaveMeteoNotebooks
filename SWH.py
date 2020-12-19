#!/usr/bin/env python3
#Anna Wojciechowska,
#Tangstad, Lofoten, December 2020

from statistics import stdev
from statistics import mean
from statistics import median
import statistics
import sys
import random


#my improved stdev for waves
#waves cannot be sorted!!!!
def wave_stdev(set):
    core_set = []
    print("Tralala")

#average of 1/3 of highest waves
def significant_wh(set):
    set.sort(reverse=True)
    top_waves = int(1/3 * len(set))
 #   print(top_waves)
    return mean(set[:top_waves])


set_1 = [2, 2, 2, 2, 2, 2]
set_2 = [1, 2.5, 2.5, 2.5, 2.5, 1]
set_3 = [0.5, 1.5, 4.5, 2.5, 0.5, 2.5]

swell_t1 = [set_1, set_2, set_3]


set_4 = [1, 3.5, 3.5, 3.5, 3.5, 1]
set_5 = [0.5, 2, 3, 4, 1.5, 0.5]
set_6 = [0.5, 1.5, 0.5, 2, 5, 0.5]

swell_t2 = [set_4, set_5, set_6]

swh_heights = []

waves_heights = []

for set in swell_t1:
    print(set)
    print("Mean:                     " + str(mean(set)) )
    print("Median:                   " + str(median(set)))
    print("Standard deviation:       " + str(stdev(set)))
    swh = significant_wh(set)
    print("Significiant wave height: " + str(swh))
    print()
    swh_heights.append(swh)
    for wave in set:
        waves_heights.append(wave)
print()
print()

for set in swell_t2:
    print(set)
    #print("Mean:                     " + str(mean(set)) )
    #print("Median:                   " + str(median(set)))
    print("Standard deviation:       " + str(stdev(set)))
    swh = significant_wh(set)
    print("Significiant wave height: " + str(swh))
    swh_heights.append(swh)
    for wave in set:
        waves_heights.append(wave)


print(waves_heights)
print(swh_heights)
swh_of_means = significant_wh(swh_heights)
print("Siginificant wave height counted on swh: ")
print(swh_of_means)
print(mean(swh_heights))
swh_of_waves = significant_wh(waves_heights)
print("Siginificant wave height counted on waves: ")
print(swh_of_waves)
print(mean(waves_heights))
