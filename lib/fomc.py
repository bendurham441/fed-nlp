def get_lname(string):
    return string.split(' ')[-1][:-1].lower()


def get_pres(region, date, prdf):
    import pandas as pd
    
    for i, row in prdf[prdf['Bank'] == region].iterrows():
        range = pd.period_range(row.In, to_date(row.Out))
        if date in range:
            return row.lname
    return f'{region}-{date}'

def lname_extract(full_name):
    name_arr = [part.lower() for part in full_name.split(' ')]
    if name_arr[-1] == 'jr.':
        name_arr = name_arr[:-1]
    return name_arr[-1]

def init_fomc(pres_path, bog_path):
    import pandas as pd
    prdf = pd.read_csv(pres_path)
    prdf.fillna({'Out': '', 'Interim': 0}, inplace=True)
    prdf['lname'] = prdf['Name'].apply(lname_extract)
    bog = pd.read_csv(bog_path)
    bog.fillna('', inplace=True)
    return prdf, bog

def to_date(string):
    import datetime
    if string != '':
        return datetime.datetime.strptime(string, '%m-%d-%Y')
    return datetime.datetime.today()

def get_bog(date, bog):
    import pandas as pd
    bog_members = []
    for i, row in bog.iterrows():
        range = pd.period_range(row.start, to_date(row.end))
        if date in range:
            bog_members.append(row.lname)
    return bog_members

def get_fomc(date, prdf, bog):
    regions = ['Richmond', 'Philadelphia', 'San Francisco', 'St. Louis', 'Cleveland',
            'Chicago', 'Boston', 'Minneapolis', 'Atlanta', 'Dallas', 'New York', 'Kansas City']
    return [get_pres(region, date, prdf) for region in regions] + get_bog(date, bog)