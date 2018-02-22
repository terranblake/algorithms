from random import randint


class selection(object):
    def sort(self, arr):
        print(arr[:20])
        spos = -1
        pos = -1
        org = arr

        for i in arr:
            current = i
            min = 100
            swap = 1
            pos += 1

            for x in arr[pos:]:
                spos += 1

                if x < min:
                    min = x
                    swap = spos + pos

            arr[pos], arr[swap] = arr[swap], arr[pos]

            swap = 1
            spos = -1
            min = 100

        return arr


def main():
    mySort = selection()

    print(mySort.sort([randint(1, 100) for x in range(randint(10, 50))]))


if __name__ == '__main__':
    main()
