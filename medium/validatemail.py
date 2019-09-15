# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
def fun(s):
    seps = list(str(s).split("@"))
    if len(seps) == 2 :
        username = seps[0]
        vals = seps[1].split(".")
        if len(vals) == 2 :
            website = vals[0]
            ext = vals[1]
            valid_username = "abcdefghijklmnopqrstuvwqxyz123456789_-"
            valid_website = "abcdefghijklmnopqrstuvwqxyz123456789"
            
            if len(username) == 0 :
                return False

            for char in username :
                try :
                    valid_username.index(char)
                except :
                    return False
            
            for char in website :
                try :
                    valid_website.index(char)
                except :
                    return False
            
            if len(ext) >= 4 :
                return False
            if len(ext) < 1 :
                return False
            return True
        else :
            return False
    else :
        return False
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)