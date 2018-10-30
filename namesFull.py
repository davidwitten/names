import sqlite3
from matplotlib import pyplot as plt
import math, numpy as np
import webbrowser, csv, os
conn = sqlite3.connect('names.db')

#Source: https://catalog.data.gov/dataset/baby-names-from-social-security-card-applications-data-by-state-and-district-of-
#https://fivethirtyeight.com/features/how-to-tell-someones-age-when-all-you-know-is-her-name/


#TODO: average age of name


#Names that are expanding: Reynaldo, Ruthie, Esperanza, Margarita, Blanca, Maria* (which is super popiular now)

#Switched: Lizzie, Sammie, Ruthie, Rachel*

#Ryan, Lisa, Joshua* (used to be super southern), Ashley

#Kevin, from NE to nation


#Everyone -> centralized: Betty, Shirley

#Hard-coded in
total = [(1910, 516314), (1911, 565822), (1912, 888001), (1913, 1028581), (1914, 1293346), (1915, 1690016), (1916, 1786521), (1917, 1855694), (1918, 2013354), (1919, 1954819), (1920, 2101103), (1921, 2170945), (1922, 2127296), (1923, 2141727), (1924, 2218862), (1925, 2172453), (1926, 2137446), (1927, 2160493), (1928, 2105666), (1929, 2040908), (1930, 2071087), (1931, 1959273), (1932, 1964682), (1933, 1857969), (1934, 1933629), (1935, 1947208), (1936, 1936447), (1937, 1986912), (1938, 2068497), (1939, 2060068), (1940, 2157777), (1941, 2288426), (1942, 2576719), (1943, 2665101), (1944, 2537270), (1945, 2501960), (1946, 3032558), (1947, 3427692), (1948, 3280348), (1949, 3312351), (1950, 3330537), (1951, 3507113), (1952, 3617593), (1953, 3667968), (1954, 3791378), (1955, 3823178), (1956, 3925857), (1957, 4002187), (1958, 3933674), (1959, 3955206), (1960, 3947893), (1961, 3930285), (1962, 3825808), (1963, 3747769), (1964, 3674739), (1965, 3419702), (1966, 3267919), (1967, 3184354), (1968, 3159851), (1969, 3245111), (1970, 3359602), (1971, 3177636), (1972, 2890196), (1973, 2759385), (1974, 2774010), (1975, 2744585), (1976, 2753993), (1977, 2882836), (1978, 2877538), (1979, 3019008), (1980, 3130677), (1981, 3146258), (1982, 3193151), (1983, 3153863), (1984, 3176979), (1985, 3246454), (1986, 3228422), (1987, 3266619), (1988, 3341430), (1989, 3475561), (1990, 3567015), (1991, 3503086), (1992, 3442568), (1993, 3364306), (1994, 3307657), (1995, 3249717), (1996, 3225567), (1997, 3193822), (1998, 3230178), (1999, 3234048), (2000, 3297841), (2001, 3252018), (2002, 3238979), (2003, 3290057), (2004, 3295289), (2005, 3306909), (2006, 3389627), (2007, 3414740), (2008, 3342853), (2009, 3235216), (2010, 3120176), (2011, 3083811), (2012, 3080220), (2013, 3075928), (2014, 3137104), (2015, 3128534), (2016, 3091230), (2017, 2990357)]
states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC','DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
coords = {'NH': [43.452492, -71.563896], 'KS': [38.5266, -96.726486], 'NJ': [40.298904, -74.521011], 'FL': [27.766279, -81.686783], 'AL': [32.806671, -86.79113], 'CA': [36.116203, -119.681564], 'NC': [35.630066, -79.806419], 'AZ': [33.729759, -111.431221], 'WA': [47.400902, -121.490494], 'LA': [31.169546, -91.867805], 'MI': [43.326618, -84.536095], 'ND': [47.528912, -99.784012], 'WY': [42.755966, -107.30249], 'DC': [38.897438, -77.026817], 'TN': [35.747845, -86.692345], 'DE': [39.318523, -75.507141], 'MS': [32.741646, -89.678696], 'IL': [40.349457, -88.986137], 'GA': [33.040619, -83.643074], 'CO': [39.059811, -105.311104], 'AK': [61.370716, -152.404419], 'IA': [42.011539, -93.210526], 'NM': [34.840515, -106.248482], 'MA': [42.230171, -71.530106], 'ME': [44.693947, -69.381927], 'MD': [39.063946, -76.802101], 'MO': [38.456085, -92.288368], 'OK': [35.565342, -96.928917], 'NE': [41.12537, -98.268082], 'HI': [21.094318, -157.498337], 'OR': [44.572021, -122.070938], 'MT': [46.921925, -110.454353], 'VA': [37.769337, -78.169968], 'OH': [40.388783, -82.764915], 'UT': [40.150032, -111.862434], 'NY': [42.165726, -74.948051], 'TX': [31.054487, -97.563461], 'RI': [41.680893, -71.51178], 'SD': [44.299782, -99.438828], 'NV': [38.313515, -117.055374], 'AR': [34.969704, -92.373123], 'VT': [44.045876, -72.710686], 'KY': [37.66814, -84.670067], 'SC': [33.856892, -80.945007], 'CT': [41.597782, -72.755371], 'WI': [44.268543, -89.616508], 'ID': [44.240459, -114.478828], 'PA': [40.590752, -77.209755], 'MN': [45.694454, -93.900192], 'IN': [39.849426, -86.258278], 'WV': [38.491226, -80.954453]}
abbrevs = { 'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa', 'AZ': 'Arizona', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DC': 'District of Columbia', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'GU': 'Guam', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri', 'MP': 'Northern Mariana Islands', 'MS': 'Mississippi', 'MT': 'Montana', 'NA': 'National', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'PR': 'Puerto Rico', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 'VI': 'Virgin Islands', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'WY': 'Wyoming' }
male = [2e-05, 3.2999999999999996e-05, 8e-05, 0.00016, 0.00031800000000000003, 0.00059, 0.001044, 0.0018059999999999999, 0.0029960000000000004, 0.0048389999999999996, 0.00758, 0.011793, 0.0177, 0.025668000000000003, 0.036032, 0.049015, 0.064806, 0.083496, 0.10506, 0.129376, 0.15621, 0.185463, 0.21638200000000002, 0.248477, 0.281268, 0.31431, 0.347276, 0.379954, 0.41219, 0.443888, 0.47494, 0.503668, 0.531422, 0.558155, 0.58397, 0.60892, 0.632958, 0.6559339999999999, 0.6777580000000001, 0.698464, 0.71814, 0.734997, 0.7507560000000001, 0.765417, 0.77903, 0.79165, 0.8033560000000001, 0.814208, 0.824282, 0.833645, 0.84234, 0.8510989999999999, 0.859306, 0.867004, 0.87424, 0.881055, 0.887528, 0.8937280000000001, 0.899706, 0.9055, 0.91114, 0.916302, 0.92124, 0.92593, 0.9303680000000001, 0.934585, 0.938588, 0.9423969999999999, 0.9460080000000001, 0.9494389999999999, 0.9527, 0.95519, 0.957534, 0.9597410000000001, 0.961834, 0.963825, 0.96572, 0.967542, 0.9693080000000001, 0.9710230000000001, 0.97269, 0.9741289999999999, 0.9755739999999999, 0.9770719999999999, 0.978616, 0.9802, 0.981786, 0.9833289999999999, 0.984784, 0.98615, 0.98743, 0.988448, 0.9893439999999999, 0.990084, 0.99068, 0.991135, 0.9914839999999999, 0.9917860000000001, 0.992078, 0.992376, 0.9927, 0.9929389999999999, 0.9931939999999999, 0.993445, 0.9937119999999999, 0.99403, 0.994376, 0.994837]
female = [0.00016, 0.000337, 0.0006640000000000001, 0.0012259999999999999, 0.002162, 0.00363, 0.00588, 0.009186, 0.013902000000000001, 0.020429, 0.02925, 0.041329, 0.056673999999999995, 0.075488, 0.09777799999999999, 0.12331, 0.151798, 0.182807, 0.215812, 0.25027299999999997, 0.28562, 0.322029, 0.35834, 0.394142, 0.429092, 0.46294, 0.49548800000000004, 0.526612, 0.556264, 0.584514, 0.61148, 0.637108, 0.661406, 0.6843739999999999, 0.706152, 0.726885, 0.746576, 0.7651819999999999, 0.78268, 0.7991539999999999, 0.81471, 0.827459, 0.839252, 0.850105, 0.860078, 0.86924, 0.8776560000000001, 0.885371, 0.89245, 0.8989489999999999, 0.90492, 0.910715, 0.916052, 0.9209639999999999, 0.925492, 0.929675, 0.933562, 0.937202, 0.9406180000000001, 0.943862, 0.94693, 0.949924, 0.952782, 0.955514, 0.958138, 0.96067, 0.9631, 0.965425, 0.9676260000000001, 0.96973, 0.97172, 0.973267, 0.974712, 0.976065, 0.977326, 0.97851, 0.9796239999999999, 0.9806819999999999, 0.981688, 0.982643, 0.98357, 0.984324, 0.985062, 0.9857739999999999, 0.986474, 0.98716, 0.9878439999999999, 0.988512, 0.9891739999999999, 0.98983, 0.99048, 0.991015, 0.9915039999999999, 0.99193, 0.9922960000000001, 0.99261, 0.99288, 0.9931310000000001, 0.993376, 0.99363, 0.99389, 0.9940889999999999, 0.9942939999999999, 0.994498, 0.9947060000000001, 0.99495, 0.9952439999999999, 0.995638]

