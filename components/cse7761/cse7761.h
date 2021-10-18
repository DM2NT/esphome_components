#pragma once

#include "esphome/components/sensor/sensor.h"
#include "esphome/components/uart/uart.h"
#include "esphome/core/component.h"

namespace esphome {
namespace cse7761 {

/// This class implements support for the CSE7761 UART power sensor.
class CSE7761Component : public PollingComponent, public uart::UARTDevice {
 public:
  void set_voltage_sensor(sensor::Sensor *voltage_sensor) {
    voltage_sensor_ = voltage_sensor;
  }
  void set_active_power_1_sensor(sensor::Sensor *power_sensor_1) {
    power_sensor_1_ = power_sensor_1;
  }
  void set_current_1_sensor(sensor::Sensor *current_sensor_1) {
    current_sensor_1_ = current_sensor_1;
  }
  void set_active_power_2_sensor(sensor::Sensor *power_sensor_2) {
    power_sensor_2_ = power_sensor_2;
  }
  void set_current_2_sensor(sensor::Sensor *current_sensor_2) {
    current_sensor_2_ = current_sensor_2;
  }
  void setup() override;
  void loop() override;
  void dump_config() override;
  float get_setup_priority() const override;
  void update() override;

 protected:
  // Sensors
  sensor::Sensor *voltage_sensor_{nullptr};
  sensor::Sensor *power_sensor_1_{nullptr};
  sensor::Sensor *current_sensor_1_{nullptr};
  sensor::Sensor *power_sensor_2_{nullptr};
  sensor::Sensor *current_sensor_2_{nullptr};

  void write_(uint32_t reg, uint32_t data);
  bool read_once_(uint32_t reg, uint32_t size, uint32_t *value);
  uint32_t read_(uint32_t reg, uint32_t size);
  uint32_t read_fallback_(uint32_t reg, uint32_t prev, uint32_t size);
  bool chip_init_(void);
  void get_data_(void);
};

}  // namespace cse7761
}  // namespace esphome