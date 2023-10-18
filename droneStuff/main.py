from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading
connection_string = "tcp:127.0.0.1:5762"
hostName = "127.0.0.1"
serverPort = 8080
global webserverOut
global kill
kill = 0
webserverOut = ""
class MyServer(BaseHTTPRequestHandler):
    global webserverOut
    def do_GET(self):
        global webserverOut
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>go away >:(</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>if you are seeing this and you ARE NOT the website, go away</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        webserverOut = self.path
        print(webserverOut)
    
def serverThread():
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
webserver = threading.Thread(target=serverThread)
webserver.start()
#main loop
print("connecting to drone")
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal
import math
input("start dronekit-sitl and connect missionPlanner, then press enter")
print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)
print("mainloop started")
while True:
    time.sleep(1)
    if webserverOut != "":
        print("got data: ", webserverOut)
        
        cordLatLon = webserverOut.split(",")
        webserverOut = ""
        cordLatLon[0] = cordLatLon[0].replace("/","")
        print(cordLatLon)

        height = 15
        # show the admin that the drone, is infact, sane
        print("Get some vehicle attribute values:")
        print(" GPS: %s" % vehicle.gps_0)
        print(" Battery: %s" % vehicle.battery)
        print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
        print(" Is Armable?: %s" % vehicle.is_armable)
        print(" System status: %s" % vehicle.system_status.state)
        print(" Mode: %s" % vehicle.mode.name)    # settable

        # how close are we to the target point
        def get_distance_metres(aLocation1, aLocation2):
            """
            Returns the ground distance in metres between two LocationGlobal objects.

            This method is an approximation, and will not be accurate over large distances and close to the 
            earth's poles. It comes from the ArduPilot test code: 
            https://github.com/diydrones/ardupilot/blob/master/Tools/autotest/common.py
            """
            dlat = aLocation2.lat - aLocation1.lat
            dlong = aLocation2.lon - aLocation1.lon
            return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5
        
        # this does a bunch of fancy stuff for the takeoff
        def arm_and_takeoff(aTargetAltitude):
            """
            Arms vehicle and fly to aTargetAltitude.
            """

            print("Basic pre-arm checks")
            # Don't try to arm until autopilot is ready
            while not vehicle.is_armable:
                print(" Waiting for vehicle to initialise...")
                time.sleep(1)

            print("Arming motors")
            # Copter should arm in GUIDED mode
            vehicle.mode = VehicleMode("GUIDED")
            vehicle.armed = True
            print(vehicle.mode)

            # Confirm vehicle armed before attempting to take off
            while not vehicle.armed:
                print(" Waiting for arming...")
                time.sleep(1)

            print("Taking off!")
            if vehicle.armed:
                vehicle.simple_takeoff(aTargetAltitude) # Take off to target altitude

                # Wait until the vehicle reaches a safe height before processing the goto (otherwise the command
                #  after Vehicle.simple_takeoff will execute immediately).
                while True:
                    print(" Altitude: ", vehicle.location.global_relative_frame.alt)
                    #Break and return from function just below target altitude.
                    if vehicle.location.global_relative_frame.alt>=aTargetAltitude*0.95:
                        print("Reached target altitude")
                        break
                    time.sleep(1)

        arm_and_takeoff(height)
        #41.4695185, -81.9325376
        print("cord: ",cordLatLon)
        a_location = LocationGlobalRelative(float(cordLatLon[0]),float(cordLatLon[1]), height)
        print(a_location)
        def gotoLocation(location,acc):
            vehicle.simple_goto(location)
            print(get_distance_metres(vehicle.location.global_frame, location))
            while get_distance_metres(vehicle.location.global_frame, location)>=acc:
                time.sleep(1)
                print(get_distance_metres(vehicle.location.global_frame, location))
        # Close vehicle object before exiting script
        gotoLocation(a_location,2)
        a_location = LocationGlobalRelative(float(cordLatLon[0]),float(cordLatLon[1]), 3)
        gotoLocation(a_location,2)
        a_location = LocationGlobalRelative(float(cordLatLon[0]),float(cordLatLon[1]), height)
        gotoLocation(a_location,2)
                
        vehicle.mode = VehicleMode("RTL")