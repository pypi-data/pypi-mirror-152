pub mod bindings;
pub mod macros;

extern "C" {
    pub fn _putchar(c: u8);
    pub fn _get_plc_mem_devices_struct() -> &'static mut bindings::plc_dev_t;
}
