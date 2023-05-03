import random
import pandas as pd

def chorechart(daily_chores, weekly_chores):
    
    weekday_chore_dic= {
        "Monday" : [],
        "Tuesday" : [],
        "Wednesday" : [],
        "Thursday" : [],
        "Friday":[],
    }

    weekend_chore_dic = {"Saturday": [], 
                        "Sunday": []}

    daily_list = daily_chores
    weekly_list = weekly_chores
    
    # daily_list.append(daily_chores)
    # weekly_list.append(weekly_chores)
    # print(daily_list)
# chore_dic["Person1"].append("mop")

    # print(weekday_chore_dic)

    for key in weekday_chore_dic:
        chore = random.choice(daily_list)
        daily_list.remove(chore)
        weekday_chore_dic[key].append(chore)
    for key in weekend_chore_dic:
        chore= random.choice(weekly_list)
        weekly_list.remove(chore)
        weekend_chore_dic[key].append(chore)
        
    def Merge(dict1, dict2):
        return(dict2.update(dict1))
            

    Merge(weekend_chore_dic,weekday_chore_dic)
    # print(weekday_chore_dic)
    # for day, chore in weekday_chore_dic.items():
    #     pretty = print(f'{day} {chore}')
    
    return weekday_chore_dic



weekday_chores = chorechart(daily_chores=["Trash", "Counters","Sweep Kitchen","Stove","Microwave"], weekly_chores=["Mop","Clean Fridge", "Vaccum", "Dust", "Bathroom"])

print(weekday_chores)

for day, chore in weekday_chores.items():
    print(f"{day}, {chore}")

df = pd.DataFrame(weekday_chores,index = None)
print(df)

df.to_csv("ChoreChart.csv")




