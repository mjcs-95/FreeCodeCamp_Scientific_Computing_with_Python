def add_time(start, duration, starting_day=""):
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    timer = duration.split(":")
    start_timer = start.replace(":"," ").split()    
    final_hour = 0
    final_minute = int(timer[1])+ int(start_timer[1])
    if(final_minute > 60):
        final_hour += int(final_minute/60)
        final_minute = final_minute % 60
    final_hour += int(timer[0]) +int(start_timer[0])
    if start_timer[2] == "PM":
        final_hour += 12    
    n = int(final_hour / 24) 
    final_hour = final_hour % 24
    if final_hour < 12:
        pm = " AM"
    else:
        pm = " PM"
    final_hour = final_hour % 12
    if final_hour == 0:
        final_hour = 12    
    new_time = str(final_hour)+ ":"+str(final_minute).rjust(2,'0') + pm;    
    if starting_day:
        for i in range(len(days)):
            if(str.upper(starting_day) == str.upper(days[i])):
                new_time += (", " + days[ (i+n) % len(days)])
                break
    if 1 <= n:
        if n == 1:
            new_time += " (next day)"
        else:
            new_time += " (" + str(n) + " days later)"
    return new_time
