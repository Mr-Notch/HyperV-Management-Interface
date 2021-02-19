
from MainInterface import it_hmi_location
import random
import os

def getRandomPort():
    
    random_value = random.randint(10000,20000)
    checker=[]
    checker.append(str(random_value))
    path=it_hmi_location+"Config\\cache\\random_dice_var_statistics.txt"
    if not os.path.isfile(path):
        fd = open(path, mode="w", encoding="utf-8")
        fd.close()
        exist_switch = False
    elif os.path.isfile(path):
        exist_switch = True

    if exist_switch == False:
        with open(path,mode="w") as that:
            for line in checker:
                that.write(line)
        that.close()
    else:
        with open(path,mode="r") as this:
            new_checker = this.readlines()
            if str(random_value) in str(new_checker):
                random_value_2 = random.randint(10000, 20000)
                new_checker.append(str(random_value_2))

                returner=random_value_2
            else:
                new_checker.append(str(random_value))

                returner=random_value
            with open(path,mode="w") as fuck:
                for lines in new_checker:
                    fuck.write(lines+' ')
                fuck.close()
        this.close()
    return returner