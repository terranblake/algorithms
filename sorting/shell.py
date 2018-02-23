from random import randint


class shell(object):
    def sort(self, arr, step):
        print(arr[:20])
        sortPos = -1
        normPos = -1

        for i in arr[:normPos:step]:
            min = 100000
            normPos += 1
            swapConsec = 0


            for x in arr[:normPos:step]:
                sortPos += 1

                if arr[(normPos * step) - sortPos] > i:
                    print(arr)
                    print('Comparing:',arr[(normPos * step) - sortPos] , 'to', arr[(normPos * step) - swapConsec])
                    print('Positions:',str((normPos * step) - sortPos) , '||', str((normPos * step) - swapConsec))

                    arr[(normPos * step) - swapConsec], arr[(normPos * step) - sortPos] = arr[(normPos * step) - sortPos], arr[(normPos * step)- swapConsec]
                    swapConsec += 1
                else:
                    swapConsec = 0
                    break

            sortPos = 0
            min = 100000

        return arr


def main():
    mySort = shell()

    input = [randint(1, 10) for x in range(randint(10, 20))]

    first = mySort.sort(input, 3)
    second = mySort.sort(input, 1)

    print(second)


if __name__ == '__main__':
    main()