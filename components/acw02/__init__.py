import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

CONF_UART_ID = "uart_id"

acw02_ns = cg.esphome_ns.namespace("acw02")
ACW02 = acw02_ns.class_("ACW02", cg.Component, uart.UARTDevice)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(ACW02),
    cv.Required(CONF_UART_ID): cv.use_id(uart.UARTComponent),
})

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    uart_var = await cg.get_variable(config[CONF_UART_ID])
    cg.add(var.set_uart_parent(uart_var))
