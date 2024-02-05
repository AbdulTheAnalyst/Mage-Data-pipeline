@transformer
def transform(data, *args, **kwargs):
    # Remove rows where passenger count is equal to 0 or trip distance is equal to zero
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create a new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Rename columns in Camel Case to Snake Case
    data.columns = [col.lower() for col in data.columns]

    return data

@test
def test_output(output, *args) -> None:
    # Assertion 1: vendor_id is one of the existing values in the column (currently)
    assert output['vendorid'].isin([1, 2]).all(), 'VendorID is not one of the existing values in the column'

    # Assertion 2: passenger_count is greater than 0
    assert (output['passenger_count'] > 0).all(), 'Passenger count is not greater than 0'

    # Assertion 3: trip_distance is greater than 0
    assert (output['trip_distance'] > 0).all(), 'Trip distance is not greater than 0'