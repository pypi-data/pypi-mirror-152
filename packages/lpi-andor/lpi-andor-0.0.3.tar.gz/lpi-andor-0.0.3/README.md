# LPI Andor
Andor spectrometer controller built for the LPI group at EPFL.

## Notes

### Limitations
Can only be run from Windows machines at the moment.

### Acquiring data
Background measurements are taken with the `Spectrometer#background` method, and signals are taken with the `Spectrometer#aquire` method.
Each returns a 1D Numpy array of counts. The wavelength for each index is stored in the `Spectrometer.wavelengths` property.
The `Spectrometer.wavelengths` property is reset any time the `Spectrometer.center_wavelength` property is set, so be sure to save the 
wavelength of previous scans before changing the center wavelength.

### Spectrograph configuration
For properties specific to your spectrograph (e.g. Filters, read out rates, etc.), define their configuration in the `enums` module.

### Shutdown
When running `Spectrometer#shutdown` method, the instance will block until the sensor temeprature has reached -15 C to prevent the sensor from heating too quickly. This can be overriden by calling `Spectrometer#shutdown( safe = False )` or by setting the default exit behavior with the `Spectrometer.exit_safe` property.

## Modules

+ **spectrometer:** Defines Spectrometer representing high level functionality of the spectrometer.
+ **enums:** Enums representing the spectrometer configuration.
+ **measurement_parameters:** Measurement parameters that are used to intialize the spectrometer.

## Example
```python
import time
import numpy as np
from lpi_andor import Spectrometer


# intialize spectrometer
spec = Spectrometer()
spec.temperature = -70
spec.enable_cooler()

# wait for temperature
while spec.temperature < 70:
	time.sleep( 10 )


# setup measurement
# center: 800 nm
# 10 scans, each for 1s
spec.center_wavelength = 800
spec.acquisition_accumulate()
spec.accumulation_scans = 10
spec.exposure_time = 1

# take measurement
background = spec.background()
signal = spec.acquire()

# compile data
data = np.dstack( ( spec.wavelengths, background, signal ) )
print( data )

# shutdown
spec.shutdown()
```