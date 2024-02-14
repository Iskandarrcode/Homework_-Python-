date = "20th Oct 2052"

def sanalar(date):
    dt = {
        "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04",
        "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
        "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
    }
    umum = str()
    if len(date) == 12:
        a = date[0:1]
    if len(date) == 13:
        a = date[0:2]
        
    if len(date) == 12:
        for key, value in dt.items():
            if date[4:7] == key:
                umum = date[8:12] + "-" + value
    if len(date) == 13:
        for key, value in dt.items():
            if date[5:8] == key:
                umum = date[9:13] + "-" + value
                
    
    
    if len(a) == 1:
        umum = umum + "-" + "0" + a
    elif len(a) == 2:
        umum = umum + "-" + a
                
    return umum
    
print(sanalar(date))