'''to do:'''
#fix zeroes
def setup():
 #   conn.execute("create table names (name text not null, gender text not null, state text not null, year int not null, count int not null);")
    for i in ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC','DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']:
        readin(i + '.txt')
    conn.commit()

def percentile(s, p, weights=None):
    """
    Find percentiles *p* in sample *s* where each *s* is weighted by *w*.

    This sorts the weights in increasing *s* and converts them to a normalized
    CDF.  The index of *p* in the CDF is then used to return the corresponding
    value in the sorted *s*.
    """
    if weights is None:
        weights = np.ones(len(s))
    idx = np.argsort(s)
    s, w = s[idx], weights[idx]
    w = np.cumsum(w)
    w = w/w[-1]
    q_idx = np.searchsorted(w, p)
    q = s[q_idx]
    return q

def variation(name, gender, raw=False, state = None, both = False):
    stringState = (" and state = '" + state + "' ") if state != None else ""
    you = list(conn.execute("select year, sum(count) from names where name = '" + name + "' and gender = '" + gender + "'" + stringState + " group by year"))
    r = [(i[0], 0) if i[0] not in [year[0] for year in you] else (i[0], you[[j[0] for j in you].index(i[0])][1] * (1/i[1] if not(raw) else 1)) for i in  total]
    r = [i[1] for i in r]
    return np.std(r)/sum(r) *len(r)
    

