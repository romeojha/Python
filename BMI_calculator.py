import itertools
import threading
import time
import sys

done = False
# animation


def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading your' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rsurvey completed!')


weight = input("enter your weight in Kilo Gram(KG)\n")
height = input("enter your height in meters\n")
float_height = float(height)
BMI = float(weight)/(float_height ** 2)
# animation part start
# long process here
t = threading.Thread(target=animate)
t.start()
time.sleep(2)
done = True
# animtaion part ends here
print(f"\nyour BMI is {int(BMI)}")
print(type(BMI))
if 0 <= BMI <= 18.5:
    print("you are underweight,\n please improve your protein intake\n 2 eggs each day, and light exercise every morning")
elif 18.6 <= BMI <= 25:
    print("you are normal weight,\n stay as you are ,improve your food intake (include vegetables) and exercise")
elif 25.1 <= BMI <= 30:
    print("you are overweight,\n you must know what its like to live in somalia, you need exercise and less carbohydrate")
else:
    print("you are too much, you will die of obesity\nIF YOU DONT REACT NOW")
