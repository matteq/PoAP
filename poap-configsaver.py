#!/bin/env python


# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



 
import sys
import xml.etree.cElementTree as ET

cdp_dict = {}

def get_cdp_info():
    #get the cdp info of mgmt0 to generate the config file name
    #grep cdp info of mgmt0 in XML
    raw_input = cli("show cdp neighbors int mgmt0")

# Split the output into a list containing each line
    all_raw_lines = raw_input.split('\n')
#print all_raw_lines



# We need to ignore the first few lines, including the header of the table. This
# code does that

    all_device_lines = []
    line_no = 0
    dev_list = {}
    for line in all_raw_lines:
        line_no += 1
        if line_no <= 6:
            pass
        else:
            all_device_lines.append(line)

# Also remove the last three lines, which contain the footer - Total Entries
# displayed

    for i in range(3):
        all_device_lines.pop();


#print all_device_lines

# We now have only the table, which has a line containing switch nae followed by
# the cdp details

# We iterate through this to build up our dictionary of local ports connected to
# particular remote port and platform, switch

# We use the local port as the key

    for idx, line in enumerate(all_device_lines):
        if (idx % 2 == 0):
            pass
        else: 
            thisline = re.split('\s+',line)
            dev_list[thisline[1]] = {}
            dev_list[thisline[1]]['remote_port'] = thisline[-2]
            dev_list[thisline[1]]['platform'] = thisline[-3]
            dev_list[thisline[1]]['switch_name'] = all_device_lines[idx-1]


def save_to_server($server, $login, $password, $location, $file):
    c = transfer("ftp", "$server", "$location","$file", user="$login", password="$password")

def create_config_file($cdp_info):
#as we are using CDP for PoAP the file needs to be in the following format : e.g. mgmt0 is connected to Core1 eth1/2 conf_Core1_eth1/2.cfg
    

def main():
    #get neighbor info of mgmt0
    get_cdp_info()
    create_config_file()
    #Save
    save_to_server()



if __name__=="__main__":
    sys.exit(main())