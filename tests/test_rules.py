from game_of_life.core.board import dead_state
from game_of_life.core.next_board import next_board_state

def test_next_state() -> None:
    '''
    dead board stays dead
    '''
    init_state1 = expected_next_state1 = dead_state(10,10)
    
    actual_next_state1 = next_board_state(init_state1)
    assert expected_next_state1 == actual_next_state1

    '''
    pattern that never changes
    '''
    init_state2 = [
    [False, False, False, False],
    [False, True,  True,  False],
    [False, True,  True,  False],
    [False, False, False, False],
    ]
    expected_next_state2 = [
    [False, False, False, False],
    [False, True,  True,  False],
    [False, True,  True,  False],
    [False, False, False, False],
    ]
    actual_next_state2 = next_board_state(init_state2)
    assert expected_next_state2 == actual_next_state2

    '''
    a lonely cell dies
    '''
    lonely_cell = [
    [False, False, False],
    [False, True,  False],
    [False, False, False],
    ]
    expected_lonely = [
    [False, False, False],
    [False, False, False],
    [False, False, False],
    ]
    actual_next_lonely = next_board_state(lonely_cell)
    assert expected_lonely == actual_next_lonely

    '''
    a dead cell with 3 neighbours becomes alive
    '''
    reproduction = [
    [True,  True,  False],
    [True,  False, False],
    [False, False, False],
    ]
    expected_reproduction = [
    [True,  True,  False],
    [True,  True,  False],
    [False, False, False],
    ]
    actual_next_reproduction = next_board_state(reproduction)
    assert expected_reproduction == actual_next_reproduction

    '''
    a live cell with more than 3 neighbours dies
    '''
    overpop = [
    [True, True, True],
    [True, True, True],
    [True, True, True],
    ]
    expected_overpop = [
    [True, False, True],
    [False, False, False],
    [True, False, True],
    ]
    actual_next_overpop = next_board_state(overpop)
    assert expected_overpop == actual_next_overpop


'''
test a period-2 pattern
'''
def test_blinker() -> None:

    blinker = [
    [False, False, False],
    [True,  True,  True],
    [False, False, False],
    ]
    blinker_step_1 = [
    [False, True,  False],
    [False, True,  False],
    [False, True,  False],
    ]
    blinker_step_2 = [
    [False, False, False],
    [True,  True,  True],
    [False, False, False],
    ]
    actual_step1 = next_board_state(blinker)
    actual_step2 = next_board_state(actual_step1)
    assert actual_step1 == blinker_step_1 and actual_step2 == blinker_step_2

'''
test glider in loop, board with edges
'''
def test_glider_edges() -> None:

    glider_start = [
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, True,  False, False, False, False, False, False, False],
    [False, False, False, True,  False, False, False, False, False, False],
    [False, True,  True,  True,  False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    ]

    glider_step_4 = [
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, True,  False, False, False, False, False, False],
    [False, False, False, False, True,  False, False, False, False, False],
    [False, False, True,  True,  True,  False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    ]
    actual_glider_step = glider_start
    for _ in range(4):
        actual_glider_step = next_board_state(actual_glider_step)

    assert actual_glider_step == glider_step_4


    glider_final_step = [
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, True, True],
    [False, False, False, False, False, False, False, False, True, True],
    ]

    for _ in range(23):
        actual_glider_step = next_board_state(actual_glider_step)
    
    assert actual_glider_step == glider_final_step


'''
test glider in loop, toroidal board
'''
def test_glider_toroidal() -> None:

    glider_start = [
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, True,  False, False, False, False, False, False, False],
    [False, False, False, True,  False, False, False, False, False, False],
    [False, True,  True,  True,  False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    ]
    actual_glider_step = glider_start
    for _ in range(40):
        actual_glider_step = next_board_state(actual_glider_step, 'toroidal')
    
    assert actual_glider_step == glider_start