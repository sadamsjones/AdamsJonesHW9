#include <iostream>
#include <cmath>
#include <iomanip> // for setprecision
#include "AnalogIn.h" // Include the AnalogIn header file
#include <string.h>
//#include "AnalogIn.cpp"

//Example Invocation ./read_resistance_2


int main() {
    AnalogIn analogIn; //AnalogIn Instance

    // Constants for the voltage divider circuit
    const double Vcc = 1.8; // Voltage across both resistors
    const double R1 = 10000.0; // Top resistor (10kΩ)

    // Analog input pins
    const std::string analogInPin = "P9_39";

    // Set the pin for AnalogIn
    analogIn.setPin(analogInPin.c_str());

    // Get the analog value from the sensor
    std::cout << "Using " << analogIn.getPin() << " to read analog value." << std::endl;
    int analogValue = analogIn.readAdcSample();

    // Calculate the resistance using the voltage divider formula
    double resistance = R1 * (Vcc / analogValue - 1);

    // Round the resistance to the nearest Ohm
    int roundedResistance = static_cast<int>(std::round(resistance));

    // Print the result based on the resistance value
    if (roundedResistance < 1000) {
        std::cout << "Measuring resistance ..." << std::endl;
        std::cout << "ADC value is: " << analogValue << std::endl;
        std::cout << "Resistance: " << roundedResistance << " Ohms" << std::endl;
    } else {
        std::cout << "Measuring resistance ..." << std::endl;
        std::cout << "ADC value is: " << analogValue << std::endl;
        std::cout << "Resistance: " << std::fixed << std::setprecision(2) << roundedResistance / 1000.0 << "K Ohms" << std::endl;
    }
    return 0;
}

