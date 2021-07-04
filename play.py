import time

from road import Road, Action, print_state


def main():
    road = Road()

    def new_game():
        state = road.reset()
        print('New game:')
        print('')
        return state

    state = new_game()
    total_reward = 0
    while True:
        action = choose_action(road, state)
        state, reward, done = road.step(action)
        total_reward += reward
        print_state(state)
        print('Score:', total_reward)
        print('')
        if done:
            print('Game over!')
            print('')
        time.sleep(1)
        if done:
            state = new_game()


def choose_action(road, state):
    row = state[-2]
    car_index = road.car_index
    if row[car_index] == Road.OTHER_CAR:
        if car_index >= 1 and row[car_index - 1] == Road.EMPTY_SPACE:
            action = Action.MoveLeft
        elif car_index <= Road.NUMBER_OF_ROADS - 2 and row[car_index + 1] == Road.EMPTY_SPACE:
            action = Action.MoveRight
        else:
            action = Action.Stay
    else:
        action = Action.Stay
    return action


if __name__ == '__main__':
    main()
