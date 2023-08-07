use rusqlite::{Connection, ToSql, Transaction};
use pyo3::prelude::*;

const HMMSEARCH_INSERT_QUERY: &str = "INSERT OR IGNORE INTO orthograph_hmmsearch (
    'taxid',
    'query',
    'target',
    'score',
    'evalue',
    'log_evalue',
    'hmm_start',
    'hmm_end',
    'ali_start',
    'ali_end',
    'env_start',
    'env_end'
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

const BLASTP_INSERT_QUERY: &str =  "INSERT OR IGNORE INTO orthograph_blast (
'taxid',
'query',
'target',
'score',
'evalue',
'log_evalue',
'start',
'end',
'hmmsearch_id'
) VALUES (?,?,?,?,?,?,?,?,?)";


fn transaction_wrapper(mut conn: Connection, hits_list: Vec<Vec<&str>>, fields: u8, query: &str) {
    let tx = conn.transaction().unwrap();
    run_transaction(&tx, hits_list, fields as usize, query);
    tx.commit().unwrap();
}


fn run_transaction(transaction: &Transaction, hits_list: Vec<Vec<&str>>, fields: usize, query: &str) {
    let mut statement = transaction.prepare_cached(query).unwrap();
    for hit in hits_list.iter() {
        let mut param_values: Vec<_> = Vec::new();
        for i in 0..fields{
        param_values.push(&hit[i] as &dyn ToSql);
        }
        statement.execute(&*param_values).unwrap();
    }
}

#[pyfunction]
fn hmmsearch_inserts(db_path: &str, hits_list: Vec<Vec<&str>>, use_pragma: bool) {
    let conn = Connection::open(db_path).unwrap();
    if use_pragma {
            conn.execute_batch(
        "PRAGMA journal_mode = OFF;
              PRAGMA synchronous = 0;
              PRAGMA cache_size = 1000000;
              PRAGMA locking_mode = EXCLUSIVE;
              PRAGMA temp_store = MEMORY;",
    )
    .expect("PRAGMA");
    }
    transaction_wrapper(conn, hits_list, 12, HMMSEARCH_INSERT_QUERY);
}

#[pyfunction]
fn blastp_inserts(db_path: &str, hits_list: Vec<Vec<&str>>, use_pragma: bool) {
    let conn = Connection::open(db_path).unwrap();
    if use_pragma {
            conn.execute_batch(
        "PRAGMA journal_mode = OFF;
              PRAGMA synchronous = 0;
              PRAGMA cache_size = 1000000;
              PRAGMA locking_mode = EXCLUSIVE;
              PRAGMA temp_store = MEMORY;",
    )
    .expect("PRAGMA");
    }
    transaction_wrapper(conn, hits_list, 9, BLASTP_INSERT_QUERY);
}

/// Module for running sql inserts from orthograph analyzer.
#[pymodule]
fn inserts(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hmmsearch_inserts, m)?)?;
    m.add_function(wrap_pyfunction!(blastp_inserts, m)?)?;
    Ok(())
}