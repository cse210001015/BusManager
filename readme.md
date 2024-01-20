BUS BOOKING SYSTEM ::

BACKEND + DATABASE WORK::

Users (UserID | UserName | Password | UserCoordinates | Admin?)
Buses (BusID | SeatPlan | OperationDays | Booked?)
Bookings (BookingID | UserID | BusID | SeatLoc | Departure | Arrival)
Stops (LocationID | BusID | BusArrivalTime | BusDepartureTime)
Routes (FromID | ToID | Distance | Cost | Time) (relation between stops)
Location (LocationName | Coordinates)

Users need an authentication SYSTEM

Some users will have the admin role that gives the
    CREATE | READ | UPDATE | DELETE 
        buses with SeatPlan
        Routes cost, time and distance
        Stops (New Stops and their schedules)

LOW PRIORITY :: Some users maybe drivers who will need to access their scheduling system
(entirely based on making some use of the OperationDays counter)

Users can book buses to move from A to B
    do BFS / DFS on locations to find plausible paths, query cost, distance and time from routes for path metrics report them to the UserID 
        who can then create Bookings onPayment (swipe integration??)
filter the buses with nearestFirst requirement from UserLoc
Users can cancel anytime with cancellation charges


This is the DataBase ER Diagram:  https://lucid.app/lucidchart/0bd8ad43-051a-43e0-b08a-de66327a824a/edit?existing=1&token=b6e0a3571d2ff6ff834d283afdb2522fae852c270c8af043bf5f1d8a5353178c-eml%3Dcse210001015%2540iiti.ac.in%26ts%3D1705740854%26uid%3D175057260&docId=0bd8ad43-051a-43e0-b08a-de66327a824a&shared=true&invitationId=inv_c148f699-8730-4ef8-8ab2-435ba9a97a13
