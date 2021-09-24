import time


class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        for color in TrafficLight.__color:
            print(f'Сейчас горит цвет {color}')
            if color == 'Красный':
                time.sleep(7)
            elif color == 'Жёлтый':
                time.sleep(2)
            else:
                time.sleep(4)



t_m = TrafficLight()
t_m.running()