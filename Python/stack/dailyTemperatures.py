#O(n^2)
def daily_temperatures_v0(temperatures: list[int]) -> list[int]:
    result = [0] * len(temperatures)
    for day in range(len(temperatures)):
        furuture_day = day + 1
        while furuture_day < len(temperatures):
            if temperatures[day] < temperatures[furuture_day]:
                result[day] = furuture_day - day
                break
            furuture_day += 1
    return result

print(daily_temperatures_v0([73,74,75,71,69,72,76,73]))


def daily_temperatures_v1(temperatures: list[int]) -> list[int]:
    result = [0] * len(temperatures)
    stack = [] # (temp, index)
    
    for ind, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stackTemp, stackInd = stack.pop()
            result[ind] = ind - stackInd
        stack.append(temp, ind)
    return result    

print(daily_temperatures_v1([73,74,75,71,69,72,76,73]))
