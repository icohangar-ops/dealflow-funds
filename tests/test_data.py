from dealflow_funds.data import load_rows


def test_synthetic_data_loads():
    rows = load_rows()
    assert len(rows) > 0
