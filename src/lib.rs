use pyo3::prelude::*;

///Find the median of three numbers.
///
///Parameters
///----------
///u, v, w : float
///    The three numbers to find the median of.
///
///Returns
///-------
///float
///    median of u, v, w
fn med3(u: &f64, v: &f64, w: &f64) -> f64 {
    if (u <= v && v <= w) || (u >= v && v>= w) {
        v
    } else if (u <= w && w <= v) || (u >= w && w >= v) {
        w
    } else {
        u
    }
}


/// Find the index of the median of three numbers.
///
/// Parameters
/// ----------
/// u, v, w : float
///     The three numbers to find the index of the median of.
///
/// Returns
/// -------
/// int
//     -1 if u, 0 if v, or 1 if w is the median
fn imed3(u: f64, v: f64, w: f64) -> i64 {
    if (u <= v && v <= w) || (u >= v && v >= w) {
        0
    } else if (u <= w && w <= v) || (u >= w && w >= v) {
        1
    } else {
        -1
    }
}


#[pyfunction]
fn sm_3(
    mut x: Vec<f64>,
    mut y: Vec<f64>,
    n: i8,
    end_rule: i8
) -> (bool, Vec<f64>, Vec<f64>) {

    const N_CUTOFF: i8 = 2;
    let mut chg: bool = false;

    if n <= N_CUTOFF{
        for i in 0..n {
            y[i] = x[i];
        }
        return (false, x, y)
    }

    for i in 1..(n - 1) {
        let j: i64 = imed3(x[i-1], x[i], x[i+1]);
        y[i] = x[i+j];
        chg = chg || (j != 0);
    }

    sm_do_endrule(y, x, n, chg, end_rule)
}

fn median(numbers: &mut Vec<f64>) -> f64 {
    numbers.sort_by(|a, b| a.partial_cmp(b).unwrap();
    let mid = numbers.len() / 2;
    numbers[mid]
}

fn sm_do_endrule(
    mut y: Vec<f64>,
    mut x: Vec<f64>,
    n: i8,
    chg: bool,
    end_rule: i8,
) -> (bool, Vec<f64>, Vec<f64>) {
    match end_rule {
        0 => return (chg, y, x),
        1 => {
            y[0] = x[0];
            y[n-1] = x[n-1];
        },
        2 => {
            y[0] = Stats::median([3 * y[1] - 2 * y[2], x[0], y[1]]);
            chg = chg or (y[0] != x[0]);
            y[n - 1] = Stats::median([y[n - 2], x[n - 1], 3 * y[n - 2] - 2 * y[n - 3]]);
            chg = chg or (y[n - 1] != x[n - 1]);
        },
        _ => { panic!("invalid end-rule for running median of 3: {end_rule}"); }
    }

    (chg, y, x)
}

/// A Python module implemented in Rust.
#[pymodule]
fn pysmooth(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(med3, m)?)?;
    m.add_function(wrap_pyfunction!(imed3, m)?)?;
    m.add_function(wrap_pyfunction!(sm_3, m)?)?;
    Ok(())
}
