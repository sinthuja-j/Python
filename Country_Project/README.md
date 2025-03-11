Country Catalogue Management System

Overview

This project provides a Country Catalogue Management System, which allows users to manage country-related data. The system reads country information from a data file, stores it in a catalogue, and provides functionalities to update, retrieve, and save the data.

Features

Country Representation: Each country is represented as an object with attributes such as name, population, area, and continent.
Country Catalogue: A catalogue stores multiple country objects and supports operations such as adding, updating, and retrieving country data.
Data Processing: The system processes update files to modify existing country data while logging invalid updates separately.
File Handling: Supports reading country data from a file and saving the updated catalogue to a new file.

Files and Modules
1. assign4_country.py
Defines the Country class, which represents an individual country with the following methods:

__init__: Initializes a country object.
__repr__: Returns a formatted string representation of a country.
getName, getPopulation, getArea, getContinent: Retrieve country attributes.
setPopulation, setArea, setContinent: Modify country attributes.

2. assign4_catalogue.py
Defines the CountryCatalogue class, which manages multiple Country objects with these functionalities:

Reads a data file and initializes a dictionary of Country objects.
Allows modifying country attributes (population, area, continent).
Supports adding new countries and searching for existing ones.
Saves the updated catalogue to a file.

3. assign4_procUpdates.py
Handles processing updates to the country catalogue by:

Reading an update file containing modification requests.
Validating updates (ensuring correct format and valid continent names).
Applying valid updates while logging invalid ones separately.
Saving the final country catalogue to an output file.

Error Handling
If the country data file or update file is missing, the user is prompted to provide a new file or exit.
Invalid updates (e.g., incorrect continent names, bad formatting) are logged separately.
