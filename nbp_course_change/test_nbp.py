import nbp_change

# values, full_name = get_courses(currency_code, days)
def mock_get_courses(currency_code, days):
    name = 'Mock name'
    val = [5]*days
    # for i in range(1, len(days)):
    #     val.append(val[i-1]+0.2)
    return val, name

def test_calc_statistics(monkeypatch):
    monkeypatch.setattr("nbp_change.get_courses", mock_get_courses)
    res = nbp_change.calc_statistics(["GBP"], 10)
    # {'GBP': {'change': 1.003759172981944, 'course': 5.0199, 'full_name': 'funt szterling'}}
    assert res['GBP']['change'] == 1
    assert res['GBP']['course'] == 5
    assert res['GBP']['full_name'] == 'Mock name'

