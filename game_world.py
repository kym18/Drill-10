#게임월드 모듈


#게임월드 표현
world = [ [], [], [] ]

#게임월드에 객체 담기
def add_object(o, depth = 0):
    world[depth].append(o)    #지정된 깊이의 레이어에 객체 추가

#게임월드 객체들을 몽땅 업데이트
def update():
    for layer in world:
        for o in layer:
            o.update()

#게임월드의 객체들 몽따 ㅇ그리기
def render():
    for layer in world:
        for o in layer:
            o.draw()

#객체 삭제
def remove_object(o):
    for layer in world:
        if o in layer: #list 안에 들어있니?
            layer.remove(o)
            return
    #print('왜 존재하지도 않는 걸 지우라굿?')
    raise ValueError('왜 존재하지도 않는 걸 지우라굿?')