def readin(file):
    f = open(file)
    text = f.readlines()
    for i in text:
        u = i.split(',')
        conn.execute("insert into names (name, gender, state, year, count) \
    values ('" + u[3] + "','" + u[1] + "','" + u[0]+ "',"+ u[2]+',' + u[4]+")")
    
    f.close()

def graph(name, gender=None, state = None, raw = True):
    if state == None:
        stringState = ""
        addition = ""
    else:
        stringState =" and state = '"+state + "' "
        addition = " in " + state
    if gender == None:
        stringGender = ""
    else:
        stringGender = " and gender = '" + gender + "' "
    cursor = conn.execute("select year, sum(count) from names where name = '"+name+"'"+stringState+stringGender+" group by year")
    c = [i for i in cursor]
    d = [0 if i not in [j[0] for j in c] else c[[j[0] for j in c].index(i)][1]*(100/total[i-1910][1] if not(raw) else 1) for i in range(1910, 2018)]
    plt.title("Births of " + name + addition)
    plt.plot(list(range(1910, 2018)), d)
    plt.ylabel(("Percent of " if raw == False else "") + "Births")
    plt.xlabel("Year")
    return d

def mostPopularState(name, year, gender = None,raw = False,n = 10):
    cursor = conn.execute("select state, sum(count) from names where name = '" + name + "' and year" + str(year) + " group by state")
    cursor2 = conn.execute("select state, sum(count) from names where year" + str(year) + " and gender = '" + gender + "' group by state")# and year =" + str(year))
    c = [i for i in cursor]
    d = [i for i in cursor2]
    e = [(i[0], 0) if i[0] not in [k[0] for k in c] else (i[0], c[[k[0] for k in c].index(i[0])][1]*(100/i[1] if not(raw) else 1)) for i in d]
    e = sorted(e, key = lambda x: x[1])[::-1]
    plt.bar(list(range(n)), [i[1] for i in e][:n], align = 'center')
    plt.xticks(list(range(n)), [i[0] for i in e][:n])
    plt.title("Most Popular States for "+name+" in " + str(year))
    plt.ylabel(("Percent of " if raw == False else "") + "Births")
    plt.xlabel("States")
