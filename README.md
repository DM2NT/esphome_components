# ESPHome Components 
This is my particular collection of ESPHome components to add support for unsupported devices on mainline ESPHome.
All content is published under the ESPHome license.

## MCP4728
MCP4728 is a quad channel, 12-bit voltage output Digital-to-Analog Converter with non-volatile memory and I2C compatible Serial Interface.
 * Supported features
   * Each channel is exported as a `float output`.
   * Output Vref can be selected between `vdd` and `internal` (2.048V).
   * For `internal` Vref, two levels of gain can be selected (`X1` (default) and `X2`).
   * Two write modes are supported:
     * MultiWrite: write all channel settings without writing to non-volatile memory (EEPROM). This is the default and recommended mode.
     * SequentialWrite: write all channel settings to non-volatile memory (EEPROM) and apply this changes.
 * Unsupported features
   * Power-down mode selection (`NORMAL` is selected for all channels).
   * FastWrite mode as this requires the LDAC pin.
   * SingleWrite mode.

See [example_mcp4728.yaml](./example_mcp4728.yaml) for a reference usage file.

## MAX44009
The MAX44009 is an ambient light sensor featuring an I2C digital output
 * Supported features
   * Measure lux intensity
   * Measure mode selection:
     * Low power: The IC measures lux intensity only once every 800ms regardless of integration time.
     * Continuous mode: The IC continuously measures lux intensity.
     * Auto: Continuous mode for an update interval < 800ms, low power mode otherwise.
   * The device always runs on auto mode (hardware default).
 * Unsupported features
   * Manual mode.
   * Advanced power saving features (timers, thresholds, INT pin).

See [example_max44009.yaml](./example_max44009.yaml) for a reference usage file.
