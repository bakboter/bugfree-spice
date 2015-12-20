"""
Dit stukje geeft relties aan tussen getallen 
het tweede stukje code geeft berkeinge weer die in het print stukje worden uit gewerkt.
"""
cars = 100 
space_in_a_car = 4
drivers = 30 
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

"""
deze print comando's worden hier onder  weer geven 
en worde de berkding hier boven uit gevoerd worden hier onder weer geven.
"""

print "there are", cars, "cars available."
print "there are only", drivers,"drivers available"
print "there will be", cars_not_driven ,"empty cars today"
print "We can transport", carpool_capacity, "people today"
print "we have", passengers, "car pool today."
print "we needed to put about", average_passengers_per_car, "in each car."
"""
1. Het verandert de staat van de out komt van de vaule

We can transport 120.0 people today.

2.  nummer 4.0 is floating point en nummer 4 is decimaal.

3. done

4.
= teken is om dinge te benomen 

5.  Unders_Score is een teken 

6. 
>>> a = 3
>>> b = 45
>>> a + b
48

Extra opdracht.

Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined

becouse he dint use the , to make it a sprtate command form the previes print command 


"""