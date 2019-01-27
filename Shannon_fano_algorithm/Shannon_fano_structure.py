import collections
import operator

class Shannon_fano_structure:

    code_book = {}


    def create_list(self, text):
        list = dict(collections.Counter(text))
        list_sorted = sorted(list.items(), key=operator.itemgetter(1), reverse=True)

        # format the final list as [letters, frquancy, code]
        final_list = []
        for key, value in list_sorted:
            final_list.append([key, value, ''])

        return final_list



    def divide_list(self, list):
        all_m = []
        left = 0
        right = 0
        for i in range(0, len(list)):
            for j in range(i + 1, len(list)):
                right += list[j][1]

            for l in range(i, -1, -1):
                left += list[l][1]

            between = abs(right - left)

            all_m.append(between)

            left = 0
            right = 0

        # find min minus
        min = [all_m[0], 0]
        for z in range(1, len(all_m)):
            if all_m[z] < min[0]:
                min = [all_m[z], z]

        # cutting
        index_of_min = min[1]

        return list[0:index_of_min + 1], list[index_of_min + 1:]


    def shannon_fano_structure(self, list):
        l1, l2 = self.divide_list(list)
        for i in l1:
            i[2] += '0'
            self.code_book[i[0]] = i[2]

        for i in l2:
            i[2] += '1'
            self.code_book[i[0]] = i[2]

        print('Dictionary -> ', self.code_book)

        if len(l1) > 1:
            self.shannon_fano_structure(l1)
        if len(l2) > 1:
            self.shannon_fano_structure(l2)

        return self.code_book


    def compression(self, text):
        after_compression = ''
        for i in text:
            for j in self.code_book.keys():
                if i == j:
                    after_compression += self.code_book[j]

        return after_compression


