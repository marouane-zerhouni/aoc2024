import re

def day4data(filename: str) -> str:
    with open(filename) as text_input:
        input_text = text_input.read().strip()
        return input_text

day4puzzle = day4data("day4input.txt")

def firststar(input_string: str) -> int:
    l_re = re.findall(r'(?=XMAS)', input_string, re.DOTALL)
    r_re = re.findall(r'(?=SAMX)', input_string, re.DOTALL)
    d_re = re.findall(r'(?=X(?:.{140})M(?:.{140})A(?:.{140})S)', input_string, re.DOTALL)
    u_re = re.findall(r'(?=S(?:.{140})A(?:.{140})M(?:.{140})X)', input_string, re.DOTALL)
    dr_re = re.findall(r'(?=X(?:.{141})M(?:.{141})A(?:.{141})S)', input_string, re.DOTALL)
    ul_re = re.findall(r'(?=S(?:.{141})A(?:.{141})M(?:.{141})X)', input_string, re.DOTALL)
    dl_re = re.findall(r'(?=X(?:.{139})M(?:.{139})A(?:.{139})S)', input_string, re.DOTALL)
    ur_re = re.findall(r'(?=S(?:.{139})A(?:.{139})M(?:.{139})X)', input_string, re.DOTALL)
    xmas_count =len(l_re)+len(ul_re)+len(dl_re)+len(r_re)+len(ur_re)+len(dr_re)+len(d_re)+len(u_re)
    return xmas_count

print(firststar(day4puzzle))

def secondstar(input_string: str) -> int:
    re_formula = re.findall(r'(?=M(?:.{1})M(?:.{139})A(?:.{139})S(?:.{1})S|M(?:.{1})S(?:.{139})A(?:.{139})M(?:.{1})S|S(?:.{1})M(?:.{139})A(?:.{139})S(?:.{1})M|S(?:.{1})S(?:.{139})A(?:.{139})M(?:.{1})M)', input_string, re.DOTALL)
    xmas_count = len(re_formula)
    return xmas_count

print(secondstar(day4puzzle))