from random import randint


class insertion(object):
    def sort(self, arr):
        print(arr[:20])
        sortPos = -1
        normPos = -1

        for i in arr:
            min = 100000
            normPos += 1
            swapConsec = 0

            values = arr[:normPos]

            for x in values:
                sortPos += 1

                if i < arr[normPos - sortPos]:
                    arr[normPos - swapConsec], arr[normPos - sortPos] = arr[normPos - sortPos], arr[normPos- swapConsec]
                    swapConsec += 1
                else:
                    swapConsec = 0
                    break

            sortPos = 0
            min = 100000

        return arr


def main():
    mySort = insertion()

    print(mySort.sort([randint(1, 10) for x in range(randint(10, 20))]))


if __name__ == '__main__':
    main()