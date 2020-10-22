#!/usr/bin/python3

charge_percent = open(
        "/sys/class/power_supply/BAT0/capacity", "r").readline().strip()

charge_state = open(
        "/sys/class/power_supply/BAT0/status","r").readline().strip()

print("Battery: " + charge_percent + "%, " + charge_state)
