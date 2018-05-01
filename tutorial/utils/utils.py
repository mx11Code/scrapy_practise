def chinese_to_number(cn):
    digit = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
             u'零': 0, u'壹': 1, u'贰': 2, u'叁': 3, u'肆': 4, u'伍': 5, u'陆': 6, u'柒': 7, u'捌': 8, u'玖': 9,
             u'貮': 2, u'两': 2,
             }
    units = {u'十': 10, u'拾': 10, u'百': 100, u'佰': 100, u'千': 1000, u'仟': 1000, }
    unit_base_map = {u'万': 10000, u'萬': 10000, u'亿': 100000000, u'億': 100000000, u'兆': 1000000000000, }

    num = 0
    unit = 1
    unit_base = 1
    for char in cn.split()[0][::-1]:
        if char in digit:
            base = digit.get(char)
            num += base * unit * unit_base
            unit = 1
        elif char in units:
            unit = units.get(char) * unit
        elif char in unit_base_map:
            current_unit_base = unit_base
            unit_base = unit_base_map.get(char)
            if current_unit_base > unit_base:
                unit_base = unit_base * current_unit_base
    if unit != 1:
        num += 1 * unit * unit_base
    return num


# test_data = {
#     '零': 0,
#     '九': 9,
#     '十一': 11,
#     '十千零三': 10003,
#     '三百千零九十': 300090,
#     '一百二十三': 123,
#     '一千二百零三': 1203,
#     '一万一千一百零一': 11101,
#     '十万零三千六百零九': 103609,
#     '一百二十三万四千五百六十七': 1234567,
#     '一千一百二十三万四千五百六十七': 11234567,
#     '一亿一千一百二十三万四千五百六十七': 111234567,
#     '一百零二亿五千零一万零一千零三十八': 10250011038,
#     '一千一百一十一亿一千一百二十三万四千五百六十七': 111111234567,
#     '一兆一千一百一十一亿一千一百二十三万四千五百六十七': 1111111234567,
#     '一万亿': 1000000000000,
#     '一万零一百亿': 1010000000000,
#     '一万兆': 10000000000000000,
#     '一百万亿零五千': 100000000005000,
#     '一千万': 10000000,
# }
#
# for key, value in test_data.items():
#     calc = chinese_to_number(key)
#     if calc == value:
#         print(key, ":Passed")
#     else:
#         print("%s failed, expect %s, but got %s" % (key, value, calc))
