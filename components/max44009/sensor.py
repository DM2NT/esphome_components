import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, i2c
from esphome.const import (
    CONF_ID,
    CONF_MODE,
    DEVICE_CLASS_ILLUMINANCE,
    STATE_CLASS_MEASUREMENT,
    UNIT_LUX,
    CONF_STATE_CLASS,
    ICON_EMPTY
)

DEPENDENCIES = ["i2c"]

max44009_ns = cg.esphome_ns.namespace("max44009")
MAX44009Sensor = max44009_ns.class_(
    "MAX44009Sensor", sensor.Sensor, cg.PollingComponent, i2c.I2CDevice
)

MAX44009Mode = max44009_ns.enum("MAX44009Mode")
MODE_OPTIONS = {
    "auto": MAX44009Mode.MAX44009_MODE_AUTO,
    "low_power": MAX44009Mode.MAX44009_MODE_LOW_POWER,
    "continuous": MAX44009Mode.MAX44009_MODE_CONTINUOUS
}

CONFIG_SCHEMA = (sensor.sensor_schema(
        UNIT_LUX, ICON_EMPTY, 0, DEVICE_CLASS_ILLUMINANCE
    )
    .extend(
        {
            cv.GenerateID(): cv.declare_id(MAX44009Sensor),
            cv.Optional(CONF_STATE_CLASS, default=STATE_CLASS_MEASUREMENT): sensor.validate_state_class,
            cv.Optional(CONF_MODE, default="auto"): cv.enum(
                MODE_OPTIONS, upper=False
            ),
        }
    )
    .extend(cv.polling_component_schema("60s"))
    .extend(i2c.i2c_device_schema(0x4A))
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config[CONF_MODE])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
    await sensor.register_sensor(var, config)
