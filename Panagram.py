import string

alpha = string.ascii_lowercase


def panagram(str):
    found = []
    for c in str:
        if c in alpha and c not in found:
            found.append(c)

            if len(found) == len(alpha):
                return True
            else:
                return False


print(panagram("hello my name is zxyrwdasfgrsgjldvhsdwp"))
