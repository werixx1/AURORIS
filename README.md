<div align="center">
<h1 style="font-family: 'Orbitron'">⟡ AURORIS - Aurora Forecast and Live Viewing App ⟡</h1>
Auroris is an interactive application that helps users track aurora activity and view live aurora transmissions from various locations. The app allows users to check if aurora is visible in their area based on their location (IP) and provides information about the KP index (auroral activity) and whenether it's high enough to see aurora. It also provides live streaming of auroras from popular locations worldwide.
</div>


## Features
   - Current Location Detection: Automatically retrieves the user's geographic location (latitude and longitude) using the IP address.
   - Aurora Forecast: Fetches the current KP index for auroral activity at the user's location to indicate whether auroras are visible.
   - Live Viewing: Provides links to live aurora streams from various locations around the world.
   - Resources: Includes links to relevant APIs and libraries used in the app.

## How it Works
   - Get User Location: The app uses the IP address to determine the user's current geographical location (latitude and longitude).
   - Aurora Data: The app uses the Auroras Live API to fetch the KP index data, which represents auroral activity.
   - Distance Calculation: The app calculates the distance between the user's location and other popular aurora viewing spots using the Haversine formula.
   - Live Streams: Based on the aurora visibility, users can view live streams of the aurora from different parts of the world.
   - Popup Information: The app provides additional information about how it works and useful resources (API links, etc.).

## Libraries and Technologies Used
   - CustomTkinter: A modern and customizable version of Tkinter used for building the graphical user interface (GUI).
   - WebView: A lightweight cross-platform library used for embedding web views within the application for live stream windows.
   - Requests: Used for making HTTP requests to APIs (Aurora API, IP geolocation).
   - Pillow: Used to handle and display images within the GUI (e.g., background images, icons).

## External APIs
   - IPInfo API: Used to retrieve the user's geographical location (latitude and longitude) based on their IP address. [link: https://ipinfo.io/]
   - Auroras Live API: Provides real-time aurora KP index data to determine aurora visibility. [link: http://auroraslive.io/#/api/v1]

## Figma elements used to design GUI
  - https://www.figma.com/community/file/1020701317322253884
  - https://www.figma.com/community/file/1101849114331939744
  - https://www.figma.com/community/plugin/752558325552095625/noise


