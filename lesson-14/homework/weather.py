from bs4 import BeautifulSoup

with open("weather.html") as file:
    soup = BeautifulSoup(file, 'html.parser')

tbody = soup.find('tbody')
contents = tbody.find_all('tr')
weather = {}

# saves parsed data into dict
for content in contents:
    sub_contents = content.find_all('td')
    weather[content.find('td').text] = {
        "temperature": sub_contents[1].text,
        "condition": sub_contents[2].text
    }


def print_out(dict):
    temps = []
    good_day = []
    for day, values in dict.items():
        print(f"\nOn {day}:\n\tTemperature: {values['temperature']}\n\tCondition: {values['condition']}")
        temps.append("".join(filter(str.isdigit, values['temperature'])))
        if values['condition'] == 'Sunny': good_day.append(day)
    
    avrg_temp = (sum(int(temp) for temp in temps)) / len(temps)
    return temps, good_day, avrg_temp

# prints the entire result
listed_func = list(print_out(weather))
print(f"\nThe highest temperature: {max(listed_func[0])}\nThe Sunny days: {", ".join(listed_func[1])}\nAverage temperature: {listed_func[2]}")
