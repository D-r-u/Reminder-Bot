
# Copyright [2024] [Drupad M D]

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import urllib.parse
import datetime

def check_dict(addr):
    dict = {'Netherlands Visa Application Center-Abu Dhabi Level B2 (Lower Ground), The Mall World Trade Centre, Khalifa Bin Zayed the 1st Street Abu Dhabi, UAE Abu Dhabi,UAE': 'https://maps.app.goo.gl/eaSLhy9TfGWkFKzk9?g_st=iw', 'Netherlands Visa application center- Dubai Wafi Mall, Level 2, Falcon Phase 2, Umm Hurair 2, Dubai, UAE': 'https://maps.app.goo.gl/EQa357WstGTnpvVx8?g_st=iwb', 'Germany Visa application center- Dubai Wafi Mall, Level 2, Falcon Phase 2, Umm Hurair 2, Dubai, UAE': 'https://maps.app.goo.gl/EQa357WstGTnpvVx8?g_st=iwb', 'TÃ¼rkiye Visa Application Center-Dubai WAFI Mall, Level 3, Falcon, Phase 2, UMM Hurrair2 Dubai,UAE': 'https://maps.app.goo.gl/EQa357WstGTnpvVx8?g_st=iwb', 'Belgium Visa Application Center-Abu Dhabi Level B2 (Lower Ground), The Mall World Trade Centre, Khalifa Bin Zayed the 1st Street Abu Dhabi,UAE': 'https://maps.app.goo.gl/eaSLhy9TfGWkFKzk9?g_st=iw', 'BLS Spain visa application centre, Dubai I-Rise, Barsha Heights, Dubai, United Arab Emirates': 'https://g.co/kgs/jEoBgm', 'Switzerland Visa Application Centre- Abu Dhabi Level B2 (Lower Ground), The Mall World Trade Centre, Khalifa Bin Zayed the 1st Street Abu Dhabi Abu Dhabi, UAE': 'https://maps.app.goo.gl/eaSLhy9TfGWkFKzk9?g_st=iw', 'FRANCE VISA APPLICATION CENTER, VFS GLOBAL ABUDHABI, The Mall World Trade Centre, Khalifa Bin Zayed the 1st Street Abu Dhabi Abu Dhabi, UAE': 'https://maps.app.goo.gl/eaSLhy9TfGWkFKzk9?g_st=iw', 'Cyprus Visa application center- Dubai Wafi Mall, Level 3, Falcon Phase 2, Umm Hurair 2, Dubai, UAE': 'https://maps.app.goo.gl/EQa357WstGTnpvVx8?g_st=iwb', 'Switzerland Visa application center- Dubai Wafi Mall, Level 2, Falcon Phase 2, Umm Hurair 2, Dubai, UAE': 'https://maps.app.goo.gl/EQa357WstGTnpvVx8?g_st=iwb', 'Hungary Visa Application Centre- Abu Dhabi Level B2 (Lower Ground), The Mall World Trade Centre, Khalifa Bin Zayed the 1st Street Abu Dhabi Abu Dhabi, UAE': 'https://maps.app.goo.gl/eaSLhy9TfGWkFKzk9?g_st=iw', 'BLS Spain visa application centre, Abu Dhabi 1311, Tamouh Tower; 13th Floor, Marina Square, Al Reem Island, Abu Dhabi, UAE': 'https://maps.app.goo.gl/7K6xmGMtEaiUowMN9', 'Italy Visa Application Center ,Dubai Dubai International Financial Center The Gate Avenue, Level 1, Unit # 166 & 168 Dubai,UAE': 'https://g.co/kgs/nWBGWr', 'Italy Visa Application Center Abu Dhabi, United Arab Emirates Nation Towers Mall, 1st Floor; # F24; 1st Street, Al Bateen, Abu Dhabi, UAE': 'https://maps.app.goo.gl/4vwyr1DEdg9vsLJJ8', 'Greece Visa application center- Dubai Wafi Mall, Level 2, Falcon Phase 2, Umm Hurair 2, Dubai, UAE': 'https://maps.app.goo.gl/EQa357WstGTnpvVx8?g_st=iwb', 'HUNGARY Visa application center- Dubai Wafi Mall, Level 2, Falcon Phase 2, Umm Hurair 2, Dubai, UAE': 'https://maps.app.goo.gl/EQa357WstGTnpvVx8?g_st=iwb', 'GERMANY VISA APPLICATION CENTER, VFS GLOBAL ABU DHABI': 'https://maps.app.goo.gl/syaoq8QTrecqcMcz7', 'Greece Visa Application Centre- Abu Dhabi Level B2 (Lower Ground), The Mall World Trade Centre, Khalifa Bin Zayed the 1st Street Abu Dhabi Abu Dhabi, UAE': 'https://maps.app.goo.gl/eaSLhy9TfGWkFKzk9?g_st=iw', 'Denmark Visa Application Center-Dubai WAFI Mall, Level 2, Falcon, Phase 2, Umm Hurair2 Dubai, UAE, 114100': 'https://maps.app.goo.gl/EQa357WstGTnpvVx8?g_st=iwb', 'South Africa Visa Application Center-Dubai WAFI Mall, Level 3, Falcon Phase 2, Umm Hurair2, Dubai, UAE, 114100': 'https://maps.app.goo.gl/EQa357WstGTnpvVx8?g_st=iwb'}
    if addr in dict.keys():
        return dict[addr]
    else:
        return 0


def generate_msg(time,address,city,date):
    greet = ""
    center = address[:address.find(",")]
    center = center.upper()
    city = city.upper()
    time = time[:time.rfind(":")]
    day = date.strftime("%A")
    day = day.upper()
    date = date.strftime("%d-%m-%Y")

    check = address.replace("\n"," ")

    ret = check_dict(check.strip())
    if day == "MONDAY": 
        greet = "Afternoon" 
    else: 
        greet = "Evening"

    if ret == 0:
        # finding the google map location and link
        tail = address
        tail = tail[tail.find(",")+1:].strip()

        base = "https://www.google.com/maps/search/?api=1&query="
        url = base + urllib.parse.quote(tail)
    else:
        url = ret

    str = f"""Good  {greet}!

Reminder from The Visa Guy, in regards to your appointment for {day}({date}). 

The time is at {time} AM  at the {center}, {city}

You may reach there 15 minutes prior to your appointment.

We hope you're ready with the required documents (details have been sent through email) for your appointment. 

Make sure you dont forget them, Have a great day ahead 😊

Location :
{address}

{url} """
    return(str)



# #TEST CASE
# t = "11:15"
# addr = """Greece Visa Application Centre- Abu Dhabi
# Level B2 (Lower Ground), The Mall World Trade Centre, Khalifa Bin Zayed the 1st Street Abu Dhabi
# Abu Dhabi,
# UAE"""
# city = "ABU DHABI"
# day = "MONDAY"
# generate_msg(t,addr,city,day)