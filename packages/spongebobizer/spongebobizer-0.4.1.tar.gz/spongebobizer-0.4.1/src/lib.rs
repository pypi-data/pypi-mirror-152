use pyo3::prelude::*;

use spongebobizer::process_string;

/// A Python module implemented in Rust.
#[pymodule]
fn spongebobizer(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(spongebobize, m)?)?;
    Ok(())
}

/// Converts alphabetic characters in a string
#[pyfunction]
fn spongebobize(input: &str) -> PyResult<String> {
	Ok(process_string(input))
}

