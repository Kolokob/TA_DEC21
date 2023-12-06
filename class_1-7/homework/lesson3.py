from string import punctuation


class Lesson3:

    def recursion_reversed_str(self, string):
        string = ''.join([i if i not in '?!,. ' else '' for i in string.lower()])

        return self.recursive_check(string)

    def recursive_check(self, string):
        if len(string) <= 1:
            return True

        return string[0] == string[-1] and self.recursive_check(string[1:-1])


a = Lesson3()
print(a.recursion_reversed_str('Oh, who was it I saw? Oh, who?'))