#    plt.show()
    return e

def topN(state, year,gender, n = 10, raw = True):
    cursor = conn.execute("select name, count from names where state = '"+state + "' and year = " + str(year) + " and gender ='" + gender + "' order by -count")
    p = list(cursor)
    print(len(p))
    total = sum([i[1] for i in p])
 #   print(p)
    j = p[:n]
    print([i[1]*(100/sum([u[1] for u in p]) if not(raw) else 1) for i in j])
    plt.bar(list(range(n)), [i[1]*(100/total if not(raw) else 1) for i in j], align = 'center')
    plt.xticks(list(range(n)), [i[0] for i in j])
    plt.title("Most Popular " + ("Boy" if "M" else "Girl")+" Names in "+state+" in " + str(year))
    plt.ylabel(("Percent of " if raw == False else "")+ "Births")
    plt.show()
    return [[i[0], i[1]*(100/sum([i[1] for i in p]) if not(raw) else 1)] for i in j]

def mostConstant():
    #most popular 1000 names:
    cursor = conn.execute("select name, sum(count) from names group by name")
    print("Done generating")
    top1000 = sorted([i for i in cursor], key = lambda x: -1*x[1])[:200]
    print("Done sorting")
    newArray =[]
    for i in range(200):
        newArray.append([top1000[i][0], variation(top1000[i][0])])
        if i%10 == 0:
            print(i)
    return newArray


def percentileName(name, gender, pct):
    cursor = conn.execute("select year, sum(count) from names where name = '" + name + "' and gender = '" + gender + "' group by year")
    k = [[2018 - i[0], i[1]*(male if gender == 'M' else female)[i[0] - 1910]] for i in cursor]
    a = [i[0] for i in k][::-1]
    b = [i[1] for i in k][::-1]
    return percentile(np.array(a), pct, np.array(b)/sum(b))
#    x =  [percentile(np.array(a), i, np.array(b)/sum(b)) for i in [0.25, .5, .75]]

#TODO: fix graphing issue like chuck    
def median_age(name, gender):
    if not(insideTotals(name, gender)):
        cursor = conn.execute("select year, sum(count) from names where name = '" + name + "' and gender = '" + gender + "' group by year") 
        k = [[2018 - i[0], i[1]*(male if gender == 'M' else female)[i[0] - 1910]] for i in cursor]
        a = [i[0] for i in k][::-1]
        b = [i[1] for i in k][::-1]
        return [percentile(np.array(a), i, np.array(b)/sum(b)) for i in [0.25, .5, .75]]
    else:
        return list(conn.execute("select low, med, high from totals where name = '" + name + "' and gender = '" + gender + "'"))[0]
  #  print(len(k))
#    print(a)
#    print(b)
#    plt.plot(a,b)# bins = 100)
#    print(a)
 #   plt.fill_between(a[x[0]:x[-1]], b[x[0]:x[-1]])
#    plt.show()

def insideTotals(name, gender):
    return len(list(conn.execute("select 1 from totals where name = '" +name+ "' and gender = '" + gender+ "'")))

def create_totals():
    cursor = conn.execute("select distinct(name), gender, sum(count) from names group by name, gender")
    top1000 = sorted([i for i in cursor], key = lambda x: -1*x[2])[1600:1800]
    #conn.execute("create table totals (name text not null, gender text not null, stdRaw float, stdPct float, low float, med float, high float, total int);")
    for n,i in enumerate(top1000):
        x,y = variation(i[0],i[1], both = True)
        a,b,c = median_age(i[0], i[1])
        conn.execute("insert into totals (name, gender, stdRaw, stdPct, low, med, high, total) \
values ('" + i[0] + "','" + i[1] + "'," + str(x)+ ","+str(y)+',' +
str(a)+',' + str(b)+',' + str(c)+"," + str(i[2]) +")")
        if n%50 == 0:
            print(n)
        if n < 10:
            print(i)
        conn.commit()



def myPercentile(name, gender, age):
    print(3)


