<img src="images/KLM_logo.svg" width="80">

___

# Airline Booking System

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Overview
This project implements a simple airline booking management system for KLM in Python. It includes functionalities to add bookings and query them based on departure times and routes.

## Features
- Add new flight bookings.
- Retrieve bookings departing before a specified time.
- Retrieve bookings for a specific route (origin to destination).

## Prerequisites
- Python 3.10 or higher

## Setup
1. Clone the repository
2. Navigate to the project directory
3. Run the project using Python (there are no third party libraries)

```bash
git clone https://github.com/dariomory/klm-booking-system.git
cd klm-booking-system
python main.py
```

## Tests

Run the tests using the following command:

```bash
python3 -m unittest discover tests
```

## Usage
To use the BookingManager, create an instance of the BookingManager class and use its methods to manage bookings.

See also: `demo.py`

### Creating Itineraries
```python
from klm_booking_system import Itinerary

itinerary = Itinerary(["AMS", "LHR", "JFK"])
```

### Making a Booking

```python
from klm_booking_system import Booking
from datetime import datetime

booking = Booking(datetime(2023, 5, 26, 6, 45), itinerary)
```

### Managing Bookings

```python
from klm_booking_system import BookingManager

manager = BookingManager()
manager.add_booking(booking)
```

### Querying Bookings

```python
bookings_before_date = manager.bookings_before(datetime(2023, 6, 1))
bookings_on_route = manager.bookings_for_route("AMS", "LHR")
```