import re
pwd= 'avbdA$@'

num_search = bool(re.search(r'\d',pwd)) # 判断是否匹配到数字

upper_search = re.match('^(?:(?=.*[A-Z])).*$',pwd)

lower_search = re.match('^(?:(?=.*[a-z])).*$',pwd)

# (?=.*[a-z]) 称为正向肯定预查，加括号就是分组
#（?:exp）就是匹配exp本身

def judge_password(password):
    if len(password) >= 8:
        pattern = re.compile('[A-Z]+')
        match = pattern.findall(password)
        if match:
            pattern = re.compile('[a-z]+')
            match = pattern.findall(password)
            if match:
                pattern = re.compile('[0-9]+')
                match = pattern.findall(password)
                if match:
                    return 'True'
                else:
                    return '必须包含数字'
            else:
                return '必须包含小写字母'
        else:
            return '必须包含大写字母'
    else:
        return '长度必须大于8位'

def collect_vowels(s):
    """ (str) -> str

    Return the vowels (a, e, i, o, and u) from s.

    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('xyz')
    ''
    """

    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char
    return vowels

##if __name__ == "__main__":
##	import doctest
##	doctest.testmod(verbose=True)