def geography(name, year, gender = None):
    cursor = conn.execute("select state, sum(count) from names where name = '" + name + "' and gender = '" + gender + "' and year" + str(year) + " group by state")
    cursor2 = conn.execute("select state, sum(count) from names where year" + str(year) + " and gender = '" + gender + "' group by state")# and year =" + str(year))
    c = [i for i in cursor]
    d = [i for i in cursor2]
    e = [0 if i[0] not in [k[0] for k in c] else c[[k[0] for k in c].index(i[0])][1]*100/i[1] for i in d]
    e = sorted(e)[::-1]
    return sum(e[:5])/sum(e)

def percentAlive(name, gender):
    cursor = list(conn.execute("select year, sum(count) from names where name = '" + name + "' and gender = '" + gender + "' group by year")) 
    k = [[2018 - i[0], i[1]*(male if gender == 'M' else female)[i[0] - 1910]] for i in cursor]
    return sum([i[1] for i in k])/sum([i[1] for i in cursor])


#This is doing it by standard deviation/mean
def bestGeography1():
    j = conn.execute("select name from totals order by -1 * total")
    f = [next(j)[0] for i in range(100)]
    state_totals = [430161, 5815853, 3433745, 3598468, 30527811, 3627048, 3466933, 1450522, 640358, 10008972, 8593426, 981539, 4222176, 1205511, 15670010, 7435562, 3325885, 5514027, 5733608, 7796910, 4674750, 1415699, 12004123, 5784508, 7027352, 4068851, 969844, 8829082, 1088992, 2327275, 987775, 8633002, 1700657, 940408, 24465590, 14651955, 4285275, 2804896, 17111472, 1175133, 4549782, 1078128, 6583232, 22868433, 2461619, 7009089, 557552, 4904376, 6289402, 3018726, 435016]
    each = [[i[0] for i in conn.execute("select sum(count) from names where name = '" + i + "' group by state")] for n,i in enumerate(f)]
    each = [[k[i]/state_totals[i] for i in range(len(state_totals))] for k in each]
    each = [np.std(i)/sum(i) * len(i) for i in each]
    return sorted([[f[i], each[i]] for i in range(len(each))], key = lambda x: -x[1])


#Fill in names
#E.g. Reginald, 
def geoMeasure1(name):
    state_totals = [430161, 5815853, 3433745, 3598468, 30527811, 3627048, 3466933, 1450522, 640358, 10008972, 8593426, 981539, 4222176, 1205511, 15670010, 7435562, 3325885, 5514027, 5733608, 7796910, 4674750, 1415699, 12004123, 5784508, 7027352, 4068851, 969844, 8829082, 1088992, 2327275, 987775, 8633002, 1700657, 940408, 24465590, 14651955, 4285275, 2804896, 17111472, 1175133, 4549782, 1078128, 6583232, 22868433, 2461619, 7009089, 557552, 4904376, 6289402, 3018726, 435016]
    each = [i for i in list(conn.execute("select state, sum(count) from names where name = '" + name + "' group by state"))]
    fine = [[i, 0] for i in list(set(states) - set([i[0] for i in each]))]
    each = sorted(each + fine, key = lambda x: x[0])
    each = [each[i][1]/state_totals[i] for i in range(len(state_totals))]
    return np.std(each)/sum(each)*len(each)            

def geoMeasure2(name):
    state_totals = [430161, 5815853, 3433745, 3598468, 30527811, 3627048, 3466933, 1450522, 640358, 10008972, 8593426, 981539, 4222176, 1205511, 15670010, 7435562, 3325885, 5514027, 5733608, 7796910, 4674750, 1415699, 12004123, 5784508, 7027352, 4068851, 969844, 8829082, 1088992, 2327275, 987775, 8633002, 1700657, 940408, 24465590, 14651955, 4285275, 2804896, 17111472, 1175133, 4549782, 1078128, 6583232, 22868433, 2461619, 7009089, 557552, 4904376, 6289402, 3018726, 435016]
    each = [i for i in list(conn.execute("select state, sum(count) from names where name = '" + name + "' group by state"))]
    fine = [[i, 0] for i in list(set(states) - set([i[0] for i in each]))]
    each = sorted(each + fine, key = lambda x: x[0])
    return 1000 * sum([i[1] for i in each[:5]])/sum([i[1] for i in each]) / orderArea([coords[i[0]] for i in each[:5]])

