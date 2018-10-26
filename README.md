# Ad Hoc Networks for coordinating relief efforts

### The Problem
During a natural calamity, one of the biggest challenges is communication. In most cases, network connectivity in affected areas is critically hit, to the point of non-existence in some cases. This makes it next to impossible for victims to communicate with external relief efforts for help, or the outside world in general. As such all efforts have to be taken making guesses as to where victims are likely to be.

### Our Solution
Our solution proposes the creation of cluster networks through WiFi Hotspots (and/or Bluetooth) over a certain region which will
1. Enable affected victims of that area to connect and share critical information, bringing aid at a faster pace.
2. Map all people who had ever connected to the network, so relief efforts know where to search if one person manages to connect to the outside world or is rescued.

## Solution in detail
The solution allows for groups of people in different areas of an affected region to form clusters among themselves through the creation of WiFi Hotspots (and/or Bluetooth).

### Connecting to Devices
Whenever a person connects to some network (cluster), they get access to co-ordinates of all the people who have connected to the cluster at any point in time. At the same time, they share co-ordinates of all people on any distinct network (cluster) that might exist. This way, at all times more information is shared and cluster knowledge sizes keep increasing, and ultimately relief aid can be brought to the members of this cluster.

In order to maximise connections, a device cycles through all available clusters, sharing data at each connect.

### Sharing Data
In order to keep as updated a list as possible, when connecting to a cluster a device shares and receives the list of all devices on any clusters it has been with the following data:
 - Device ID
 - Device co-ordinates
 - Time of last connection

If any of the data is new/updated, then all networks on the cluster store the updated values.

If any device gets cellular connectivity, all the data is instantly transferred to the nearest and centralized relief camps, and information on the camps is shared with the device for communicating with others.

### Misc
 - The system is automatically enabled in disaster management situations

## Features

- The mobile application would enable a peer to peer Wi-Fi and/or Bluetooth signal.
- Detect the location of all the available networks close by and exchange information in the background.
- Create a cluster mapping to know the position of the victims and display it on a map api.
- Information Update
  - Update the location of the person done by the app.
  - Modify the attention and critical alert levels and share the information with the other devices on the network.
- Find any device that has internet connectivity and upload the information of the main base camp server.
- The server at the base camp can then channel search teams and resources accordingly.
- As this solution only requires a mobile with wifi capability, it does not depend on traditional mobile network connections. Hence it is robust against network fluctuations commonly seen during natural disasters.

# Running the Code
Requirement: python3

```
pip install -r requirements.txt
python3 src/app/sim.py
```
