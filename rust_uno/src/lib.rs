//! Generated Rust bindings for FreedomOffice UNO types
//!
//! This crate contains automatically generated Rust bindings
//! for FreedomOffice UNO (Universal Network Objects) types.

// Core UNO functionality
pub mod core;
pub mod examples;
pub mod ffi;

// Auto-generated FFI bindings
pub mod generated;

/// Entry point function called by FreedomOffice to test Rust UNO bindings
/// This function is called from desktop/source/app/app.cxx during FreedomOffice startup
#[unsafe(no_mangle)]
pub extern "C" fn run_rust_uno_test() {
    println!("=== Rust UNO Bridge Test with Auto-Generated FFI ===");

    // Run the load_writer example to demonstrate service-style FFI functions
    examples::load_writer::run();

    println!("=== Rust UNO Bridge Test Done ===");
}