#1920-1950
def geo1year(name,year):
    each = [i for i in list(conn.execute("select state, sum(count) from names where name = '" + name + "' and year" + year + " group by state"))]
    fine = [[i, 0] for i in list(set(states) - set([i[0] for i in each]))]
    each = sorted(each + fine, key = lambda x: x[0])
    if year != ">1990":
        state_totals = [21996, 1768644, 1120251, 291733, 3152209, 561689, 741832, 343176, 107825, 930652, 1902212, 217356, 1218040, 246355, 3582847, 1660018, 865722, 1650934, 1358052, 2000376, 866126, 401879, 2692369, 1351447, 1771232, 1301535, 250296, 2246154, 347814, 646455, 207301, 1805007, 315678, 32037, 5929445, 3354171, 1290555, 453374, 4958322, 312387, 1266830, 325174, 1671940, 3765052, 327792, 1531228, 154593, 774011, 1524207, 1121739, 103701]
    else:
        state_totals = [161221, 1197113, 710705, 1838001, 12735311, 1357083, 849287, 231580, 186847, 4648517, 2735249, 239771, 805223, 383106, 3852197, 1878571, 787829, 1148468, 1275585, 1713266, 1444206, 264574, 2780765, 1465650, 1682891, 718606, 188545, 2525476, 176546, 494461, 272211, 2346519, 495901, 606932, 5697766, 3366101, 1001240, 945687, 3304813, 233181, 1045840, 196042, 1784382, 8809764, 1015761, 2090576, 103698, 1760123, 1449753, 430374, 88524]
    each = [each[i][1]/state_totals[i] for i in range(len(state_totals))]
    return np.std(each)/sum(each)*len(each)

    


def areas(array):
    f = lambda x,y: x[0]*y[1] - x[1]*y[0]
    return abs(sum([f(array[i], array[(i+1)%len(array)]) for i in range(len(array))]))/2

def orderArea(array):
    middle = [sum([i[0] for i in array])/len(array), sum([i[1] for i in array])/len(array)]
    array = sorted(array, key = lambda x: angle(middle, x))
    return areas(array)


def angle(point1, point2):
    one2two = [point2[0] - point1[0], point2[1] - point1[1]]
    dot = lambda x,y: sum([x[i] * y[i] for i in range(len(y))])
    a = math.acos(dot(one2two, [1,0])/math.sqrt(one2two[0]**2 + one2two[1]**2))
    if point2[1] < point1[1]:
    	a *= -1
    return a


def mapName(name,year,gender):
    e = mostPopularState(name, year, gender)
    e = sorted([[abbrevs[i[0]], i[1]] for i  in e], key = lambda x: x[0])


    
    with open('statesdata.csv', mode='w') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(['state','value'])
        for i in e:
            employee_writer.writerow(i)
    

    print('file://' + os.path.realpath("index.html"))
    webbrowser.open('file://' + os.path.realpath("index.html"))

def polyfit(x, y, degree):
    results = {}

    coeffs = np.polyfit(x, y, degree)

     # Polynomial Coefficients
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = np.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = np.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = np.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = np.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot

    return results


def graphAges():
    j = list(conn.execute("select name, low, med, high from totals order by -med"))
    for i in range(10):
        plt.scatter([i/10],[j[i][2]],color = 'r', s = 10)
        plt.plot([i/10] * 3, [j[i][c+1] for c in range(3)],'b')
    plt.xticks([i/10 for i in range(10)], [j[i][0] for i in range(10)])
    plt.ylabel("Age")
    plt.xlabel("Name")
    plt.title("Ten Oldest Names by Median")
    plt.show()
    
'''Practices:
cursor = conn.execute("select sum(count) from names")

cursor = conn.execute("select sum(count) from names where year = 2000")

cursor = conn.execute("select sum(count) from names where year = 2000 and gender = 'F'")

cursor = conn.execute("select distinct(year) from names")

cursor = conn.execute("select name, sum(count) from names where year > 2000 group by name, gender")

Ages:

j = list(conn.execute("select name, gender,low, med, high from totals where gender = 'F' order by med"))

#biggest range
print(max(j, key = lambda x: x[-1] - x[-3]))

'''




#TODO: Figure out how to print sum(count) by year


