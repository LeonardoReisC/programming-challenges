import sys

stdin = "".join(list(sys.stdin)).strip().split('\n\n')
output = []

n_cases = int(stdin[0])


class Highway:
    def __init__(self, tolls: list) -> None:
        self.tolls = tolls


class Photo:
    def __init__(self, d: int, h: int, m: int, word: str, km: int) -> None:
        self.d = d
        self.h = h
        self.m = m
        self.word = word
        self.km = km

    def __repr__(self) -> str:
        return f'{self.__dict__}'


class Car:
    def __init__(self, licence: str, highway: Highway) -> None:
        self._licence = licence
        self.photos: list[Photo] = []
        self.highway = highway

    def add(self, photo: Photo):
        self.photos.append(photo)

    @property
    def bill(self) -> float:
        total = 0.0
        self.photos.sort(key=lambda x: (x.d, x.h, x.m))

        while self.photos:
            photo_exit = self.photos.pop()
            if photo_exit.word == 'enter':
                continue

            if not self.photos:
                continue

            photo_entrance = self.photos.pop()
            if photo_entrance.word == 'exit':
                self.add(photo_entrance)
                continue
            distance = abs(photo_exit.km - photo_entrance.km)
            toll = self.highway.tolls[photo_entrance.h] / 100

            total += (toll * distance) + 1

        if total:
            total += 2.0

        return round(total, 2)

    def __str__(self) -> str:
        return f'{self._licence}\n{self.photos}'


for n in range(1, n_cases+1):
    case = stdin[n].strip().split('\n')

    highway = Highway(list(map(int, case[0].strip().split())))
    records = [x.split(' ') for x in case[1:]]

    licenses = {lic: Car(lic, highway)
                for lic in set(map(lambda x: x[0], records))}

    for record in records:
        args = list(map(int, record[1].split(':')))[1:]
        args.extend([record[2], int(record[3])])

        photo = Photo(*args)
        licenses[record[0]].add(photo)

    local_output = ''
    for license, car in licenses.items():
        bill = car.bill

        if not bill:
            continue

        local_output += f'{license} ${bill:.2f}\n'

    output.append('\n'.join(sorted(local_output.strip().split('\n'))))

print(('\n\n'.join(output)).rstrip(), end='\n')
